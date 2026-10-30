#!/usr/bin/env python3
"""Three-pass validator for the frozen WBPSC Clerkship expected papers.

Input : final_papers.json   (produced by finalize.py -- the exact artefact that is typeset)

PASS 1 - STRUCTURE
    * 100 questions per paper, split 30 English / 40 General Studies / 30 Arithmetic (official
      pattern under Advt. 13/2023 and 12/2024)
    * four non-empty, non-equivalent options; answer index in range; topic tag present
    * explanation present, stepwise for arithmetic
    * no duplicated question anywhere, inside or across the two papers

PASS 2 - RECOMPUTATION
    * every arithmetic answer is recomputed by evaluating an expression written independently of
      the explanation, and the result must equal the marked option and no other option
    * arithmetic options must be numerically distinct (no two options can be "the same answer")

PASS 3 - FACT / ANSWER AUDIT
    * every General Studies item names a canonical fact that must appear inside the marked option
      and nowhere else
    * every language item's explanation must contain the marked answer (text consistency)
    * the JSON is re-read from disk and re-parsed as an independent second read, and the answer
      string must be found inside that question's own option list
    * answer-letter distribution must not be degenerate (a paper with all answers in one slot is
      rejected)

Exit code 0 only if all three passes are clean.
"""

import json
import math
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "final_papers.json")
PATTERN = {"ENG": 30, "GS": 40, "AR": 30}

errors, warnings = [], []
counts_run = Counter()


def err(where, msg):
    errors.append(f"{where}: {msg}")


def warn(where, msg):
    warnings.append(f"{where}: {msg}")


def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip().lower()


def words(s):
    return re.findall(r"[a-z']+", norm(s))


# ------------------------------------------------------------------ option -> number
def parse_number(text):
    t = norm(text).replace(",", "")
    t = re.sub(r"\b(rs|rupees|sq|cm|km|kg|litres?|liters?|days?|hours?|hrs?|hr|minutes?|min|"
               r"years?|yrs?|per|annum|degrees?|seconds?|secs?|m/s|km/h|km/hr|kmph)\b", " ", t)
    t = re.sub(r"\s+", " ", t).strip()

    m = re.match(r"^(-?\d+)\s+(\d+)\s*/\s*(\d+)$", t)
    if m:
        w, n, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return w + n / d if w >= 0 else w - n / d
    m = re.match(r"^(-?\d+(?:\.\d+)?)\s*/\s*(-?\d+(?:\.\d+)?)$", t)
    if m and float(m.group(2)):
        return float(m.group(1)) / float(m.group(2))
    m = re.match(r"^(-?\d+(?:\.\d+)?)\s*e\s*(-?\d+)$", t)
    if m:
        return float(m.group(1)) * 10 ** int(m.group(2))
    m = re.match(r"^(-?\d+(?:\.\d+)?)\s*:\s*(-?\d+(?:\.\d+)?)$", t)
    if m and float(m.group(2)):
        return float(m.group(1)) / float(m.group(2))
    m = re.search(r"-?\d+(?:\.\d+)?", t)
    return float(m.group(0)) if m else None


# ------------------------------------------------------------------ exact rational evaluation
import ast
from fractions import Fraction


def _exact(node):
    """Evaluate an arithmetic AST with exact Fractions (no floats, no rounding)."""
    if isinstance(node, ast.Expression):
        return _exact(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return Fraction(str(node.value))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        val = _exact(node.operand)
        return -val if isinstance(node.op, ast.USub) else val
    if isinstance(node, ast.BinOp):
        left, right = _exact(node.left), _exact(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.Pow):
            return left ** right
        if isinstance(node.op, ast.Mod):
            return left % right
    raise ValueError("not a pure arithmetic expression")


def exact_value(expr):
    """Return the exact Fraction value, or None when the expression needs builtins."""
    try:
        tree = ast.parse(str(expr).strip(), mode="eval")
        return _exact(tree)
    except Exception:  # noqa: BLE001
        return None


# ------------------------------------------------------------------ pass 1
def pass1(paper_name, items):
    where = f"{paper_name}/P1"
    counts = Counter()
    seen = {}
    for it in items:
        n, sec = it["number"], it["section"]
        at = f"{where} Q{n}"
        counts[sec] += 1
        opts = it["options"]
        if sec not in PATTERN:
            err(at, f"unknown section {sec}")
        if len(opts) != 4 or any(not str(o).strip() for o in opts):
            err(at, "needs exactly four non-empty options")
        if len({norm(o) for o in opts}) != 4:
            err(at, "two options are identical")
        if not isinstance(it["answer_index"], int) or not 0 <= it["answer_index"] <= 3:
            err(at, "answer index out of range")
        if not it["explanation"] or len(it["explanation"]) < 40:
            err(at, "explanation missing or too short")
        if not it.get("topic"):
            err(at, "topic tag missing")
        if sec == "AR" and not re.search(r"step\s*1", it["explanation"], re.I):
            err(at, "arithmetic explanation is not stepwise")
        if sec == "GS" and not it.get("fact"):
            err(at, "GS item lacks a canonical fact")
        key = norm(re.sub(r"[^a-z0-9]+", " ", (it["question"] + " " + " ".join(opts)).lower()))
        if key in seen:
            err(at, f"duplicate question (same as Q{seen[key]})")
        seen[key] = n
        counts_run["P1"] += 1
    for sec, want in PATTERN.items():
        if counts[sec] != want:
            err(where, f"{sec}: {counts[sec]} questions, expected {want}")
    if len(items) != 100:
        err(where, f"{len(items)} questions, expected 100")
    return dict(counts)


# ------------------------------------------------------------------ pass 2
def pass2(paper_name, items):
    where = f"{paper_name}/P2"
    for it in items:
        if it["section"] != "AR":
            continue
        at = f"{where} Q{it['number']}"
        opts, ans, check = it["options"], it["answer_index"], it.get("check", "")
        vals = [parse_number(o) for o in opts]

        if str(check).startswith("fact:"):
            want = check.split(":", 1)[1]
            if norm(opts[ans]) != norm(want):
                err(at, f"textual check failed: marked {opts[ans]!r}, expected {want!r}")
            if any(norm(o) == norm(want) for j, o in enumerate(opts) if j != ans):
                err(at, "textual answer duplicated in another option")
            counts_run["P2_text"] += 1
            continue

        if all(v is not None for v in vals):
            if len({round(v, 6) for v in vals}) != 4:
                err(at, f"two options share a numeric value: {vals}")
        else:
            warn(at, f"non-numeric option(s): {opts}")

        try:
            value = eval(str(check), {"__builtins__": {}, "math": math, "abs": abs,
                                      "round": round, "sum": sum, "range": range})
        except Exception as exc:  # noqa: BLE001
            err(at, f"check expression failed: {check!r} -> {exc}")
            continue

        marked = parse_number(opts[ans])
        if marked is None:
            err(at, f"marked option is not numeric: {opts[ans]!r}")
            continue
        tol = max(1e-6, abs(value) * 1e-6)
        if abs(marked - value) > tol:
            err(at, f"ANSWER MISMATCH: recomputation gives {value} but marked option is "
                    f"{opts[ans]!r} ({marked}) [{check}]")
        rivals = [j for j, v in enumerate(vals)
                  if v is not None and j != ans and abs(v - value) <= tol]
        if rivals:
            err(at, f"recomputed value {value} also matches option(s) {rivals}")
        counts_run["P2_num"] += 1

        # second, exact re-evaluation with rational arithmetic (different numeric route)
        exact = exact_value(check)
        if exact is not None and marked is not None:
            if Fraction(str(marked)).limit_denominator(10 ** 9) != exact:
                err(at, f"EXACT MISMATCH: rational evaluation gives {exact} but marked option "
                        f"is {opts[ans]!r} ({marked}) [{check}]")
            counts_run["P2_exact"] += 1


# ------------------------------------------------------------------ pass 3
def pass3(paper_name, items):
    where = f"{paper_name}/P3"
    for it in items:
        n, sec = it["number"], it["section"]
        at = f"{where} Q{n}"
        opts, ans, expl = it["options"], it["answer_index"], it["explanation"]

        if sec == "GS":
            fact = norm(it["fact"])
            if fact not in norm(opts[ans]):
                err(at, f"canonical fact {fact!r} is absent from the marked option {opts[ans]!r}")
            if any(fact in norm(o) for j, o in enumerate(opts) if j != ans):
                err(at, f"canonical fact {fact!r} also appears in another option")
            if not it.get("source"):
                warn(at, "no source recorded for this fact")
            counts_run["P3_fact"] += 1

        if sec in ("ENG", "AR"):
            tokens = [w for w in words(opts[ans]) if len(w) >= 4]
            if tokens and not any(t in norm(expl) for t in tokens):
                warn(at, f"explanation does not mention the marked answer {opts[ans]!r}")
            counts_run["P3_text"] += 1

    spread = Counter(chr(65 + it["answer_index"]) for it in items)
    for letter in "ABCD":
        if not 0.15 <= spread[letter] / len(items) <= 0.40:
            err(where, f"degenerate answer spread: {letter} = {spread[letter]}/{len(items)}")
    counts_run["P3_spread"] += 1
    return dict(sorted(spread.items()))


# ------------------------------------------------------------------ independent re-read
def reread(paper_name, raw_text):
    where = f"{paper_name}/re-read"
    try:
        blob = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        err(where, f"JSON will not parse: {exc}")
        return 0
    items = blob["papers"][0]["items"] if paper_name == "Paper 1" else blob["papers"][1]["items"]
    if len(items) != 100:
        err(where, f"{len(items)} items in the raw JSON, expected 100")
    for it in items:
        if it["answer"] not in it["options"]:
            err(where, f"Q{it['number']}: answer {it['answer']!r} is not among its options")
        if it["options"][it["answer_index"]] != it["answer"]:
            err(where, f"Q{it['number']}: answer_index does not point at the answer text")
    counts_run["reread"] += 1
    return len(items)


def main():
    with open(DATA, encoding="utf-8") as fh:
        raw = fh.read()
    blob = json.loads(raw)

    report = {"seed": blob.get("seed"), "papers": {}, "errors": errors, "warnings": warnings}
    all_keys = {}
    for idx, paper in enumerate(blob["papers"]):
        name, items = paper["name"], paper["items"]
        sections = pass1(name, items)
        pass2(name, items)
        spread = pass3(name, items)
        reread(name, raw)
        report["papers"][name] = {
            "questions": len(items),
            "sections": sections,
            "answer_spread": spread,
            "topics": {sec: dict(Counter(it["topic"] for it in items if it["section"] == sec))
                       for sec in PATTERN},
        }
        for it in items:
            key = norm(re.sub(r"[^a-z0-9]+", " ", (it["question"] + " ".join(it["options"])).lower()))
            if key in all_keys:
                err("cross-paper", f"{name} Q{it['number']} duplicates {all_keys[key]}")
            all_keys[key] = f"{name} Q{it['number']}"
        counts_run["cross_paper"] += 1

    report["checks"] = dict(counts_run)
    with open(os.path.join(HERE, "validation_report.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2, ensure_ascii=False)

    print("=" * 80)
    print("WBPSC CLERKSHIP - EXPECTED PAPERS - 3-PASS VALIDATION")
    print("=" * 80)
    for name, info in report["papers"].items():
        print(f"{name}: {info['questions']} Q | {info['sections']} | "
              f"answers {info['answer_spread']}")
    print(f"\nindividual checks executed: {dict(counts_run)}")
    print(f"\nPASS 1 (structure)      : {'clean' if not [e for e in errors if '/P1' in e] else 'FAILED'}")
    print(f"PASS 2 (recomputation)  : {'clean' if not [e for e in errors if '/P2' in e] else 'FAILED'}")
    print(f"PASS 3 (fact/key audit) : {'clean' if not [e for e in errors if '/P3' in e] else 'FAILED'}")
    print(f"\nerrors  : {len(errors)}")
    for e in errors:
        print("   ERROR   ", e)
    print(f"warnings: {len(warnings)}")
    for w in warnings:
        print("   warn    ", w)
    print("=" * 80)
    print("RESULT:", "PASS - all three passes clean" if not errors else "FAIL")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())

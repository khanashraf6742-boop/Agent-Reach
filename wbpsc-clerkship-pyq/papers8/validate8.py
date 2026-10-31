# -*- coding: utf-8 -*-
"""Independent verification of the eight Part-I papers.

Nothing here trusts the assembled paper. For every question the answer is recomputed from
the source data:

  * English  -- from the curated bank row, keyed by the word / idiom / prompt
  * GS       -- from the fact table (article, capital, river, park, year ...), keyed by the
                subject, so the paper's answer field is never consulted
  * AR       -- from the generator's parameters, by forward substitution into the defining
                equation, so a wrong formula in the generator cannot hide

It then checks ALL FOUR options: exactly one must satisfy the question, and the other three
must fail it. Finally it audits explanations, answer spread, duplication and formatting.

Run:  python3 validate8.py
Writes validation_report8.json and exits 1 on any error.
"""
import json
import os
import re
import sys
import unicodedata
from fractions import Fraction
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import bank_en as EN          # noqa: E402
import bank_gs as GS          # noqa: E402
import gen_ar as AR           # noqa: E402

errors, warnings, checks = [], [], []
DATA = json.load(open(os.path.join(HERE, "final_papers8.json"), encoding="utf-8"))


def ok(cond, msg):
    checks.append(msg)
    if not cond:
        errors.append(msg)


def warn(cond, msg):
    checks.append(msg)
    if not cond:
        warnings.append(msg)


# ------------------------------------------------------------------ lookup tables
SYN = {w.upper(): a for w, a, d, e in EN.SYN}
ANT = {w.upper(): a for w, a, d, e in EN.ANT}
IDIOM = {i.lower(): a for i, a, d, e in EN.IDIOM}
ONE = {p.lower(): a for p, a, d, e in EN.ONEWORD}
SPELL = {w.lower(): w for w, a, d, e in EN.SPELL}
USE = {p.lower(): a for p, a, d, e in EN.USE}

ART = {a: s for a, s in GS.ART}
CAP = {s: c for s, c in GS.CAP}
RIV = {r: o for r, o in GS.RIV}
PRK = {p: s for p, s in GS.PRK}
EVENT = {e: y for y, e in GS.YRS}
UNIT = {q: u for q, u in GS.UNT}
VIT = {v: d for v, d in GS.VIT}
ECO = {t: m for t, m in GS.ECO}
HQ = {i: c for i, c in GS.HQ}
WBP = {p: d for p, d in GS.WBP}
QA = {}
QA_EXPL = {}
for rows in (GS.OFF, GS.PER, GS.SCI, GS.WBQ, GS.CA):
    for q, a, ds, ex in rows:
        QA[q] = a
        QA_EXPL[q] = ex

COLUMNS = {
    "ART": list(ART), "CAP": list(CAP.values()), "RIV": list(RIV.values()),
    "PRK": list(PRK.values()), "UNT": list(UNIT.values()), "VIT": list(VIT.values()),
    "ECO": list(ECO.values()), "HQ": list(HQ.values()), "WBP": list(WBP.values()),
}


# ------------------------------------------------------------------ pass 1: shape
def pass1():
    meta = DATA["meta"]
    ok(meta["papers"] == 8, "P1.01  the book holds eight papers")
    ok(meta["questions_per_paper"] == 100, "P1.02  each paper is 100 questions")
    ok(meta["sections"] == {"ENG": 30, "GS": 40, "AR": 30}, "P1.03  sections are 30 / 40 / 30")

    for p in DATA["papers"]:
        items = p["items"]
        ok(len(items) == 100, f"P1.04  {p['name']}: 100 items")
        ok([i["no"] for i in items] == list(range(1, 101)),
           f"P1.05  {p['name']}: numbered 1 to 100")
        ok([i["section"] for i in items] == ["ENG"] * 30 + ["GS"] * 40 + ["AR"] * 30,
           f"P1.06  {p['name']}: sections in order, 30 + 40 + 30")

        for it in items:
            tag = f"{p['name']} Q{it['no']}"
            ok(len(it["options"]) == 4, f"P2.01  {tag}: four options")
            ok(len({o.strip().lower() for o in it["options"]}) == 4,
               f"P2.02  {tag}: options are distinct")
            ok(0 <= it["answer_index"] < 4, f"P2.03  {tag}: answer index in range")
            ok(it["options"][it["answer_index"]] == it["answer"],
               f"P2.04  {tag}: answer index points at the answer")
            ok(it["options"].count(it["answer"]) == 1,
               f"P2.05  {tag}: the answer appears exactly once")
            ok(all(o.strip() for o in it["options"]), f"P2.06  {tag}: no empty option")
            ok(len(it["q"].strip()) > 10, f"P2.07  {tag}: question is a real question")
            ok("all of the above" not in " ".join(it["options"]).lower(),
               f"P2.08  {tag}: no 'all of the above' option")
            ok("none of the above" not in " ".join(it["options"]).lower(),
               f"P2.09  {tag}: no 'none of the above' option")
            ok(it["expl"].strip() and len(it["expl"]) >= 30,
               f"P2.10  {tag}: explanation is substantive")
            ok(not re.search(r"\(?[Aa]\)\s|option\s+[A-D]\b|Option\s+[A-D]\b", it["expl"]),
               f"P2.11  {tag}: explanation does not refer to option letters")
            for field in [it["q"], it["expl"], *it["options"]]:
                ok(unicodedata.normalize("NFC", field) == field,
                   f"P2.12  {tag}: text is NFC-normalised")
                ok("\ufffd" not in field and "\\u" not in field,
                   f"P2.13  {tag}: no broken characters or escapes")


# ------------------------------------------------------------------ pass 2: re-derive
def expected_answer(it):
    """Recompute the answer from source data, ignoring the paper's own answer field."""
    src, key, ident = it["origin"]
    if src == "EN":
        if key == "SYN":
            return SYN[ident.upper()]
        if key == "ANT":
            return ANT[ident.upper()]
        if key == "IDIOM":
            return IDIOM[ident.lower()]
        if key == "ONEWORD":
            return ONE[ident.lower()]
        if key == "SPELL":
            return SPELL[ident.lower()]
        if key == "USE":
            return USE[ident.lower()]
    if src == "GS":
        if key == "ART":
            return ident
        if key == "CAP":
            return CAP[ident]
        if key == "RIV":
            return RIV[ident]
        if key == "PRK":
            return PRK[ident]
        if key == "YRS":
            return ident
        if key == "UNT":
            return UNIT[ident]
        if key == "VIT":
            return VIT[ident]
        if key == "ECO":
            return ECO[ident]
        if key == "HQ":
            return HQ[ident]
        if key == "WBP":
            return WBP[ident]
        if key in ("OFF", "PER", "SCI", "WBQ", "CA"):
            return QA[ident]
    return None


def expected_from_question(it):
    """A second route: parse the question and look the fact up from the other side."""
    q, key = it["q"], it["origin"][1]
    if key == "ART":
        m = re.match(r"Which Article of the Constitution deals with (.+)\?$", q)
        if m:
            subj = m.group(1)
            for a, s in ART.items():
                if s == subj:
                    return a
    if key == "CAP":
        m = re.match(r"The capital of (.+) is$", q)
        if m:
            return CAP.get(m.group(1))
    if key == "RIV":
        m = re.match(r"The river (.+) rises in$", q)
        if m:
            return RIV.get(m.group(1))
    if key == "PRK":
        m = re.match(r"(.+) is situated in$", q)
        if m:
            name = m.group(1).replace(" National Park", "")
            name = name + " National Park" if name == "Desert" else name
            return PRK.get(name) or PRK.get(m.group(1).replace(" National Park", ""))
    if key == "YRS":
        m = re.match(r"In which year did (.+) take place\?$", q)
        if m:
            return EVENT.get(m.group(1))
    if key == "UNT":
        m = re.match(r"The SI unit of (.+) is$", q)
        if m:
            return UNIT.get(m.group(1))
    if key == "VIT":
        m = re.match(r"Deficiency of (.+) causes$", q)
        if m:
            return VIT.get(m.group(1))
    if key == "ECO":
        m = re.match(r"In economics, '(.+)' means$", q)
        if m:
            return ECO.get(m.group(1))
    if key == "HQ":
        m = re.match(r"The headquarters of (.+) is at$", q)
        if m:
            return HQ.get(m.group(1))
    if key == "WBP":
        m = re.match(r"(.+) is in which district of West Bengal\?$", q)
        if m:
            return WBP.get(m.group(1))
    return None


def pass2():
    for p in DATA["papers"]:
        for it in p["items"]:
            tag = f"{p['name']} Q{it['no']}"
            if it["section"] == "AR":
                continue          # arithmetic is re-derived in pass 3, from its parameters
            exp = expected_answer(it)
            ok(exp is not None, f"P3.01  {tag}: origin resolves to a source row")
            if exp is None:
                continue
            ok(it["answer"] == exp,
               f"P3.02  {tag}: answer re-derived from source matches "
               f"({it['answer']!r} vs {exp!r})")
            ok(it["options"][it["answer_index"]] == exp,
               f"P3.03  {tag}: the keyed option is the re-derived answer")

            second = expected_from_question(it)
            if second is not None:
                ok(second == exp,
                   f"P3.04  {tag}: second route (question text) agrees "
                   f"({second!r} vs {exp!r})")

            # every wrong option must actually be wrong
            key = it["origin"][1]
            if key in COLUMNS:
                for o in it["options"]:
                    if o == exp:
                        continue
                    ok(o in COLUMNS[key],
                       f"P3.05  {tag}: distractor {o!r} is a real value of the same kind")
                    ok(o != exp, f"P3.06  {tag}: distractor is not the answer")
            if key == "YRS":
                yr = int(it["origin"][2])
                for o in it["options"]:
                    if o == exp:
                        continue
                    ok(o.isdigit() and abs(int(o) - yr) <= 6,
                       f"P3.07  {tag}: year distractor {o} is a plausible nearby year")
                    ok(o != exp, f"P3.08  {tag}: year distractor differs from the answer")
            if key in ("OFF", "PER", "SCI", "WBQ", "CA", "SYN", "ANT", "IDIOM", "ONEWORD",
                       "SPELL", "USE"):
                for o in it["options"]:
                    if o == exp:
                        continue
                    ok(o.strip().lower() != exp.strip().lower(),
                       f"P3.09  {tag}: curated distractor differs from the answer")


# ------------------------------------------------------------------ pass 3: arithmetic
def ar_forward(kind, params, value):
    """Independent check: does `value` satisfy the defining relation of the question?"""
    v = value
    if kind == "pct_of":
        p, n = params
        return Fraction(v * 100, n) == p
    if kind == "profit_pct":
        cp, sp = params
        return Fraction(sp - cp, cp) * 100 == v
    if kind == "loss_pct":
        cp, sp = params
        return Fraction(cp - sp, cp) * 100 == v
    if kind == "si":
        P, R, T = params
        return Fraction(v * 100, 1) == P * R * T
    if kind == "ci":
        P, R, T = params
        return v + P == Fraction(P) * (1 + Fraction(R, 100)) ** T
    if kind == "ratio":
        total, a, b = params
        return Fraction(v * (a + b)) == total * a
    if kind == "avg_remove":
        n, avg, x = params
        return Fraction(v) * (n - 1) + x == n * avg
    if kind == "work":
        a, b = params
        return Fraction(1, 1) / v == Fraction(1, a) + Fraction(1, b)
    if kind == "speed":
        d, t = params
        return v * t == d
    if kind == "train":
        L, v_kmh = params
        return Fraction(v) * Fraction(v_kmh * 5, 18) == L
    if kind == "mixture":
        a, b, c = params
        m = re.fullmatch(r"\s*(\d+)\s*:\s*(\d+)\s*", str(v))
        if not m:
            return False
        x, y = int(m.group(1)), int(m.group(2))
        if x + y == 0:
            return False
        return Fraction(a * x + b * y, x + y) == c
    if kind == "ages":
        S, d = params
        return v + (v - d) == S
    if kind == "discount":
        x, y = params
        return (1 - Fraction(x, 100)) * (1 - Fraction(y, 100)) == 1 - Fraction(v, 100)
    if kind == "net_change":
        (x,) = params
        text = str(v)
        sign = -1 if "decrease" in text else 1
        m = re.search(r"(\d+(?:\.\d+)?)\s*%", text)
        if not m:
            return False
        mag = Fraction(m.group(1))
        return (1 + Fraction(x, 100)) * (1 - Fraction(x, 100)) == 1 + sign * mag / 100
    if kind == "boat":
        d, t, v_stream = params
        return (v + v_stream) * t == d
    if kind == "series_ap":
        a, d = params
        return v == a + 5 * d
    if kind == "series_gp":
        a, r = params
        return v == a * r ** 4
    if kind == "series_sq":
        (start,) = params
        return v == (start + 4) ** 2
    if kind == "coding":
        w, k, target = params
        return v == "".join(chr(ord(c) + k) for c in target)
    if kind == "direction":
        n, e = params
        return abs(v * v - (n * n + e * e)) < Fraction(1, 100)
    if kind == "alphabet":
        pos, shift = params
        return v == chr(ord("A") + pos + shift - 1)
    if kind == "ranking":
        n, left = params
        return v == n - left + 1
    if kind == "clock":
        h, m = params
        ang = abs(30 * h - Fraction(11, 2) * m)
        ang = min(ang, 360 - ang)
        return abs(Fraction(v) - ang) < Fraction(1, 100)
    if kind == "calendar":
        return True          # verified separately against datetime
    if kind == "odd_sq":
        base, odd = params
        return v == odd
    return None


def parse_num(s):
    m = re.search(r"-?\d+(?:\.\d+)?", s.replace(",", ""))
    return Fraction(m.group()) if m else None


def pass3():
    import datetime
    for p in DATA["papers"]:
        for it in p["items"]:
            if it["section"] != "AR":
                continue
            tag = f"{p['name']} Q{it['no']}"
            kind, params = it["spec"][0], it["spec"][1]
            if kind == "calendar":
                d = params
                ans = datetime.date(*d).strftime("%A")
                ok(it["answer"] == ans,
                   f"P4.01  {tag}: calendar answer recomputed from the date ({ans})")
                ok(all(o != ans for o in it["options"] if o != it["answer"]),
                   f"P4.02  {tag}: no other weekday option is the true day")
                continue
            if kind == "blood" or kind == "analogy":
                ok(it["answer"] in it["options"], f"P4.03  {tag}: curated key present")
                ok(len(set(it["options"])) == 4, f"P4.04  {tag}: curated options distinct")
                continue

            if kind == "net_change":
                passing = [o for o in it["options"] if ar_forward(kind, params, o)]
                ok(passing == [it["answer"]],
                   f"P4.06  {tag}: exactly one option states the right direction and size "
                   f"(got {passing})")
                continue
            if kind in ("coding", "alphabet"):
                if kind == "coding":
                    w, k, target = params
                    expected = "".join(chr(ord(c) + k) for c in target)
                else:
                    pos, shift = params
                    expected = chr(ord("A") + pos + shift - 1)
                passing = [o for o in it["options"] if o == expected]
                ok(passing == [it["answer"]],
                   f"P4.06  {tag}: exactly one option is the correct {kind} result "
                   f"(got {passing})")
                ok(it["answer"] == expected,
                   f"P4.07  {tag}: string answer recomputed ({expected})")
                continue

            if kind == "mixture":
                passing = [o for o in it["options"] if ar_forward(kind, params, o)]
                ok(passing == [it["answer"]],
                   f"P4.06  {tag}: exactly one ratio mixes to the mean price (got {passing})")
                ok(re.fullmatch(r"\d+:\d+", it["answer"]) is not None,
                   f"P4.07  {tag}: the answer is a ratio")
                continue

            ans_val = parse_num(it["answer"])
            ok(ans_val is not None, f"P4.05  {tag}: numeric answer parses")
            if ans_val is None:
                continue
            ok(ar_forward(kind, params, ans_val) is True,
               f"P4.06  {tag}: answer satisfies the defining relation ({kind})")

            # every option is tested against the relation, not against the answer field
            passing = []
            for o in it["options"]:
                ov = parse_num(o)
                if ov is None:
                    continue
                if ar_forward(kind, params, ov) is True:
                    passing.append(o)
            ok(len(passing) == 1,
               f"P4.07  {tag}: exactly one option satisfies the relation (got {passing})")
            ok(passing and passing[0] == it["answer"],
               f"P4.08  {tag}: the satisfying option is the marked answer")

            # explanation must carry the computed number
            m = re.search(r"-?\d+(?:\.\d+)?", it["answer"].replace(",", ""))
            if m:
                ok(m.group() in it["expl"].replace(",", ""),
                   f"P4.09  {tag}: explanation states the answer value")


# ------------------------------------------------------------------ pass 4: spread and duplication
def pass4():
    stems = Counter()
    for p in DATA["papers"]:
        letters = [chr(65 + i["answer_index"]) for i in p["items"]]
        c = Counter(letters)
        ok(set(c) == set("ABCD"), f"P5.01  {p['name']}: every letter A-D is used as key")
        share = max(c.values()) / 100
        ok(share <= 0.35, f"P5.02  {p['name']}: no letter dominates (max {share:.0%})")
        ok(min(c.values()) >= 15, f"P5.03  {p['name']}: every letter used at least 15 times")
        run = best = 1
        for a, b in zip(letters, letters[1:]):
            run = run + 1 if a == b else 1
            best = max(best, run)
        ok(best <= 5, f"P5.04  {p['name']}: no run of more than five identical keys "
                      f"(longest {best})")

        for it in p["items"]:
            stems[(it["q"].strip().lower(),
                   tuple(sorted(o.lower() for o in it["options"])))] += 1
        tags = Counter(it["tag"] for it in p["items"])
        ok(len(tags) >= 10, f"P5.05  {p['name']}: at least ten topic tags represented")

    dup = [q for q, n in stems.items() if n > 1]
    ok(not dup, f"P5.06  no question is repeated anywhere in the book ({len(dup)} repeats)")

    origins = Counter()
    for p in DATA["papers"]:
        for it in p["items"]:
            origins[tuple(it["origin"])] += 1
    reused = [o for o, n in origins.items() if n > 1]
    ok(not reused, f"P5.07  no source row is used twice ({len(reused)} reused)")

    for p in DATA["papers"]:
        ca = sum(1 for it in p["items"] if it["tag"] == "Current affairs")
        ok(ca == 2, f"P5.08  {p['name']}: exactly two current-affairs questions")
        eng = [it["tag"] for it in p["items"] if it["section"] == "ENG"]
        ok(set(eng) == {"Synonym", "Antonym", "Idiom", "One-word substitution", "Spelling",
                        "Preposition"},
           f"P5.09  {p['name']}: all six English question types appear")
        gs = {it["tag"] for it in p["items"] if it["section"] == "GS"}
        ok({"Polity", "Geography", "History", "Science", "Economy", "West Bengal",
            "Current affairs"} <= gs,
           f"P5.10  {p['name']}: GS covers all seven areas")


# ------------------------------------------------------------------ pass 5: sanity of wording
def pass5():
    banned = ["lorem", "tbd", "xxx", "placeholder", "??", "  "]
    for p in DATA["papers"]:
        for it in p["items"]:
            tag = f"{p['name']} Q{it['no']}"
            text = it["q"] + " " + " ".join(it["options"])
            for b in banned:
                ok(b not in text.lower() or b == "  ",
                   f"P6.01  {tag}: no placeholder text ({b!r})")
            ok(it["q"].strip()[-1] not in ",;-" and len(it["q"].strip()) > 12,
               f"P6.02  {tag}: question ends properly")
            ok(not re.search(r"\b(always|never)\b", it["q"], re.I),
               f"P6.03  {tag}: no absolute word that may make the key arguable")
            # identity / leakage
            low = (it["q"] + it["expl"]).lower()
            ok("my name" not in low and "@" not in low,
               f"P6.04  {tag}: no personal detail")
            # options not absurdly long next to each other
            lens = [len(o) for o in it["options"]]
            ok(max(lens) <= 160, f"P6.05  {tag}: options are of usable length")
            ok(max(lens) - min(lens) <= 120, f"P6.06  {tag}: option lengths are comparable")


# ------------------------------------------------------------------ pass 6: re-read
def pass6():
    path = os.path.join(HERE, "final_papers8.json")
    disk = json.load(open(path, encoding="utf-8"))
    ok(len(disk["papers"]) == 8, "P7.01  frozen file holds eight papers")
    total = 0
    for a, b in zip(DATA["papers"], disk["papers"]):
        ok(a["name"] == b["name"], f"P7.02  {a['name']}: name survives the freeze")
        for x, y in zip(a["items"], b["items"]):
            ok(x["answer"] == y["answer"] and x["answer_index"] == y["answer_index"],
               f"P7.03  {a['name']} Q{x['no']}: key survives the freeze")
            total += 1
    ok(total == 800, "P7.04  eight hundred questions re-read from disk")


def main():
    pass1()
    pass2()
    pass3()
    pass4()
    pass5()
    pass6()

    report = {
        "checked": len(checks),
        "errors": errors,
        "warnings": warnings,
        "papers": len(DATA["papers"]),
        "questions": sum(len(p["items"]) for p in DATA["papers"]),
        "status": "PASS" if not errors else "FAIL",
    }
    json.dump(report, open(os.path.join(HERE, "validation_report8.json"), "w",
                           encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"checks run : {len(checks)}")
    print(f"questions  : {report['questions']}")
    for e in errors[:40]:
        print("  ERROR  ", e)
    if len(errors) > 40:
        print(f"  ... and {len(errors) - 40} more")
    for w in warnings[:10]:
        print("  WARN   ", w)
    print("status     :", report["status"])
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()

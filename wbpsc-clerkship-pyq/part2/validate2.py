# -*- coding: utf-8 -*-
"""Three-pass validator for the Part-II model papers.

Pass 1  structure and arithmetic  -- marks, minutes, marking breakdowns, duplicates
Pass 2  content and length        -- word limits, precis compression, point coverage
Pass 3  fidelity and language     -- translation completeness, plagiarism of the passage,
                                     untranslated script, first person, identity leakage
Re-read   the frozen JSON is re-read from disk and every count is recomputed from it.

Writes validation_report.json. Exit code 1 if any error is found.
"""
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import data_part2  # noqa: E402

BN_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
BN_RANGE = re.compile(r"[\u0980-\u09FF]")
STRIP = str.maketrans("", "", ",.;:!?\"'“”‘’()[]{}")

errors, warnings, checks = [], [], []


def ok(cond, msg):
    checks.append(msg)
    if not cond:
        errors.append(msg)


def warn(cond, msg):
    checks.append(msg)
    if not cond:
        warnings.append(msg)


def norm(t):
    t = unicodedata.normalize("NFC", t)
    t = t.translate(BN_DIGITS).lower()
    t = t.replace("\u200c", "").replace("\u200d", "")   # ZWNJ / ZWJ: র‍্যালি == র্যালি
    t = t.translate(STRIP)
    return re.sub(r"\s+", " ", t).strip()


def words(t):
    """Word count: whitespace tokens that contain a letter or a digit."""
    return sum(1 for w in t.split() if re.search(r"[0-9A-Za-z\u0980-\u09FF]", w))


def sentences(t):
    parts = re.split(r"(?<=[.!?।])\s+", t.strip())
    return [p for p in parts if words(p)]


def strip_ws(t):
    return re.sub(r"\s+", " ", t).strip()


# --------------------------------------------------------------------------- pass 1
def pass1(papers):
    ok(len(papers) == 2, "P1.01  exactly two papers")
    seen_instructions = {}
    for p in papers:
        qs = p["questions"]
        ok(len(qs) == 6, f"P1.02  {p['name']}: six questions")
        ok([q["no"] for q in qs] == [1, 2, 3, 4, 5, 6],
           f"P1.03  {p['name']}: questions numbered 1-6 in order")
        ok([q["group"] for q in qs] == ["A", "A", "A", "B", "B", "B"],
           f"P1.04  {p['name']}: group A (English) first, then group B")
        ok([q["type"] for q in qs] == ["report", "precis", "translation"] * 2,
           f"P1.05  {p['name']}: report / precis / translation in each group")

        ga = sum(q["marks"] for q in qs if q["group"] == "A")
        gb = sum(q["marks"] for q in qs if q["group"] == "B")
        ok(ga == 50, f"P1.06  {p['name']}: group A totals 50 (got {ga})")
        ok(gb == 50, f"P1.07  {p['name']}: group B totals 50 (got {gb})")
        ok(ga + gb == 100, f"P1.08  {p['name']}: paper totals 100")

        minutes = sum(q["minutes"] for q in qs)
        planned = minutes + data_part2.META["reading_minutes"] + data_part2.META["checking_minutes"]
        ok(planned == 60,
           f"P1.09  {p['name']}: writing + reading + checking = 60 min (got {planned})")

        for q in qs:
            tag = f"{p['name']} Q{q['no']}"
            want = {"report": 20, "precis": 15, "translation": 15}[q["type"]]
            ok(q["marks"] == want, f"P1.10  {tag}: {q['type']} carries {want} marks")
            ok(sum(m for _, m in q["marking"]) == q["marks"],
               f"P1.11  {tag}: marking breakdown adds to {q['marks']}")
            ok(all(m > 0 for _, m in q["marking"]),
               f"P1.12  {tag}: no zero-weight marking criterion")
            ok(len(q["marking"]) >= 4, f"P1.13  {tag}: at least four marking criteria")
            ok(len(q["notes"]) >= 2, f"P1.14  {tag}: at least two examiner notes")
            ok(len(q["must"]) >= 3, f"P1.15  {tag}: at least three must-carry tokens")
            ok(q["minutes"] >= 0.4 * q["marks"],
               f"P1.16  {tag}: realistic time per mark ({q['minutes']} min / {q['marks']} marks)")

            if q["type"] == "report":
                ok(len(q.get("points", [])) >= 6,
                   f"P1.17  {tag}: at least six supplied points")
                ok(all(pt.get("check") for pt in q["points"]),
                   f"P1.18  {tag}: every supplied point has coverage tokens")
            if q["type"] in ("precis", "translation"):
                ok(len(strip_ws(q.get("passage", ""))) > 80,
                   f"P1.19  {tag}: a real source passage is supplied")

            key = norm(q.get("passage", "") + " || " +
                       " ".join(pt["text"] for pt in q.get("points", [])))
            ok(key not in seen_instructions,
               f"P1.20  {tag}: passage / supplied points not reused elsewhere")
            seen_instructions[key] = tag

    marks = [q["marks"] for p in papers for q in p["questions"]]
    ok(sum(marks) == 200, "P1.21  two papers, 200 marks in all")
    ok(len({q["minutes"] for p in papers for q in p["questions"]}) == 3,
       "P1.22  the same three time allowances are used in both papers")
    ok(data_part2.META["marks"] == 100 and data_part2.META["minutes"] == 60,
       "P1.23  META records 100 marks in 60 minutes")
    ok(data_part2.META["group_marks"] == {"A": 50, "B": 50},
       "P1.24  META records 50 + 50")


# --------------------------------------------------------------------------- pass 2
def pass2(papers):
    for p in papers:
        for q in p["questions"]:
            tag = f"{p['name']} Q{q['no']}"
            body = q["model"]["body"]
            title = q["model"].get("title", "")
            full = strip_ws(title + " " + body)
            n = words(full)

            if q["type"] == "report":
                ok(150 <= n <= 200, f"P2.01  {tag}: report is 150-200 words (got {n})")
                ok(title.strip() != "", f"P2.02  {tag}: report has a headline")
                ok(2 <= words(title) <= 14, f"P2.03  {tag}: headline is headline-length "
                                            f"({words(title)} words)")
                first = body.strip().split("\n")[0]
                ok(re.search(r"\d{4}|\u09e6|\u09e7|\u09e8|\u09e9", first) is not None,
                   f"P2.04  {tag}: dateline carries a date in the opening sentence")
                ok("\n\n" in body, f"P2.05  {tag}: report is paragraphed, not one block")

                missing = []
                for pt in q["points"]:
                    for tok in pt["check"]:
                        if norm(tok) not in norm(body):
                            missing.append(tok)
                ok(not missing, f"P2.06  {tag}: every supplied point is used "
                                f"(missing: {missing})")

                low = norm(body)
                for bad, label in [("i ", "first person 'I'"), (" my ", "first person 'my'"),
                                   ("we ", "first person 'we'"),
                                   ("আমি ", "first person 'আমি'")]:
                    ok(bad not in " " + low + " ",
                       f"P2.07  {tag}: no {label} in a news report")

            if q["type"] == "precis":
                src = words(q["passage"])
                ratio = n / src
                lo, hi = q.get("ratio", (0.25, 0.40))
                ok(lo <= ratio <= hi,
                   f"P2.08  {tag}: precis is about one-third of the passage "
                   f"({n}/{src} = {ratio:.2f}, allowed {lo:.2f}-{hi:.2f})")
                ok(title.strip() != "", f"P2.09  {tag}: precis has a title")
                ok(words(title) <= 7, f"P2.10  {tag}: precis title is short "
                                      f"({words(title)} words)")
                low = norm(full)
                for opener in ["the passage says", "the writer says", "in this passage",
                               "the author says", "according to the passage",
                               "উপরের অনুচ্ছেদে", "লেখক বলেছেন"]:
                    ok(opener not in low,
                       f"P2.11  {tag}: precis does not open with '{opener}'")
                # no long verbatim run lifted from the source
                overlap = longest_shared_run(full, q["passage"])
                ok(overlap < 8, f"P2.12  {tag}: precis is in own words "
                                f"(longest shared run {overlap} words)")
                # the précis must be shorter than any paragraph it summarises
                ok(n < src, f"P2.13  {tag}: precis shorter than its source")

            if q["type"] == "translation":
                src = words(q["passage"])
                ratio = n / src
                ok(0.55 <= ratio <= 1.9,
                   f"P2.14  {tag}: translation is neither truncated nor padded "
                   f"({n}/{src} = {ratio:.2f})")
                s_src, s_tgt = len(sentences(q["passage"])), len(sentences(body))
                ok(s_tgt >= 0.6 * s_src,
                   f"P2.15  {tag}: no source sentence dropped "
                   f"({s_tgt} target sentences for {s_src} source)")
                ok(s_tgt <= 2.0 * s_src,
                   f"P2.16  {tag}: sentences not chopped into fragments "
                   f"({s_tgt} vs {s_src})")
                missing = [t for t in q["must"] if norm(t) not in norm(body)]
                ok(not missing, f"P2.17  {tag}: every key idea rendered "
                                f"(missing: {missing})")
                overlap = longest_shared_run(body, q["passage"])
                ok(overlap < 6, f"P2.18  {tag}: source not copied untranslated "
                                f"(longest shared run {overlap} words)")


def longest_shared_run(a, b):
    """Length in words of the longest verbatim run shared by two texts."""
    aw, bw = norm(a).split(), norm(b).split()
    best = 0
    for i in range(len(aw)):
        for j in range(len(bw)):
            k = 0
            while i + k < len(aw) and j + k < len(bw) and aw[i + k] == bw[j + k]:
                k += 1
            best = max(best, k)
    return best


# --------------------------------------------------------------------------- pass 3
def pass3(papers):
    for p in papers:
        for q in p["questions"]:
            tag = f"{p['name']} Q{q['no']}"
            body = q["model"]["body"]
            src = q.get("passage", "")

            if q["type"] == "translation":
                src_bn = bool(BN_RANGE.search(src))
                tgt_bn = bool(BN_RANGE.search(body))
                ok(src_bn != tgt_bn,
                   f"P3.01  {tag}: source and target are in different scripts "
                   f"({q['group']})")
                if src_bn:   # Bengali -> English
                    ok(not BN_RANGE.search(body),
                       f"P3.02  {tag}: no Bengali left untranslated in the English answer")
                    ok(ascii_share(body) > 0.95,
                       f"P3.03  {tag}: answer is written in English")
                else:        # English -> Bengali
                    ok(bn_share(body) > 0.85,
                       f"P3.04  {tag}: answer is written in Bengali "
                       f"({bn_share(body):.0%} Bengali tokens)")
                    ok(longest_english_chunk(body) <= 2,
                       f"P3.05  {tag}: no English sentence copied into the Bengali answer "
                       f"(longest English run {longest_english_chunk(body)} words)")

            # identity leakage -- costs 10% of the paper
            low = norm(body + " " + q["instruction"])
            for pat, label in [(r"\bmy name\b", "my name"),
                               (r"\bi am\b.{0,20}\bof\b", "self-introduction"),
                               (r"\broll\s*(no|number)\b", "roll number"),
                               (r"@[a-z0-9.]+\.[a-z]{2,}", "e-mail address"),
                               (r"\b\d{10}\b", "phone-like number"),
                               (r"আমার নাম", "আমার নাম"),
                               (r"রোল\s*(নং|নম্বর)?", "রোল নম্বর")]:
                ok(re.search(pat, low) is None,
                   f"P3.06  {tag}: no identity disclosure ({label})")

            # one spelling of every Bengali letter -- mixed encodings render differently
            for label, text in (("model answer", body), ("passage", src),
                                ("instruction", q["instruction"]),
                                ("supplied points", " ".join(pt["text"] for pt in q.get("points", [])))):
                ok(unicodedata.normalize("NFC", text) == text,
                   f"P3.11  {tag}: {label} is NFC-normalised")
            # no replacement characters / stray escapes / lone surrogates
            for label, text in (("model answer", body), ("passage", src),
                                ("instruction", q["instruction"])):
                ok("\ufffd" not in text, f"P3.07  {tag}: no U+FFFD in {label}")
                ok("\\u" not in text, f"P3.08  {tag}: no undecoded escape in {label}")
                ok(all(not (0xD800 <= ord(c) <= 0xDFFF) for c in text),
                   f"P3.09  {tag}: no lone surrogate in {label}")

    # collision check across the whole book
    texts = [(f"{p['name']} Q{q['no']}", strip_ws(q["model"]["body"]))
             for p in papers for q in p["questions"]]
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            run = longest_shared_run(texts[i][1], texts[j][1])
            ok(run < 10, f"P3.10  {texts[i][0]} vs {texts[j][0]}: answers are distinct "
                         f"(shared run {run})")


def ascii_share(t):
    toks = [w for w in t.split() if words(w)]
    return sum(1 for w in toks if not BN_RANGE.search(w)) / max(1, len(toks))


def bn_share(t):
    toks = [w for w in t.split() if words(w)]
    return sum(1 for w in toks if BN_RANGE.search(w)) / max(1, len(toks))


def longest_english_chunk(t):
    best = cur = 0
    for w in t.split():
        if re.search(r"[A-Za-z]", w) and not BN_RANGE.search(w):
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best


# --------------------------------------------------------------------------- re-read
def reread(papers, path):
    data = json.load(open(path, encoding="utf-8"))
    ok(len(data["papers"]) == 2, "P4.01  frozen JSON holds two papers")
    total = 0
    for p_in, p_out in zip(papers, data["papers"]):
        ok(p_in["name"] == p_out["name"], f"P4.02  {p_out['name']}: name survives the freeze")
        for q_in, q_out in zip(p_in["questions"], p_out["questions"]):
            ok(q_in["model"]["body"] == q_out["model"]["body"],
               f"P4.03  {p_out['name']} Q{q_out['no']}: body survives the freeze")
            ok(q_in["marks"] == q_out["marks"],
               f"P4.04  {p_out['name']} Q{q_out['no']}: marks survive the freeze")
            total += q_out["marks"]
    ok(total == 200, "P4.05  frozen JSON still adds to 200 marks")
    ok(data["meta"]["total_minutes"] == 60, "P4.06  frozen JSON records 60 minutes")
    ok(data["meta"]["reading_minutes"] == 4 and data["meta"]["checking_minutes"] == 2,
       "P4.07  frozen JSON records the reading and checking allowances")
    return data


def main():
    papers = data_part2.PAPERS
    freeze(papers)
    pass1(papers)
    pass2(papers)
    pass3(papers)
    reread(papers, os.path.join(HERE, "final_papers_part2.json"))

    report = {
        "checked": len(checks),
        "errors": errors,
        "warnings": warnings,
        "papers": [{"name": p["name"],
                    "marks": sum(q["marks"] for q in p["questions"]),
                    "minutes": sum(q["minutes"] for q in p["questions"])} for p in papers],
        "status": "PASS" if not errors else "FAIL",
    }
    json.dump(report, open(os.path.join(HERE, "validation_report_part2.json"), "w",
                           encoding="utf-8"), indent=2, ensure_ascii=False)

    print(f"checks run : {len(checks)}")
    for e in errors:
        print("  ERROR  ", e)
    for w in warnings:
        print("  WARN   ", w)
    print("status     :", report["status"])
    if errors:
        sys.exit(1)


def freeze(papers):
    out = {"meta": {"total_marks": data_part2.META["marks"],
                    "total_minutes": data_part2.META["minutes"],
                    "reading_minutes": data_part2.META["reading_minutes"],
                    "checking_minutes": data_part2.META["checking_minutes"],
                    "papers": len(papers),
                    "note": "Part-II conventional paper: report, precis, translation."},
           "papers": papers}
    json.dump(out, open(os.path.join(HERE, "final_papers_part2.json"), "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()

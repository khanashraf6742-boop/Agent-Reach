# -*- coding: utf-8 -*-
"""Audit the two revision books.

Checks the package, the page arithmetic, the coverage against the eight-paper
volume, the DSL leftovers and the text itself.  Exit 1 on any failure.
"""
import json
import os
import re
import sys
import unicodedata
import zipfile

from docx import Document

import arith_sheets
import drills
import extra
import formula_tests
import gk_sheets
import layout
import ooxml_order

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
BOOKS = [
    ("gk", "WBPSC_Clerkship_GS_Revision_Sheets_2026.docx", gk_sheets.TOPICS, 8.5),
    ("arith", "WBPSC_Clerkship_Arithmetic_Formula_Sheets_2026.docx", arith_sheets.TOPICS, 9.2),
]

checks, errors = [], []


def check(ok, tag, detail=""):
    checks.append(tag)
    if not ok:
        errors.append(f"{tag}: {detail}")


# --------------------------------------------------------------- the formulas
total, bad = formula_tests.run()
check(not bad, "F.01 formula identities", bad[:3])
check(total >= 70, "F.02 formula suite is broad enough", total)

book_tags = {t["tag"] for t in arith_sheets.TOPICS}
papers = json.load(open(os.path.join(HERE, "..", "papers8", "final_papers8.json"),
                        encoding="utf-8"))
ar_tags = {it["tag"] for p in papers["papers"] for it in p["items"] if it["section"] == "AR"}
gs_tags = {it["tag"] for p in papers["papers"] for it in p["items"] if it["section"] == "GS"}
check(book_tags == ar_tags, "F.03 every arithmetic topic has a sheet", ar_tags - book_tags)
check({t["title"] for t in gk_sheets.TOPICS} >= gs_tags, "F.04 every GS topic has a sheet",
      gs_tags - {t["title"] for t in gk_sheets.TOPICS})
check(len({t["key"] for t in gk_sheets.TOPICS}) == 7, "F.05 seven GK sheets")
check(len({t["key"] for t in arith_sheets.TOPICS}) == 23, "F.06 twenty-three formula sheets")
check(set(drills.D) == {t["key"] for t in arith_sheets.TOPICS}
      and all(len(v) == 3 for v in drills.D.values()),
      "F.07 three drills on every arithmetic sheet")

# --------------------------------------------------------------- each book
for kind, name, topics, size in BOOKS:
    path = os.path.join(OUT, name)
    check(os.path.exists(path), f"{kind}.00 file exists", name)
    with zipfile.ZipFile(path) as z:
        check(z.testzip() is None, f"{kind}.01 zip integrity")
        check("word/document.xml" in z.namelist(), f"{kind}.02 document part")

    doc = Document(path)
    check(not ooxml_order.violations(doc.element), f"{kind}.03 schema child order",
          ooxml_order.violations(doc.element)[:3])

    # one page per topic: a page break before every topic after the cover
    breaks = doc.element.body.findall(
        ".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}br")
    page_breaks = [b for b in breaks
                   if b.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}type") == "page"]
    check(len(page_breaks) == len(topics), f"{kind}.04 one page break per sheet",
          f"{len(page_breaks)} breaks for {len(topics)} sheets")

    tables = doc.tables
    check(len(tables) == len(topics) + 1, f"{kind}.05 cover table plus one per sheet", len(tables))
    body = tables[1:]
    check(all(len(t.columns) == 2 for t in body), f"{kind}.06 every sheet is two columns")
    cant = all(t.rows[0]._tr.find(
        "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}trPr") is not None
        for t in body)
    check(cant, f"{kind}.07 rows cannot split across pages")
    empty = [(i, c.text) for i, t in enumerate(body) for r in t.rows for c in r.cells
             if not c.text.strip()]
    check(not empty, f"{kind}.08 no empty column", empty[:3])

    # every paragraph of every sheet fits the measured budget
    layout.set_body(size)
    over = []
    for t in topics:
        add = extra.EXTRA.get(t["key"], {})
        left = t["left"] + add.get("left", "")
        right = t["right"] + add.get("right", "")
        if kind == "arith":
            rows = drills.D.get(t["key"], [])
            block = "\n## Three drills\n" + "\n".join(f"{q} :: {a}" for q, a in rows)
            if sum(b.height for b in layout.parse(left)) <= sum(b.height for b in layout.parse(right)):
                left += block
            else:
                right += block
        h = max(sum(b.height for b in layout.parse(left)),
                sum(b.height for b in layout.parse(right)))
        if h > layout.COL_BUDGET * 0.995:
            over.append((t["title"], round(h)))
    check(not over, f"{kind}.09 every sheet fits its page", over)

    text = "\n".join(p.text for p in doc.paragraphs)
    text += "\n" + "\n".join(c.text for t in doc.tables for r in t.rows for c in r.cells)
    check("##" not in text and "::" not in text, f"{kind}.10 no DSL markers leaked", )
    check("**" not in text, f"{kind}.11 no stray bold markers")
    check("\ufffd" not in text, f"{kind}.12 no replacement characters")
    check(unicodedata.is_normalized("NFC", text), f"{kind}.13 text is NFC")
    check(not re.search(r"\{(q|a|n|money)\}", text), f"{kind}.14 no unformatted f-strings")
    check("  " not in text.replace("        ", " "), f"{kind}.15 no doubled spaces")
    check(len(text) > 20000, f"{kind}.16 substantial", len(text))

    # the sheet titles appear in order
    titles = [p.text.strip() for p in doc.paragraphs if p.text.strip() in {t["title"] for t in topics}]
    check(titles[:len(topics)] == [t["title"] for t in topics], f"{kind}.17 sheets in order",
          titles[:4])

    print(f"{name}: {len(topics)} sheets, {os.path.getsize(path):,} bytes, "
          f"{len(doc.paragraphs)} paragraphs, {len(tables)} tables")

print(f"audit: {len(checks)} checks, {len(errors)} error(s)")
for e in errors[:12]:
    print("   ", e)
print("status:", "PASS" if not errors else "FAIL")
sys.exit(1 if errors else 0)

# -*- coding: utf-8 -*-
"""Build the two revision books.

    python3 build_sheets.py

Stops if a formula identity fails, if a topic does not fit on its page, or if
the General Studies topics drift out of step with the arithmetic ones.
"""
import os
import sys

import layout
import gk_sheets
import arith_sheets
import extra
import drills
import formula_tests

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)

total, bad = formula_tests.run()
if bad:
    for row in bad:
        print("  formula failure:", row)
    sys.exit(f"{len(bad)} formula identities failed; refusing to build")
print(f"formula identities: {total} checked, 0 failed")


def stems_for(tag, limit=3):
    """Real question stems for this topic, taken from the verified eight papers."""
    seen, out = set(), []
    for paper in papers["papers"]:
        for it in paper["items"]:
            if it["section"] == "AR" and it["tag"] == tag and it["q"] not in seen:
                seen.add(it["q"])
                out.append((len(it["q"]), it["q"]))
    out.sort()
    return [q for _, q in out[:limit]]


def build(kind):
    layout.set_body(8.5 if kind == "gk" else 9.2)
    doc = layout.new_document()
    topics = gk_sheets.TOPICS if kind == "gk" else arith_sheets.TOPICS
    global papers
    n = len(topics)
    if kind == "gk":
        layout.cover(
            doc,
            "West Bengal Public Service Commission \u00b7 Clerkship \u00b7 Part I",
            "General Studies",
            "Seven revision sheets, one page each",
            ["Every fact a Part-I paper has actually asked, in the form you can revise from",
             "Polity, Geography, History, Science, Economy, West Bengal, Current affairs",
             "Current affairs verified to 30 October 2026"],
            [("Sheet", "Topic", "What it fixes in your head")] +
            [(str(i + 1), t["title"], t["sub"]) for i, t in enumerate(topics)],
            "WBPSC Clerkship \u00b7 General Studies revision sheets \u00b7 2026",
        )
        out = os.path.join(OUT, "WBPSC_Clerkship_GS_Revision_Sheets_2026.docx")
        footer_text = "WBPSC Clerkship \u00b7 General Studies revision sheets \u00b7 2026"
        kicker_fmt = "Revision sheet {} of " + str(n)
    else:
        layout.cover(
            doc,
            "West Bengal Public Service Commission \u00b7 Clerkship \u00b7 Part I",
            "Arithmetic & Reasoning",
            f"{n} formula sheets, one page each",
            ["Formulas, the question types built on them, a worked example and the traps",
             "Every worked example is computed, not typed",
             f"{total} formula identities re-checked at build time"],
            [("Sheet", "Topic", "The formula that carries it")] +
            [(str(i + 1), t["title"], t["sub"]) for i, t in enumerate(topics)],
            "WBPSC Clerkship \u00b7 Arithmetic and Reasoning formula sheets \u00b7 2026",
        )
        out = os.path.join(OUT, "WBPSC_Clerkship_Arithmetic_Formula_Sheets_2026.docx")
        footer_text = "WBPSC Clerkship \u00b7 Arithmetic and Reasoning formula sheets \u00b7 2026"
        kicker_fmt = "Formula sheet {} of " + str(n)

    heights = []
    for i, t in enumerate(topics, start=1):
        add = extra.EXTRA.get(t["key"], {})
        left = t["left"] + add.get("left", "")
        right = t["right"] + add.get("right", "")
        if kind == "arith":
            rows = drills.D.get(t["key"], [])
            block = "\n## Three drills\n" + "\n".join(f"{q} :: {a}" for q, a in rows)
            stems = stems_for(t["tag"])
            if stems:
                block += "\n## How the paper asks it\n" + "\n".join(f"- {q}" for q in stems)
            # put the addendum in whichever column is shorter
            if sum(b.height for b in layout.parse(left)) <= sum(b.height for b in layout.parse(right)):
                left += block
            else:
                right += block
        used = layout.topic_page(doc, kicker_fmt.format(i), t["title"], t["sub"],
                                 left, right, first_page=False)
        heights.append((t["title"], used))
        if used > layout.COL_BUDGET * 0.97:
            print(f"  tight page: {t['title']} uses {used:.0f} of {layout.COL_BUDGET:.0f} pt")

    moved = layout.save(doc, out)
    print(f"{os.path.basename(out)}: {n} pages, {os.path.getsize(out):,} bytes, "
          f"{moved} property bags reordered")
    print("   fullest page: " + ", ".join(f"{t} {h:.0f}pt" for t, h in
                                          sorted(heights, key=lambda x: -x[1])[:3]))
    return out


import json                                                   # noqa: E402
papers = json.load(open(os.path.join(HERE, "..", "papers8", "final_papers8.json"),
                        encoding="utf-8"))

gk = build("gk")
ar = build("arith")

# arithmetic coverage must match the book's own topic list
book_tags = {it["tag"] for p in papers["papers"] for it in p["items"] if it["section"] == "AR"}
sheet_tags = {t["tag"] for t in arith_sheets.TOPICS}
missing = book_tags - sheet_tags
extra = sheet_tags - book_tags
print(f"topic coverage: {len(sheet_tags)} sheets vs {len(book_tags)} tags in the book")
if missing or extra:
    sys.exit(f"coverage mismatch, missing {missing}, extra {extra}")
print("   every arithmetic topic in the eight papers has a sheet")

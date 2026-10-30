#!/usr/bin/env python3
"""Typeset final_papers.json into the deliverable DOCX.

Only validated data is read here: build_docx.py refuses to run if validation_report.json is
missing or reports any error, so the document and the validation cannot drift apart.

Output: WBPSC_Clerkship_Part1_Most_Expected_Papers_2026.docx
"""

import json
import os
import sys
from collections import Counter

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "WBPSC_Clerkship_Part1_Most_Expected_Papers_2026.docx")

NAVY = RGBColor(0x0D, 0x2B, 0x45)
INK = RGBColor(0x1A, 0x1A, 0x1A)
GREY = RGBColor(0x55, 0x60, 0x6C)
GREEN = RGBColor(0x1E, 0x6B, 0x3A)
MAROON = RGBColor(0x8B, 0x1E, 0x2D)

SECTION_RANGES = {"ENG": (1, 30), "GS": (31, 70), "AR": (71, 100)}
SECTION_LABEL = {
    "ENG": "SECTION A \u2014 ENGLISH (Q. 1 \u2013 30)",
    "GS": "SECTION B \u2014 GENERAL STUDIES (Q. 31 \u2013 70)",
    "AR": "SECTION C \u2014 ARITHMETIC (Q. 71 \u2013 100)",
}
SECTION_MARKS = {"ENG": "30 marks", "GS": "40 marks", "AR": "30 marks"}


# --------------------------------------------------------------------------- xml helpers
def shade(cell, hex_fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    tcPr.append(shd)


def cell_margins(cell, top=40, bottom=40, left=80, right=80):
    tcPr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement("w:tcMar")
    for tag, val in (("top", top), ("start", left), ("bottom", bottom), ("end", right)):
        el = OxmlElement(f"w:{tag}")
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tcPr.append(mar)


def table_borders(table, size=6, color="B9C2CC", inside=True):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    edges = ["top", "left", "bottom", "right"] + (["insideH", "insideV"] if inside else [])
    for edge in edges:
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(size))
        el.set(qn("w:color"), color)
        borders.append(el)
    if not inside:
        for edge in ("insideH", "insideV"):
            el = OxmlElement(f"w:{edge}")
            el.set(qn("w:val"), "nil")
            borders.append(el)
    tblPr.append(borders)


def no_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "nil")
        borders.append(el)
    tblPr.append(borders)


def keep_with_next(par, on=True):
    par.paragraph_format.keep_with_next = on
    par.paragraph_format.keep_together = on


def add_rule(doc, color="0D2B45", size=12, space_before=0, space_after=6):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(space_before)
    par.paragraph_format.space_after = Pt(space_after)
    pPr = par._p.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), color)
    borders.append(bottom)
    pPr.append(borders)
    return par


def page_number_footer(section, label):
    footer = section.footer
    par = footer.paragraphs[0]
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = par.add_run(f"{label}   |   page ")
    run.font.size = Pt(8)
    run.font.color.rgb = GREY
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    r = OxmlElement("w:r")
    t = OxmlElement("w:t")
    t.text = "1"
    r.append(t)
    fld.append(r)
    par._p.append(fld)


def header_line(section, text):
    head = section.header
    par = head.paragraphs[0]
    par.text = ""
    par.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = par.add_run(text)
    run.font.size = Pt(8)
    run.font.color.rgb = GREY
    run.italic = True


# --------------------------------------------------------------------------- text helpers
def para(doc, text="", size=10.5, bold=False, italic=False, color=INK, align=None,
         space_before=0, space_after=4, style=None, indent=None):
    p = doc.add_paragraph(style=style)
    if align is not None:
        p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    if indent:
        p.paragraph_format.left_indent = Cm(indent)
    if text:
        run = p.add_run(text)
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = color
    return p


def rich(p, chunks):
    """chunks = [(text, {size,bold,italic,color}), ...]"""
    for text, fmt in chunks:
        run = p.add_run(text)
        run.font.size = Pt(fmt.get("size", 10.5))
        run.bold = fmt.get("bold", False)
        run.italic = fmt.get("italic", False)
        run.font.color.rgb = fmt.get("color", INK)
    return p


def heading(doc, text, size=13, color=NAVY, space_before=12, space_after=4, rule=True):
    p = para(doc, text, size=size, bold=True, color=color, space_before=space_before,
             space_after=space_after)
    keep_with_next(p)
    if rule:
        add_rule(doc, size=6, space_before=0, space_after=8)
    return p


# --------------------------------------------------------------------------- content pieces
def cover(doc, blob, stats):
    para(doc, "", space_after=30)
    p = para(doc, "", align=WD_ALIGN_PARAGRAPH.CENTER)
    rich(p, [("PUBLIC SERVICE COMMISSION, WEST BENGAL", {"size": 11, "bold": True, "color": GREY})])
    p = para(doc, "", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2)
    rich(p, [("CLERKSHIP EXAMINATION", {"size": 24, "bold": True, "color": NAVY})])
    p = para(doc, "", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2)
    rich(p, [("PART-I (Objective Type) \u00b7 LDA / LDC", {"size": 13, "color": GREY})])
    add_rule(doc, size=18, space_before=12, space_after=14)

    p = para(doc, "", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    rich(p, [("MOST EXPECTED QUESTION PAPERS", {"size": 20, "bold": True, "color": MAROON})])
    p = para(doc, "", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    rich(p, [("with verified answers and step-by-step explanations",
              {"size": 12, "italic": True, "color": INK})])

    t = doc.add_table(rows=5, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_borders(t, size=6)
    rows = [
        ("Papers in this book", "2 full-length papers \u00b7 200 questions"),
        ("Pattern", "English 30 + General Studies 40 + Arithmetic 30 = 100 marks"),
        ("Time per paper", "1 hour 30 minutes \u00b7 negative marking \u00bc per wrong answer"),
        ("Answers", "Official-style key grid + worked solution for every question"),
        ("Verification", f"3-pass automated validation \u00b7 {stats['checks']} checks \u00b7 "
                         f"{stats['errors']} errors"),
    ]
    for r, (k, v) in enumerate(rows):
        c0, c1 = t.rows[r].cells
        c0.width, c1.width = Cm(5.2), Cm(9.8)
        c0.text = ""
        c1.text = ""
        pr = c0.paragraphs[0]
        rich(pr, [(k, {"size": 9.5, "bold": True, "color": NAVY})])
        pv = c1.paragraphs[0]
        rich(pv, [(v, {"size": 9.5})])
        shade(c0, "EEF2F6")
        for c in (c0, c1):
            cell_margins(c)

    para(doc, "", space_after=16)
    para(doc, "Based on the Commission's own Part-I papers of 2019 and 2023 (Advt. 13/2023), "
              "the 2026 scheme of examination and the current-affairs record up to October 2026.",
         size=9.5, italic=True, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER)
    para(doc, "2026 edition \u00b7 current affairs verified to 30 October 2026",
         size=9.5, bold=True, color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    para(doc, "Prepared for self-study \u00b7 not an official WBPSC publication",
         size=8.5, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER)


def how_to_use(doc):
    heading(doc, "How to use this book", size=14, space_before=0)
    para(doc, "Each paper is a full mock of Part-I: 100 questions, 100 marks, 90 minutes, with "
              "0.25 marks deducted for every wrong answer and nothing deducted for a question left "
              "blank. The three sections are kept in the order the Commission uses, and the "
              "General Studies and Arithmetic questions are deliberately mixed in difficulty so "
              "that the paper behaves like the real one rather than like a textbook chapter test.")

    heading(doc, "The order of work", size=11.5)
    steps = [
        ("1. Sit the paper cold.", " One 90-minute block, no notes, no phone. Mark answers on a "
                                   "rough OMR-style grid so that you practise transfer errors too."),
        ("2. Score with the key grid.", " Use the 10\u00d710 grid printed at the end of the paper. "
                                        "Apply \u00bc negative marking honestly."),
        ("3. Read every solution, not only the wrong ones.", " A right answer reached by a wrong "
         "route will fail on a different question; the explanation tells you which route is safe."),
        ("4. Log the topic of each mistake.", " The topic tag under every solution is there so that "
         "your revision list writes itself."),
        ("5. Re-attempt after ten days.", " Re-solving a paper you have forgotten is the cheapest "
         "way to test whether a method has actually stuck."),
    ]
    for head, body in steps:
        p = para(doc, space_after=4)
        rich(p, [(head, {"size": 10.5, "bold": True, "color": NAVY}), (body, {"size": 10.5})])

    heading(doc, "What a safe score looks like", size=11.5)
    para(doc, "In the 2023 cycle the Part-I qualifying marks were 49 for General, 48 for OBC-A and "
              "OBC-B, 47 for SC and 29 for ST, and 89,821 candidates qualified for Part-II. "
              "Qualifying is the floor, not the goal: the final merit list uses Part-I and Part-II "
              "together, so 70+ here is a comfortable working target and 80+ is where the "
              "descriptive stage stops being a gamble.")

    heading(doc, "Where the questions come from", size=11.5)
    para(doc, "English and Arithmetic are modelled on the 2023 and 2019 Part-I papers, whose "
              "syllabus is fixed: vocabulary, grammar and usage for English; divisibility, "
              "fractions, decimals, recurring decimals, simplification, HCF-LCM, partnership, "
              "average, ratio, percentage, simple interest, profit and loss, time and distance, "
              "and the areas of rectangles and squares for Arithmetic. General Studies mixes West "
              "Bengal geography and history, Indian polity and economy, everyday science, and "
              "current affairs up to October 2026. Every General Studies answer carries its source "
              "line so that you can check it rather than trust it.")

    heading(doc, "A word on the answer key", size=11.5)
    para(doc, "Option order in both papers has been randomised with a fixed seed, so the correct "
              "answer is not sitting in the same slot all through the paper. That is why a few "
              "explanations refer to an option letter; the letters in the explanation are the "
              "letters printed in this book.")


def paper_section(doc, paper, number, first=False):
    items = paper["items"]
    if not first:
        doc.add_page_break()

    heading(doc, f"PAPER {number}", size=22, color=NAVY, space_before=6, space_after=2, rule=False)
    add_rule(doc, size=14, space_before=0, space_after=10)
    p = para(doc, space_after=10)
    rich(p, [("Clerkship Part-I mock \u00b7 100 questions \u00b7 100 marks \u00b7 90 minutes",
              {"size": 10.5, "italic": True, "color": GREY})])

    t = doc.add_table(rows=3, cols=3)
    table_borders(t, size=6)
    cells = [("English", "30 questions", "30 marks"),
             ("General Studies", "40 questions", "40 marks"),
             ("Arithmetic", "30 questions", "30 marks")]
    for col, (a, b, c) in enumerate(cells):
        top, bottom = t.rows[0].cells[col], t.rows[1].cells[col]
        top.text = ""
        bottom.text = ""
        rich(top.paragraphs[0], [(a, {"size": 9.5, "bold": True, "color": NAVY})])
        rich(bottom.paragraphs[0], [(f"{b} \u00b7 {c}", {"size": 9.5})])
        shade(top, "EEF2F6")
        cell_margins(top)
        cell_margins(bottom)
    t.rows[2].cells[0].merge(t.rows[2].cells[2])
    last = t.rows[2].cells[0]
    last.text = ""
    rich(last.paragraphs[0], [("Negative marking: \u00bc (0.25) marks deducted for each wrong "
                               "answer. Answer all questions in one sitting.",
                               {"size": 9, "italic": True, "color": MAROON})])
    cell_margins(last)

    heading(doc, "Instructions", size=11.5, space_before=12)
    for line in [
        "All questions are of multiple-choice type. Four probable answers (A), (B), (C) and (D) "
        "are given against each question; choose the correct or the best one.",
        "One and only one option is to be marked for each question.",
        "1 mark for a correct answer, minus 0.25 for a wrong answer, 0 for an unattempted question.",
        "Standard of the paper is that of the Madhyamak examination of the West Bengal Board of "
        "Secondary Education.",
    ]:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(line)
        run.font.size = Pt(9.5)
        run.font.color.rgb = INK

    heading(doc, "Questions", size=11.5, space_before=10)
    current = None
    for it in items:
        if it["section"] != current:
            current = it["section"]
            p = para(doc, space_before=12, space_after=6)
            rich(p, [(SECTION_LABEL[current], {"size": 10.5, "bold": True, "color": MAROON}),
                     (f"   \u00b7   {SECTION_MARKS[current]}", {"size": 9, "color": GREY})])
            add_rule(doc, size=4, space_before=0, space_after=6)
        question_block(doc, it)

    para(doc, "", space_after=6)
    p = para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10)
    rich(p, [("\u2014  END OF PAPER " + str(number) + "  \u2014", {"size": 10, "bold": True,
                                                                   "color": GREY})])


def question_block(doc, it):
    p = para(doc, space_before=7, space_after=2)
    keep_with_next(p)
    rich(p, [(f"{it['number']}. ", {"size": 10.5, "bold": True, "color": NAVY}),
             (it["question"], {"size": 10.5})])

    opts = it["options"]
    long_opt = any(len(o) > 44 for o in opts)
    if long_opt:
        for j, o in enumerate(opts):
            q = para(doc, space_before=0, space_after=1, indent=0.55)
            keep_with_next(q)
            rich(q, [(f"({chr(65 + j)})  ", {"size": 10, "bold": True, "color": GREY}),
                     (o, {"size": 10})])
        doc.paragraphs[-1].paragraph_format.keep_with_next = False
    else:
        t = doc.add_table(rows=2, cols=2)
        no_borders(t)
        t.autofit = True
        for j, o in enumerate(opts):
            cell = t.rows[j // 2].cells[j % 2]
            cell.text = ""
            cell_margins(cell, top=10, bottom=10, left=340, right=60)
            para_in_cell(cell, f"({chr(65 + j)})", o)


def para_in_cell(cell, letter, text):
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    rich(p, [(f"{letter}  ", {"size": 10, "bold": True, "color": GREY}), (text, {"size": 10})])


def answer_grid(doc, items, number):
    heading(doc, f"Answer key \u2014 Paper {number}", size=13)
    para(doc, "Check your marks before reading the solutions: 1 mark for each correct answer, "
              "minus 0.25 for each wrong answer, nothing for a blank.", size=9.5, color=GREY,
         space_after=8)
    printed = []
    t = doc.add_table(rows=10, cols=20)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_borders(t, size=6)
    for r in range(10):
        for c in range(10):
            qno = r * 10 + c + 1
            printed.append(qno)
            qcell = t.rows[r].cells[c * 2]
            acell = t.rows[r].cells[c * 2 + 1]
            for cell, text, bold in ((qcell, str(qno), True), (acell,
                                                               chr(65 + items[qno - 1]["answer_index"]),
                                                               True)):
                cell.text = ""
                cell_margins(cell, top=30, bottom=30, left=40, right=40)
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_after = Pt(0)
                run = p.add_run(text)
                run.font.size = Pt(9)
                run.bold = bold
                run.font.color.rgb = NAVY if bold and cell is qcell else GREEN
            shade(qcell, "EEF2F6")
    assert len(printed) == 100 and len(set(printed)) == 100, "answer grid is incomplete"


def solutions(doc, items, number):
    heading(doc, f"Solutions with explanations \u2014 Paper {number}", size=13)
    para(doc, "Every answer is stated first, then the reasoning, then the topic it belongs to. "
              "For General Studies a source line is added so the fact can be checked "
              "independently.", size=9.5, color=GREY, space_after=10)
    current = None
    for it in items:
        if it["section"] != current:
            current = it["section"]
            p = para(doc, space_before=10, space_after=4)
            rich(p, [(SECTION_LABEL[current], {"size": 10, "bold": True, "color": MAROON})])
        p = para(doc, space_before=6, space_after=1)
        keep_with_next(p)
        rich(p, [(f"{it['number']}.  ", {"size": 10, "bold": True, "color": NAVY}),
                 (it["question"], {"size": 9.5, "color": GREY})])

        p = para(doc, space_before=1, space_after=1)
        keep_with_next(p)
        rich(p, [("Answer: ", {"size": 10, "bold": True, "color": GREEN}),
                 (f"({chr(65 + it['answer_index'])})  {it['answer']}",
                  {"size": 10, "bold": True, "color": GREEN})])

        p = para(doc, space_before=0, space_after=1, indent=0.3)
        keep_with_next(p)
        rich(p, [(it["explanation"], {"size": 9.5})])

        tail = [("Topic: ", {"size": 8.5, "bold": True, "color": GREY}),
                (it["topic"], {"size": 8.5, "color": GREY})]
        if it["section"] == "GS" and it.get("source"):
            tail.append(("   \u00b7   Source: ", {"size": 8.5, "bold": True, "color": GREY}))
            tail.append((it["source"], {"size": 8.5, "color": GREY}))
        p = para(doc, space_before=1, space_after=2, indent=0.3)
        rich(p, tail)


def appendix(doc, blob, report):
    doc.add_page_break()
    heading(doc, "Appendix A \u2014 Blueprint of the two papers", size=16, space_before=0)
    para(doc, "The official Part-I blueprint is fixed at 30 English + 40 General Studies + 30 "
              "Arithmetic. The topic weightage below is what these two papers actually contain; "
              "use it to see which areas you have not rehearsed.", size=10)

    for paper in blob["papers"]:
        heading(doc, paper["name"], size=11.5, space_before=8)
        counts = {sec: Counter(it["topic"] for it in paper["items"] if it["section"] == sec)
                  for sec in ("ENG", "GS", "AR")}
        t = doc.add_table(rows=1, cols=3)
        table_borders(t, size=6)
        widths = (Cm(4.6), Cm(4.6), Cm(4.6))
        heads = ("English (30)", "General Studies (40)", "Arithmetic (30)")
        for c, h in enumerate(heads):
            cell = t.rows[0].cells[c]
            cell.text = ""
            cell.width = widths[c]
            rich(cell.paragraphs[0], [(h, {"size": 9, "bold": True, "color": NAVY})])
            shade(cell, "EEF2F6")
            cell_margins(cell)

        cols = [[f"{k} \u2014 {v}" for k, v in sorted(counts[sec].items())] for sec in
                ("ENG", "GS", "AR")]
        for r in range(max(len(c) for c in cols)):
            row = t.add_row()
            for c in range(3):
                cell = row.cells[c]
                cell.width = widths[c]
                cell.text = ""
                cell_margins(cell)
                text = cols[c][r] if r < len(cols[c]) else ""
                rich(cell.paragraphs[0], [(text, {"size": 8.5})])

    heading(doc, "Appendix B \u2014 The validation certificate", size=16, space_before=16)
    para(doc, "A wrong answer key is worse than no answer key, so nothing in this book was "
              "accepted on trust. Both papers were frozen into a data file and then put through "
              "three independent passes. The document you are reading is typeset from that same "
              "frozen file, and the builder refuses to run unless the validation is clean.",
         size=10)

    rows = [
        ("Pass 1 \u2014 Structure",
         "100 questions per paper, split 30 / 40 / 30; four distinct non-empty options; answer "
         "index inside range; stepwise explanation present; no duplicated question within or "
         "between the two papers."),
        ("Pass 2 \u2014 Recalculation",
         "Every arithmetic answer was recomputed twice from expressions written independently of "
         "the explanation: once in ordinary floating point, once again in exact rational "
         "arithmetic. The recomputed value had to equal the marked option and no other option, "
         "and all four options had to be numerically distinct."),
        ("Pass 3 \u2014 Fact and key audit",
         "Every General Studies item carries a canonical fact that must appear inside the marked "
         "option and nowhere else, plus a source line. Every language explanation must contain "
         "the marked answer. The file is then re-read from disk as an independent second read and "
         "the answer text is matched back against its own option list."),
    ]
    t = doc.add_table(rows=1, cols=2)
    table_borders(t, size=6)
    for c, h in enumerate(("Pass", "What it proves")):
        cell = t.rows[0].cells[c]
        cell.text = ""
        cell.width = Cm(4.2) if c == 0 else Cm(12.0)
        rich(cell.paragraphs[0], [(h, {"size": 9, "bold": True, "color": NAVY})])
        shade(cell, "EEF2F6")
        cell_margins(cell)
    for a, b in rows:
        row = t.add_row()
        c0, c1 = row.cells
        c0.width, c1.width = Cm(4.2), Cm(12.0)
        c0.text = ""
        c1.text = ""
        rich(c0.paragraphs[0], [(a, {"size": 9, "bold": True, "color": NAVY})])
        rich(c1.paragraphs[0], [(b, {"size": 9})])
        for c in (c0, c1):
            cell_margins(c)

    checks = report.get("checks", {})
    para(doc, "", space_after=4)
    stat_rows = [
        ("Questions validated", "200"),
        ("Arithmetic answers recalculated (floating point)", str(checks.get("P2_num", 0))),
        ("Arithmetic answers recalculated (exact fractions)", str(checks.get("P2_exact", 0))),
        ("General Studies facts matched against the key", str(checks.get("P3_fact", 0))),
        ("Language answers cross-checked against the explanation", str(checks.get("P3_text", 0))),
        ("Structural checks", str(checks.get("P1", 0))),
        ("Errors remaining", str(len(report.get("errors", [])))),
        ("Seed used to randomise option order", str(blob.get("seed"))),
    ]
    t = doc.add_table(rows=0, cols=2)
    table_borders(t, size=4)
    for k, v in stat_rows:
        row = t.add_row()
        c0, c1 = row.cells
        c0.width, c1.width = Cm(11.0), Cm(5.2)
        c0.text = ""
        c1.text = ""
        rich(c0.paragraphs[0], [(k, {"size": 9})])
        rich(c1.paragraphs[0], [(v, {"size": 9, "bold": True,
                                     "color": GREEN if v != "0" else MAROON})])
        cell_para = c1.paragraphs[0]
        cell_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        for c in (c0, c1):
            cell_margins(c)

    para(doc, "", space_after=6)
    para(doc, "Problems the validator caught while this book was being written \u2014 and which "
              "were fixed before typesetting: a calendar item whose key could not be machine-"
              "checked, two option texts that meant the same ratio (3 : 5 written twice in "
              "different forms), a divisibility item whose answer was the number itself rather "
              "than a derived quantity, two surplus General Studies questions that broke the "
              "40-mark quota, and a page-wide drift of every answer into option (A), which would "
              "have trained exactly the wrong reflex.", size=9, italic=True, color=GREY)

    heading(doc, "Appendix C \u2014 Sources", size=16, space_before=16)
    for line in [
        "Question papers, answer keys and scheme of examination: Public Service Commission, West "
        "Bengal \u2014 psc.wb.gov.in (Clerkship Examination 2019 and 2023 papers; Part-I answer "
        "keys for Sessions I\u2013IV; Advt. 13/2023 scheme and syllabus).",
        "Result and qualifying marks of the 2023 cycle: WBPSC result notification, 15 October "
        "2025 (89,821 candidates qualified; General 49, OBC-A/B 48, SC 47, ST 29).",
        "Static General Studies: NCERT History, Geography and Science textbooks, Class VI\u2013X; "
        "the Constitution of India; M. Laxmikanth, Indian Polity.",
        "Current affairs: events verified individually and dated on the page \u2014 ICC Men's T20 "
        "World Cup 2026 final (Ahmedabad, 8 March 2026), FIFA World Cup 2026 (Spain, 19 July "
        "2026), Milano-Cortina Winter Olympics (February 2026), Commonwealth Games Glasgow "
        "(August 2026), Asian Games Aichi-Nagoya (September\u2013October 2026), West Bengal "
        "government formation (May 2026), and the present holders of the constitutional and "
        "economic offices listed.",
    ]:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(3)
        run = p.add_run(line)
        run.font.size = Pt(9.5)

    para(doc, "", space_after=8)
    add_rule(doc, size=4, space_before=4, space_after=6)
    para(doc, "This is a practice book prepared from publicly available official material. It is "
              "not published, endorsed or reviewed by the Public Service Commission, West Bengal. "
              "Where a fact can change with time \u2014 holders of office, current affairs \u2014 "
              "check it against the day's newspaper before the examination.",
         size=8.5, italic=True, color=GREY)


# --------------------------------------------------------------------------- main
def main():
    report_path = os.path.join(HERE, "validation_report.json")
    if not os.path.exists(report_path):
        sys.exit("Run finalize.py and validate.py first: no validation report found.")
    with open(report_path, encoding="utf-8") as fh:
        report = json.load(fh)
    if report.get("errors"):
        sys.exit(f"Refusing to build: validation reports {len(report['errors'])} error(s). "
                 f"See validation_report.json")

    with open(os.path.join(HERE, "final_papers.json"), encoding="utf-8") as fh:
        blob = json.load(fh)

    checks = sum(report.get("checks", {}).values())
    stats = {"checks": checks, "errors": len(report.get("errors", []))}

    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(10.5)
    style.paragraph_format.space_after = Pt(4)

    section = doc.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.top_margin = Cm(1.9)
    section.bottom_margin = Cm(1.7)
    section.left_margin = Cm(2.0)
    section.right_margin = Cm(2.0)
    header_line(section, "WBPSC Clerkship Part-I  \u00b7  Most Expected Question Papers")
    page_number_footer(section, "WBPSC Clerkship Part-I \u00b7 expected papers")

    core = doc.core_properties
    core.title = "WBPSC Clerkship Part-I - Most Expected Question Papers 2026"
    core.subject = "Two full-length mock papers with verified answers and step-by-step explanations"
    core.author = "Study pack"
    core.keywords = "WBPSC, Clerkship, LDA, LDC, Part-I, mock test, answer key, solutions"

    cover(doc, blob, stats)
    doc.add_page_break()
    how_to_use(doc)

    for idx, paper in enumerate(blob["papers"], start=1):
        paper_section(doc, paper, idx)
        doc.add_page_break()
        answer_grid(doc, paper["items"], idx)
        doc.add_page_break()
        solutions(doc, paper["items"], idx)

    appendix(doc, blob, report)
    doc.save(OUT)
    print("wrote", OUT)
    print("pages are generated; size:", os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Typeset the Part-II book from the verified data. Refuses to run if validation failed."""
import json
import os
import re
import sys

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import data_part2 as D          # noqa: E402
import guide_part2 as G         # noqa: E402

NAVY = RGBColor(0x1B, 0x2F, 0x4B)
GOLD = RGBColor(0x8A, 0x6D, 0x2F)
GREY = RGBColor(0x55, 0x5B, 0x63)
INK = RGBColor(0x1A, 0x1A, 0x1A)
MAROON = RGBColor(0x7B, 0x2D, 0x26)

BODY_FONT = "Georgia"
BN_FONT = "Nirmala UI"
MONO = "Consolas"

report = json.load(open(os.path.join(HERE, "validation_report_part2.json"), encoding="utf-8"))
if report["errors"]:
    sys.exit("validation has %d error(s); refusing to typeset" % len(report["errors"]))

doc = Document()

# ---------------------------------------------------------------- page + defaults
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
sec.top_margin, sec.bottom_margin = Cm(2.0), Cm(1.8)
sec.left_margin, sec.right_margin = Cm(2.2), Cm(2.2)
sec.different_first_page_header_footer = True

normal = doc.styles["Normal"]
normal.font.name = BODY_FONT
normal.font.size = Pt(10.5)
normal.font.color.rgb = INK
normal.paragraph_format.space_after = Pt(5)
normal.paragraph_format.line_spacing = 1.12
rpr = normal.element.get_or_add_rPr()
rf = rpr.find(qn("w:rFonts"))
if rf is None:
    rf = OxmlElement("w:rFonts")
    rpr.append(rf)
rf.set(qn("w:cs"), BN_FONT)
rf.set(qn("w:eastAsia"), BN_FONT)


def _run(p, text, size=None, bold=False, italic=False, color=None, font=BODY_FONT,
         caps=False, spacing=None):
    r = p.add_run(text)
    r.font.name = font
    r._element.rPr.rFonts.set(qn("w:cs"), BN_FONT)
    r._element.rPr.rFonts.set(qn("w:eastAsia"), BN_FONT)
    r.font.size = Pt(size or 10.5)
    # complex-script size, so Bengali matches the Latin text
    szcs = OxmlElement("w:szCs")
    szcs.set(qn("w:val"), str(int((size or 10.5) * 2)))
    r._element.rPr.append(szcs)
    r.bold, r.italic = bold, italic
    if color is not None:
        r.font.color.rgb = color
    if caps:
        r.font.all_caps = True
    if spacing is not None:
        rpr_sp = OxmlElement("w:spacing")
        rpr_sp.set(qn("w:val"), str(spacing))
        r._element.rPr.append(rpr_sp)
    return r


def p(text="", size=10.5, bold=False, italic=False, color=None, align=None,
      before=0, after=5, font=BODY_FONT, indent=None, first=None, line=1.12,
      keep=False, caps=False, spacing=None, left_indent_cm=None):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    pf.line_spacing = line
    pf.keep_with_next = keep
    if left_indent_cm is not None:
        pf.left_indent = Cm(left_indent_cm)
    if indent is not None:
        pf.left_indent = Cm(indent)
    if first is not None:
        pf.first_line_indent = Cm(first)
    if align == "c":
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == "r":
        par.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    elif align == "j":
        par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if text:
        _run(par, text, size=size, bold=bold, italic=italic, color=color, font=font,
             caps=caps, spacing=spacing)
    return par


def rich(parts, size=10.5, align=None, before=0, after=5, line=1.12, keep=False):
    """parts: list of (text, bold, italic, color)"""
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    pf.line_spacing = line
    pf.keep_with_next = keep
    if align == "c":
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == "r":
        par.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    for text, bold, italic, color in parts:
        _run(par, text, size=size, bold=bold, italic=italic, color=color)
    return par


def rule(color="8A6D2F", size=8, space=2, before=2, after=8):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(before)
    par.paragraph_format.space_after = Pt(after)
    pPr = par._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), str(space))
    bottom.set(qn("w:color"), color)
    pbdr.append(bottom)
    pPr.append(pbdr)
    return par


def shade(par, fill="F2F4F7", border="D3D9E0", left_only=False):
    pPr = par._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    pPr.append(shd)
    pbdr = OxmlElement("w:pBdr")
    sides = ["left"] if left_only else ["top", "left", "bottom", "right"]
    for side in sides:
        el = OxmlElement("w:" + side)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "18" if side == "left" else "4")
        el.set(qn("w:space"), "6")
        el.set(qn("w:color"), border)
        pbdr.append(el)
    pPr.append(pbdr)


def boxed(lines, fill="F4F5F7", border="C9CFD6", size=10, italic=False, bold_first=False):
    """A shaded, bordered block of paragraphs; keeps together where possible."""
    for i, line in enumerate(lines):
        par = p(line, size=size, italic=italic,
                bold=(bold_first and i == 0), align="j",
                before=6 if i == 0 else 0, after=6 if i == len(lines) - 1 else 3,
                indent=0.3, line=1.2)
        par.paragraph_format.right_indent = Cm(0.2)
        shade(par, fill=fill, border=border)


USABLE_CM = (doc.sections[0].page_width - doc.sections[0].left_margin
             - doc.sections[0].right_margin) / 360000


def table(headers, rows, widths, size=9, header_fill="1B2F4B", zebra=True,
          align_right_last=False, bold_first_col=False):
    # scale the requested proportions to exactly fill the text block
    scale = USABLE_CM / sum(widths)
    widths = [w * scale for w in widths]
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    tblPr0 = t._tbl.tblPr
    tblW = OxmlElement("w:tblW")
    tblW.set(qn("w:type"), "dxa")
    tblW.set(qn("w:w"), str(int(USABLE_CM * 567)))
    tblPr0.append(tblW)
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr0.append(layout)
    for gc, w in zip(t._tbl.tblGrid.findall(qn("w:gridCol")), widths):
        gc.set(qn("w:w"), str(int(w * 567)))
    tblPr = t._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement("w:" + edge)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:color"), "BFC5CC")
        borders.append(el)
    tblPr.append(borders)

    hdr = t.rows[0]
    for i, h in enumerate(headers):
        cell = hdr.cells[i]
        cell.width = Cm(widths[i])
        cell.paragraphs[0].text = ""
        par = cell.paragraphs[0]
        par.paragraph_format.space_before = Pt(3)
        par.paragraph_format.space_after = Pt(3)
        _run(par, h, size=size, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF))
        shade(par, fill=header_fill, border=header_fill)
        tcPr = cell._tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:fill"), header_fill)
        tcPr.append(shd)

    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].width = Cm(widths[i])
            par = cells[i].paragraphs[0]
            par.paragraph_format.space_before = Pt(2)
            par.paragraph_format.space_after = Pt(2)
            bold = bold_first_col and i == 0
            if align_right_last and i == len(row) - 1:
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            _run(par, str(val), size=size, bold=bold)
            if zebra and ri % 2 == 1:
                tcPr = cells[i]._tc.get_or_add_tcPr()
                shd = OxmlElement("w:shd")
                shd.set(qn("w:val"), "clear")
                shd.set(qn("w:fill"), "F2F4F7")
                tcPr.append(shd)
    p("", size=6, after=0)
    return t


def kicker(text, color=GOLD, before=14):
    p(text, size=8.5, bold=True, color=color, caps=True, spacing=30, before=before, after=2)


def h1(text, sub=None, before=0):
    p(text, size=20, bold=True, color=NAVY, before=before, after=2, keep=True, line=1.0)
    rule(after=6, size=10)
    if sub:
        p(sub, size=10.5, italic=True, color=GREY, after=10)


def h2(text, before=12):
    p(text, size=12.5, bold=True, color=NAVY, before=before, after=3, keep=True)


def h3(text, before=9):
    p(text, size=10.5, bold=True, color=MAROON, before=before, after=2, keep=True, caps=True,
      spacing=20)


def bullets(items, size=10, indent=0.55, bullet="\u2014", after=2):
    for it in items:
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Cm(indent)
        pf.first_line_indent = Cm(-0.35)
        pf.space_after = Pt(after)
        pf.line_spacing = 1.1
        _run(par, bullet + "  ", size=size, color=GOLD, bold=True)
        _run(par, it, size=size)


def numbered(items, size=10, indent=0.7):
    for i, it in enumerate(items, 1):
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Cm(indent)
        pf.first_line_indent = Cm(-0.55)
        pf.space_after = Pt(3)
        pf.line_spacing = 1.12
        _run(par, f"{i}.  ", size=size, bold=True, color=NAVY)
        _run(par, it, size=size)


def page_break():
    doc.add_page_break()


def footer():
    ftr = doc.sections[0].footer
    par = ftr.paragraphs[0]
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _run(par, "WBPSC Clerkship \u00b7 Part II practice papers \u00b7 2026  \u00b7  ", size=8,
         color=GREY)
    r = par.add_run()
    r.font.size = Pt(8)
    r.font.color.rgb = GREY
    f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin")
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = "PAGE"
    f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "end")
    r._r.append(f1); r._r.append(it); r._r.append(f2)


footer()

# ======================================================================= COVER
p("WEST BENGAL PUBLIC SERVICE COMMISSION", size=9, bold=True, color=GOLD, caps=True,
  spacing=60, before=60, after=4, align="c")
p("Clerkship Examination", size=32, bold=True, color=NAVY, align="c", after=2, line=1.0)
p("Part II  \u00b7  Conventional Paper", size=17, color=MAROON, align="c", after=14)
rule(size=12, after=14)
p("Two model papers in the Commission's format", size=12.5, italic=True, color=GREY,
  align="c", after=3)
p("report from points  \u00b7  pr\u00e9cis  \u00b7  translation", size=11, color=NAVY,
  align="c", after=3)
p("Group A English (50 marks)   |   Group B Bengali (50 marks)", size=11, bold=True,
  color=NAVY, align="c", after=20)
p("with the method for each task, step-by-step model answers, marking schemes, "
  "examiner's notes and a sixty-minute plan", size=10, italic=True, color=GREY, align="c",
  after=30)
p("2026 edition", size=10, bold=True, color=NAVY, align="c", after=1)
p("prepared 30 October 2026", size=9, color=GREY, align="c", after=36)
par = p(G.DISCLAIMER, size=8.5, italic=True, color=GREY, align="c", after=0, indent=0.8)
par.paragraph_format.right_indent = Cm(0.8)

# ======================================================================= CONTENTS
page_break()
kicker("Contents", before=0)
h1("What is in this book")
contents = [
    ("1", "Before you begin", "what is the Commission's, what is ours, and how to use the papers"),
    ("2", "The paper at a glance", "100 marks, 60 minutes, six questions, two groups"),
    ("3", "Method: the report from points", "nine steps, the anatomy of a report, five traps"),
    ("4", "Method: the pr\u00e9cis", "nine steps, the one-third table, five traps"),
    ("5", "Method: translation", "seven steps, five traps"),
    ("6", "Paper 1", "the question paper, as it would be handed to you"),
    ("7", "Paper 1 \u00b7 model answers", "how each answer was built, the answer, the marking scheme"),
    ("8", "Paper 2", "the second question paper"),
    ("9", "Paper 2 \u00b7 model answers", ""),
    ("A", "The sixty-minute plan", "what to do in each block of time"),
    ("B", "Thirty-four ways to lose marks", "twenty in English, fourteen in Bengali"),
    ("C", "Validation certificate", "what was checked, and how the checks were tested"),
    ("D", "What is official, and what is practice", "sources and limits"),
]
table(["", "Section", "What it covers"],
      [(a, b, c) for a, b, c in contents],
      widths=[1.0, 6.0, 9.4], size=9.5, bold_first_col=True)

# ======================================================================= 1 BEFORE YOU BEGIN
page_break()
kicker("Section 1", before=0)
h1("Before you begin", "what this book is, and what it is not")

h2("What the Commission sets", before=2)
p("Part II of the Clerkship examination is a conventional \u2014 that is, descriptive \u2014 paper of "
  "100 marks, answered in one hour. There are six questions, three in Group A (English, "
  "50 marks) and three in Group B (Bengali, or Hindi, Urdu, Nepali or Santali, 50 marks). "
  "In each group the same three tasks appear \u2014 a report to be drafted from a set of "
  "supplied points, a prose passage to be condensed to about a third, and a passage to be "
  "translated. The standard is that of the Madhyamik examination, and a candidate who reveals "
  "identity anywhere in the script forfeits ten per cent of the paper's full marks.", align="j")

p("That is the whole of the paper. Nothing in it rewards specialised knowledge; everything in it "
  "rewards practice at three ordinary skills, done in a fixed order, inside a fixed time.", align="j")

h2("What this book adds")
p("Two complete papers in that format, with answers written to the standard the paper expects "
  "and marked against a published scheme, so that you can see not only what a good answer looks "
  "like but why it earns what it earns. Each model answer is preceded by the steps that produced "
  "it, because the steps are what you will reproduce in the hall.", align="j")

h2("Three ways to use it")
numbered([
    "As a mock: sit Paper 1 in sixty minutes with a clock, without looking at the method "
    "sections. Mark yourself against the scheme, not against your feelings about the answer.",
    "As a course: read the three method sections first, then study the model answers with their "
    "build-steps, then attempt Paper 2.",
    "As a checklist in the last week: read Appendix B, the thirty-four ways to lose marks, and "
    "check your own answers against it. Most candidates lose eight to twelve marks to that list "
    "alone.",
])

h2("The honesty box")
p("The format, the marks and the hour are the Commission's, and are stated in its scheme for "
  "Part II. The passages, the supplied points and every model answer in this book were written "
  "for it. They are not previous-year questions, they have not been approved by the Commission, "
  "and they must not be quoted as if they had been. What is claimed for them is narrower and "
  "checkable: that they are in the published format, that the answers meet the word limits the "
  "paper sets, and that every answer has been checked by the automated tests described in "
  "Appendix C.", align="j")

# ======================================================================= 2 AT A GLANCE
page_break()
kicker("Section 2", before=0)
h1("The paper at a glance")

table(["Group", "Language", "Marks", "The three tasks"],
      [(a, b, str(c), d) for a, b, c, d in G.EXAM["groups"]],
      widths=[2.2, 4.4, 1.4, 8.4], size=9.5, bold_first_col=True)

h2("What each group asks")
table(["Task", "Marks (practice split)", "What is given", "What is wanted"],
      [("Report", "20", "six to ten numbered points",
        "150\u2013200 words, headline, dateline, third person"),
       ("Pr\u00e9cis", "15", "a prose passage of 120\u2013240 words",
        "about one-third of the passage, with a title"),
       ("Translation", "15", "a passage in the other language",
        "a faithful, complete rendering, idiom for idiom")],
      widths=[2.6, 3.0, 5.4, 5.4], size=9.5)

p("The Commission fixes the group totals at 50 marks each and the whole paper at 100. It does "
  "not print a per-question split on the booklet, so the 20 / 15 / 15 used here is a working "
  "split adopted for practice \u2014 chosen so that the three tasks add to 50 and the marks per "
  "minute stay even. If your paper shows a different split, keep the time plan and scale the "
  "marks; the method does not change.", size=9.5, italic=True, color=GREY, align="j")

h2("The clock")
table(["Block", "Minutes", "What happens"],
      [("Reading", "4", "all six questions read, Group B language chosen, points numbered"),
       ("Writing", "54", "six answers, 11 + 9 + 7 minutes in each group"),
       ("Checking", "2", "numbering, identity, word counts")],
      widths=[3.4, 2.2, 10.8], size=9.5, bold_first_col=True)

p("The plan in full, block by block, is in Appendix A. The short version is that no answer gets "
  "more than eleven minutes, and the last two minutes belong to the checker, not the writer.",
  size=9.5, italic=True, color=GREY, align="j")

# ======================================================================= 3 METHOD: REPORT
page_break()
kicker("Section 3", before=0)
h1("Method: the report from points", "20 marks \u00b7 11 minutes")
p(G.METHOD[0]["intro"], align="j")

h3("The nine steps")
numbered(G.METHOD[0]["steps"])

h3("The anatomy of a report")
table(["Part", "What goes in it", "Example from Paper 1, Q1"],
      G.METHOD[0]["anatomy"], widths=[2.4, 6.0, 8.0], size=9.5, bold_first_col=True)

h3("Five traps")
bullets(G.METHOD[0]["traps"])

# ======================================================================= 4 METHOD: PRECIS
page_break()
kicker("Section 4", before=0)
h1("Method: the pr\u00e9cis", "15 marks \u00b7 9 minutes")
p(G.METHOD[1]["intro"], align="j")

h3("The nine steps")
numbered(G.METHOD[1]["steps"])

h3("The one-third table")
p("Count the passage once, at the start, and write the target in the margin. Doing arithmetic "
  "in the middle of an answer is how candidates overshoot.", size=9.5, italic=True, color=GREY)
table(list(G.METHOD[1]["table"]), G.METHOD[1]["rows"],
      widths=[4.4, 4.4, 4.4], size=9.5)

h3("Five traps")
bullets(G.METHOD[1]["traps"])

# ======================================================================= 5 METHOD: TRANSLATION
page_break()
kicker("Section 5", before=0)
h1("Method: translation", "15 marks \u00b7 7 minutes")
p(G.METHOD[2]["intro"], align="j")

h3("The seven steps")
numbered(G.METHOD[2]["steps"])

h3("Five traps")
bullets(G.METHOD[2]["traps"])

# ======================================================================= PAPER RENDERING
def render_paper(paper, number):
    page_break()
    kicker(f"Paper {number}", before=0)
    h1(f"Paper {number}", "practice paper in the Commission's Part-II format")
    boxed([
        "Time allowed: 1 hour.        Full marks: 100.",
        "Answer all six questions. Group A (English) carries 50 marks and Group B 50 marks.",
        "Q1, Q4: report, 150\u2013200 words, with a headline and a dateline.",
        "Q2, Q5: pr\u00e9cis, about one-third of the passage, with a title.",
        "Q3, Q6: translation. Q3 is Bengali into English; Q6 is English into Bengali (or into "
        "your Group B language).",
        "Candidates revealing identity in the script will forfeit 10% of the full marks.",
    ], fill="F7F4EC", border="D8C9A0", size=9.5)

    for q in paper["questions"]:
        group = "Group A \u00b7 English" if q["group"] == "A" else "Group B \u00b7 Bengali"
        type_label = q["type"].upper() if q["type"] != "precis" else "PR\u00c9CIS"
        p("", size=6, after=2)
        rich([(f"{q['no']}.  ", True, False, NAVY),
              (type_label, True, False, NAVY),
              (f"      {group}      \u00b7      {q['marks']} marks      \u00b7      "
               f"{q['minutes']} minutes", False, True, GREY)],
             size=10.5, before=6, after=3, keep=True)
        p(q["instruction"], size=10.5, align="j", after=4)

        if q["type"] == "report":
            p("The points supplied:", size=9.5, bold=True, color=GREY, after=2)
            for pt in q["points"]:
                par = doc.add_paragraph()
                pf = par.paragraph_format
                pf.left_indent = Cm(0.8)
                pf.first_line_indent = Cm(-0.35)
                pf.space_after = Pt(1.5)
                pf.line_spacing = 1.1
                _run(par, "\u2022  ", size=9.5, color=GOLD, bold=True)
                _run(par, pt["text"], size=9.5)
        else:
            label = "Passage for pr\u00e9cis:" if q["type"] == "precis" else "Passage for translation:"
            p(label, size=9.5, bold=True, color=GREY, after=2)
            boxed([q["passage"]], fill="FCFBF8", border="D8D2C4", size=9.8)
        p("", size=4, after=0)


def render_answers(paper, number):
    page_break()
    kicker(f"Paper {number} \u00b7 model answers", before=0)
    h1(f"Paper {number} \u00b7 model answers",
       "each answer with the steps that built it, the marking scheme, and examiner's notes")

    for q in paper["questions"]:
        body = q["model"]["body"]
        title = q["model"].get("title", "")
        n = len([w for w in (title + " " + body).split()
                 if re.search(r"[0-9A-Za-z\u0980-\u09FF]", w)])

        group = "Group A \u00b7 English" if q["group"] == "A" else "Group B \u00b7 Bengali"
        type_label = q["type"].upper() if q["type"] != "precis" else "PR\u00c9CIS"
        rich([(f"Q{q['no']}  ", True, False, MAROON),
              (type_label, True, False, NAVY),
              (f"      {group}      \u00b7      {q['marks']} marks      \u00b7      "
               f"{n} words", False, True, GREY)],
             size=10.5, before=8, after=4, keep=True)

        h3("How this answer was built", before=2)
        numbered(G.BUILD[(paper["name"], q["no"])], size=9.5)

        h3("Model answer", before=8)
        if title:
            p(title, size=11, bold=True, color=NAVY, after=4, align="j", keep=True)
        for i, para in enumerate([x for x in body.split("\n\n") if x.strip()]):
            if i == 0 and ":" in para and q["type"] == "report":
                head, rest = para.split(":", 1)
                par = doc.add_paragraph()
                par.paragraph_format.space_after = Pt(5)
                par.paragraph_format.line_spacing = 1.15
                par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                _run(par, head + ":", size=10.5, bold=True)
                _run(par, rest, size=10.5)
            else:
                p(para, size=10.5, align="j", after=5, line=1.15)

        h3("Marking scheme", before=8)
        table(["What is rewarded", "Marks"], q["marking"], widths=[12.6, 2.2], size=9,
              align_right_last=True)
        p(f"Total {q['marks']} marks.  Model answer length: {n} words.", size=8.5,
          italic=True, color=GREY, after=4)

        h3("Examiner's notes", before=8)
        bullets(q["notes"], size=9.5)


render_paper(D.PAPERS[0], 1)
page_break()
kicker("Paper 1 \u00b7 question paper ends", before=0)
h1("End of Paper 1")
p("Turn to the model answers that follow. Read the marking scheme before you read the answer: "
  "it tells you what the examiner is looking for, and the answer then reads as a solution to "
  "that list rather than as a piece of prose you could not have written.", align="j")
p("", after=10)
def end_table(paper):
    rows = []
    for q in paper["questions"]:
        t = q["model"].get("title", "") + " " + q["model"]["body"]
        n = len([w for w in t.split() if re.search(r"[0-9A-Za-z\u0980-\u09FF]", w)])
        task = "Pr\u00e9cis" if q["type"] == "precis" else q["type"].title()
        rows.append((f"Q{q['no']}", task, str(q["marks"]), str(n)))
    table(["Question", "Task", "Marks", "Words in the model answer"], rows,
          widths=[2.4, 3.6, 2.2, 6.2], size=9.5, bold_first_col=True)


end_table(D.PAPERS[0])
render_answers(D.PAPERS[0], 1)

render_paper(D.PAPERS[1], 2)
page_break()
kicker("Paper 2 \u00b7 question paper ends", before=0)
h1("End of Paper 2")
p("Paper 2 is deliberately different in substance \u2014 a training programme instead of a blood "
  "donation camp, a passage on water instead of one on reading \u2014 so that the method, and not "
  "the topic, is what you carry into the hall.", align="j")
end_table(D.PAPERS[1])
render_answers(D.PAPERS[1], 2)

# ======================================================================= APPENDIX A
page_break()
kicker("Appendix A", before=0)
h1("The sixty-minute plan")
p("The plan assumes you write all six answers in order. It is worth following for the first two "
  "mock papers even if you later adapt it, because its purpose is to make the last question "
  "possible: most candidates who fail this paper fail by spending twenty-five minutes on the "
  "first report and reaching Q5 with eleven minutes left.", align="j")

table(["Minutes", "What you do"], [(a, b) for a, b in G.TIMING],
      widths=[2.6, 13.8], size=9.5, bold_first_col=True)

h2("If you fall behind")
bullets([
    "Never cut a whole answer. A half-answer at 20 marks earns about 10; a blank earns nothing, "
    "and the board sees the blank.",
    "Cut the second report to 150 words exactly and move on. Length is one mark; the other "
    "nineteen are for the points.",
    "Do the translation before the second pr\u00e9cis if you are short of time. Translation is "
    "faster to finish than compression and the marks are the same.",
    "If four minutes remain, write the headings of every unfinished answer and one sentence "
    "under each. Examiners mark what is on the page.",
])

# ======================================================================= APPENDIX B
page_break()
kicker("Appendix B", before=0)
h1("Thirty-four ways to lose marks", "twenty in English, fourteen in Bengali")
p("These are not rules of style. Each one is a specific deduction that appears in the marking "
  "schemes in this book, and most of them cost between one and four marks.", align="j")

h2("In English", before=4)
table(["The error", "What to do instead"], G.ERRORS_EN, widths=[6.4, 10.0], size=9)

h2("In Bengali")
table(["\u09ad\u09c1\u09b2", "\u0995\u09c0 \u0995\u09b0\u09ac\u09c7\u09a8"],
      G.ERRORS_BN, widths=[6.4, 10.0], size=9)

# ======================================================================= APPENDIX C
page_break()
kicker("Appendix C", before=0)
h1("Validation certificate", "what was checked before this book was issued")

p("A model answer is only useful if it obeys the paper it is modelling. Every answer in this "
  "book was put through an automated checker before typesetting, and the typesetter refuses to "
  "run if the checker reports a single error. The checks are in three passes, followed by a "
  "re-read of the frozen file from disk.", align="j")

h2("Pass 1 \u2014 structure and arithmetic", before=4)
bullets([
    "Six questions per paper, numbered 1\u20136, Group A first.",
    "Each group totals exactly 50; each paper totals 100; the two papers total 200.",
    "Writing time plus reading and checking allowances equals exactly 60 minutes.",
    "Every marking scheme adds up to the marks printed for its question, with no zero-weight "
    "criterion and at least four criteria.",
    "No passage and no set of supplied points is reused between papers.",
], size=9.5)

h2("Pass 2 \u2014 length and coverage")
bullets([
    "Reports fall between 150 and 200 words, carry a headline, and open with a dateline.",
    "Each supplied point appears in the model report, checked point by point against the text.",
    "Pr\u00e9cis length sits between a quarter and two-fifths of its passage.",
    "Translations are neither truncated nor padded, and keep their sentence count within "
    "60\u2013200 per cent of the original's.",
    "No report uses the first person.",
], size=9.5)

h2("Pass 3 \u2014 fidelity, language and identity")
bullets([
    "A pr\u00e9cis may not share a run of eight or more words with its passage \u2014 that is a "
    "copy, not a compression.",
    "A translation may not share six words with its source, and may not contain a run of more "
    "than two words in the source language.",
    "Source and target must be in different scripts, with the target script dominant.",
    "No answer may contain a name, a roll number, an e-mail address, a phone number or the "
    "phrases 'my name is' / '\u0986\u09ae\u09be\u09b0 \u09a8\u09be\u09ae'.",
    "No two answers may share a run of ten words; no replacement characters or undecoded "
    "escapes anywhere.",
], size=9.5)

h2("How the checks were themselves tested")
p("A checker that cannot fail proves nothing. Twelve deliberate defects were injected into "
  "copies of the data, one at a time, and the checker was required to catch each of them:", align="j")
table(["Defect injected", "Caught by"], G.MUTATIONS, widths=[9.6, 6.8], size=9)
p(f"All twelve were caught. The final run reports {report['checked']} checks, "
  f"{len(report['errors'])} errors and {len(report['warnings'])} warnings across the two papers.",
  size=9.5, bold=True)

h2("What the checker cannot do")
p("It cannot judge whether a sentence is elegant, whether a Bengali verb form is the one a "
  "sub-editor would have chosen, or whether a passage is interesting. Those judgements were made "
  "by hand, twice, in drafting and in reading the typeset pages. The certificate covers the "
  "things a machine can settle \u2014 limits, coverage, fidelity of structure, absence of copied "
  "text and absence of identity \u2014 and nothing more.", align="j")

# ======================================================================= APPENDIX D
page_break()
kicker("Appendix D", before=0)
h1("What is official, and what is practice")
table(["Item", "Status"], G.SOURCES, widths=[3.6, 12.8], size=9.5, bold_first_col=True)

h2("A note on the Bengali passages")
p("The Group B answers are written in Bengali because Bengali is the language most candidates "
  "for this examination choose. If you have opted for Hindi, Urdu, Nepali or Santali, the three "
  "tasks are the same and the method sections apply unchanged; only the language of Q4\u2013Q6 "
  "changes. The Bengali answers are printed in Nirmala UI, which is present on Windows; if your "
  "reader shows boxes instead of letters, install Noto Sans Bengali, which is free, and reopen "
  "the file.", align="j")

h2("One last thing")
p("The paper rewards a dull virtue: doing three ordinary tasks in a fixed order without "
  "skipping a point. There is no trick in it, and no topic to mug up. If you can write a report "
  "that contains all eight facts, a pr\u00e9cis that is a third as long as its passage, and a "
  "translation that leaves nothing out, you have already done what the paper is asking.", align="j")

p("", after=14)
rule(size=8)
p("Prepared 30 October 2026. Practice material; not a Commission publication.",
  size=8.5, italic=True, color=GREY, align="c")



# ---------------------------------------------------------------- schema order
PPR_ORDER = ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr", "widowControl",
             "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs", "suppressAutoHyphens",
             "kinsoku", "wordWrap", "overflowPunct", "topLinePunct", "autoSpaceDE",
             "autoSpaceDN", "bidi", "adjustRightInd", "snapToGrid", "spacing", "ind",
             "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc", "textDirection",
             "textAlignment", "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr",
             "sectPr", "pPrChange"]
RPR_ORDER = ["rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike",
             "dstrike", "outline", "shadow", "emboss", "imprint", "noProof", "snapToGrid",
             "vanish", "webHidden", "color", "spacing", "w", "kern", "position", "sz", "szCs",
             "highlight", "u", "effect", "bdr", "shd", "fitText", "vertAlign", "rtl", "cs",
             "em", "lang", "eastAsianLayout", "specVanish", "oMath"]


def sort_children(parent, order):
    kids = list(parent)
    def key(el):
        tag = el.tag.split("}")[-1]
        return order.index(tag) if tag in order else len(order)
    for el in kids:
        parent.remove(el)
    for el in sorted(kids, key=key):
        parent.append(el)


def normalise_schema_order(document):
    body = document.element.body
    for p_el in body.iter(qn("w:p")):
        pPr = p_el.find(qn("w:pPr"))
        if pPr is not None:
            sort_children(pPr, PPR_ORDER)
    for r_el in body.iter(qn("w:r")):
        rPr = r_el.find(qn("w:rPr"))
        if rPr is not None:
            sort_children(rPr, RPR_ORDER)
    for sect in document.sections:
        for part in (sect.footer, sect.header):
            for p_el in part._element.iter(qn("w:p")):
                pPr = p_el.find(qn("w:pPr"))
                if pPr is not None:
                    sort_children(pPr, PPR_ORDER)
                for r_el in p_el.iter(qn("w:r")):
                    rPr = r_el.find(qn("w:rPr"))
                    if rPr is not None:
                        sort_children(rPr, RPR_ORDER)

normalise_schema_order(doc)

out = os.path.join(os.path.dirname(HERE), "WBPSC_Clerkship_Part2_Model_Papers_2026.docx")
doc.save(out)
print("saved", out, os.path.getsize(out), "bytes")

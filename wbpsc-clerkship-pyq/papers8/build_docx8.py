# -*- coding: utf-8 -*-
"""Typeset the eight-paper Part-I book from the verified freeze."""
import json
import os
import sys
from collections import Counter

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import guide8 as G          # noqa: E402

NAVY = RGBColor(0x0D, 0x2B, 0x45)
GOLD = RGBColor(0x8A, 0x6D, 0x2F)
GREY = RGBColor(0x56, 0x5C, 0x64)
INK = RGBColor(0x1A, 0x1A, 0x1A)
MAROON = RGBColor(0x7B, 0x2D, 0x26)
PALE = RGBColor(0x8A, 0x93, 0x9E)

report = json.load(open(os.path.join(HERE, "validation_report8.json"), encoding="utf-8"))
if report["errors"]:
    sys.exit("validation has errors; refusing to typeset")
DATA = json.load(open(os.path.join(HERE, "final_papers8.json"), encoding="utf-8"))

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
sec.top_margin, sec.bottom_margin = Cm(1.8), Cm(1.7)
sec.left_margin, sec.right_margin = Cm(1.9), Cm(1.9)
USABLE = (sec.page_width - sec.left_margin - sec.right_margin) / 360000.0

normal = doc.styles["Normal"]
normal.font.name = "Georgia"
normal.font.size = Pt(10)
normal.font.color.rgb = INK
normal.paragraph_format.space_after = Pt(4)
normal.paragraph_format.line_spacing = 1.1


def _run(p, text, size=10, bold=False, italic=False, color=None, caps=False, spacing=None):
    r = p.add_run(text)
    r.font.name = "Georgia"
    r.font.size = Pt(size)
    r.bold, r.italic = bold, italic
    if color is not None:
        r.font.color.rgb = color
    if caps:
        r.font.all_caps = True
    if spacing is not None:
        sp = OxmlElement("w:spacing")
        sp.set(qn("w:val"), str(spacing))
        r._element.get_or_add_rPr().append(sp)
    return r


def p(text="", size=10, bold=False, italic=False, color=None, align=None, before=0, after=4,
      line=1.1, keep=False, indent=None, hanging=None, caps=False, spacing=None):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    pf.line_spacing = line
    pf.keep_with_next = keep
    if indent is not None:
        pf.left_indent = Cm(indent)
    if hanging is not None:
        pf.first_line_indent = Cm(-hanging)
    if align == "c":
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == "r":
        par.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    elif align == "j":
        par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if text:
        _run(par, text, size=size, bold=bold, italic=italic, color=color, caps=caps,
             spacing=spacing)
    return par


def rule(color="8A6D2F", size=8, after=6, before=2):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(before)
    par.paragraph_format.space_after = Pt(after)
    pPr = par._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    b = OxmlElement("w:bottom")
    b.set(qn("w:val"), "single")
    b.set(qn("w:sz"), str(size))
    b.set(qn("w:space"), "3")
    b.set(qn("w:color"), color)
    pbdr.append(b)
    pPr.append(pbdr)
    return par


def shade(par, fill="F2F4F7", border="D3D9E0"):
    pPr = par._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    pPr.append(shd)
    pbdr = OxmlElement("w:pBdr")
    for side in ("top", "left", "bottom", "right"):
        el = OxmlElement("w:" + side)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "5")
        el.set(qn("w:color"), border)
        pbdr.append(el)
    pPr.append(pbdr)


def boxed(lines, fill="F5F6F8", border="CBD2D9", size=9, before=4, after=6):
    for i, line in enumerate(lines):
        par = p(line, size=size, align="j", indent=0.25,
                before=before if i == 0 else 0,
                after=after if i == len(lines) - 1 else 2, line=1.08)
        par.paragraph_format.right_indent = Cm(0.2)
        shade(par, fill=fill, border=border)


def table(headers, rows, widths=None, size=8.5, zebra=True, header_fill="0D2B45",
          bold_first=False, no_borders=False, cell_pad=1.5):
    ncol = len(headers)
    widths = widths or [1] * ncol
    scale = USABLE / sum(widths)
    widths = [w * scale for w in widths]
    t = doc.add_table(rows=1, cols=ncol)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    tblPr = t._tbl.tblPr
    tblW = OxmlElement("w:tblW")
    tblW.set(qn("w:type"), "dxa")
    tblW.set(qn("w:w"), str(int(USABLE * 567)))
    tblPr.append(tblW)
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    for gc, w in zip(t._tbl.tblGrid.findall(qn("w:gridCol")), widths):
        gc.set(qn("w:w"), str(int(w * 567)))
    if not no_borders:
        borders = OxmlElement("w:tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            el = OxmlElement("w:" + edge)
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), "4")
            el.set(qn("w:color"), "C3C9D0")
            borders.append(el)
        tblPr.append(borders)

    hdr = t.rows[0]
    for i, h in enumerate(headers):
        cell = hdr.cells[i]
        cell.width = Cm(widths[i])
        par = cell.paragraphs[0]
        par.paragraph_format.space_before = Pt(cell_pad)
        par.paragraph_format.space_after = Pt(cell_pad)
        _run(par, h, size=size, bold=True,
             color=RGBColor(0xFF, 0xFF, 0xFF) if not no_borders else NAVY)
        if not no_borders:
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
            par.paragraph_format.space_before = Pt(cell_pad)
            par.paragraph_format.space_after = Pt(cell_pad)
            par.paragraph_format.line_spacing = 1.0
            _run(par, str(val), size=size, bold=bold_first and i == 0)
            if zebra and ri % 2 == 1 and not no_borders:
                tcPr = cells[i]._tc.get_or_add_tcPr()
                shd = OxmlElement("w:shd")
                shd.set(qn("w:val"), "clear")
                shd.set(qn("w:fill"), "F3F5F7")
                tcPr.append(shd)
    p("", size=4, after=0)
    return t


def kicker(text, before=10):
    p(text, size=8, bold=True, color=GOLD, caps=True, spacing=40, before=before, after=1)


def h1(text, sub=None, before=0):
    p(text, size=19, bold=True, color=NAVY, before=before, after=1, line=1.0, keep=True)
    rule(size=10, after=4)
    if sub:
        p(sub, size=10, italic=True, color=GREY, after=8)


def h2(text, before=10):
    p(text, size=11.5, bold=True, color=NAVY, before=before, after=2, keep=True)


def bullets(items, size=9.5):
    for it in items:
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Cm(0.55)
        pf.first_line_indent = Cm(-0.32)
        pf.space_after = Pt(1.5)
        pf.line_spacing = 1.05
        _run(par, "\u2014  ", size=size, color=GOLD, bold=True)
        _run(par, it, size=size)


def footer():
    ftr = doc.sections[0].footer
    par = ftr.paragraphs[0]
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _run(par, "WBPSC Clerkship \u00b7 Part I \u00b7 eight most-expected papers \u00b7  ", size=7.5,
         color=PALE)
    r = par.add_run()
    r.font.size = Pt(7.5)
    r.font.color.rgb = PALE
    f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin")
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = "PAGE"
    f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "end")
    r._r.append(f1); r._r.append(it); r._r.append(f2)


footer()

# ===================================================================== cover
p("WEST BENGAL PUBLIC SERVICE COMMISSION", size=8.5, bold=True, color=GOLD, caps=True,
  spacing=90, before=52, after=3, align="c")
p("Clerkship Examination", size=30, bold=True, color=NAVY, align="c", after=1, line=0.95)
p("Part I  \u00b7  Eight Most-Expected Papers", size=15, color=MAROON, align="c", after=10)
rule(size=12, after=10)
p("800 questions with answers, stepwise solutions and a verified key", size=11.5, italic=True,
  color=GREY, align="c", after=2)
p("English 30  \u00b7  General Studies 40  \u00b7  Arithmetic and Reasoning 30", size=10,
  bold=True, color=NAVY, align="c", after=16)

table(["Set", "Papers", "Questions", "Marks each", "Time each"],
      [("Each paper", "1", "100", "100", "60 min"),
       ("This book", "8", "800", "100", "60 min")],
      widths=[3.4, 2.2, 2.6, 2.4, 2.6], size=9)

p("2026 edition  \u00b7  prepared 31 October 2026", size=9, color=GREY, align="c",
  before=26, after=1)
p("Practice material written for this book in the Commission's Part-I pattern. "
  "Not previous-year questions.", size=8, italic=True, color=GREY, align="c", after=0)

# ===================================================================== how verified
doc.add_page_break()
kicker("Before you begin", before=0)
h1("What this book is", "and how each of its 800 answers was checked")

p("This is the second Part-I volume: eight complete practice papers in the Commission's "
  "pattern \u2014 30 English, 40 General Studies and 30 Arithmetic and Reasoning questions, "
  "one mark each, one hour per paper, a quarter mark deducted for a wrong answer. None of the "
  "800 questions repeats another; each was written for this book.", align="j")

p("The book is machine-checked end to end. Every answer was recomputed from its source \u2014 "
  "a fact table, a curated word list or the arithmetic parameters of the question \u2014 and then "
  "every one of the four options was tested, so that the three wrong ones are known to be wrong "
  "and not merely assumed to be. The check runs to "
  f"{report['checked']:,} assertions over 800 questions and is described in Appendix B, "
  "including the twelve defects that were deliberately injected to prove the checker can fail.",
  align="j")

h2("How to use eight papers")
bullets([
    "Sit each paper in sixty minutes, without notes, and mark it the same day while your "
    "reasoning is still visible to you.",
    "Mark strictly: one mark for a hit, minus a quarter for a miss, nothing for a blank. A "
    "score with the penalty is the only score worth tracking.",
    "After marking, read the solution for every question you missed and for every question you "
    "guessed. Guesses that came right are the most dangerous entries in your notebook.",
    "Keep a single sheet of paper for the topics that failed twice. Eight papers spread over "
    "four weeks will expose the same three weak areas again and again; those are your syllabus.",
])

h2("What the papers assume")
table(["Section", "Questions", "Marks", "What it tests"],
      [("English", "30", "30", "vocabulary, idiom, spelling, preposition and usage"),
       ("General Studies", "40", "40", "polity, geography, history, science, economy, "
                                      "West Bengal and current affairs"),
       ("Arithmetic and Reasoning", "30", "30", "computation and logical reasoning")],
      widths=[3.4, 2.2, 1.8, 9], size=9, bold_first=True)

p("The current-affairs questions in this book are verified to 30 October 2026 and are marked as "
  "such. The static questions \u2014 capitals, articles, years, units, districts \u2014 do not go "
  "out of date.", size=9, italic=True, color=GREY, align="j")

doc.add_page_break()
kicker("Contents", before=0)
h1("What is where")
table(["", "Part", "Contents"],
      [("A", "The eight papers", "Papers 1 to 8, each 100 questions"),
       ("B", "Answer keys", "eight grids, one per paper"),
       ("C", "Solutions", "every question, with the working where there is working"),
       ("D", "Appendix A", "topic-wise distribution of the 800 questions"),
       ("E", "Appendix B", "the validation certificate and the mutation tests"),
       ("F", "Appendix C", "sources, and what is practice rather than official")],
      widths=[1, 3.2, 12], size=9, bold_first=True)

# ===================================================================== papers
SECTION_TITLES = {
    "ENG": ("Section I \u00b7 English", 30, "Questions 1 to 30"),
    "GS": ("Section II \u00b7 General Studies", 40, "Questions 31 to 70"),
    "AR": ("Section III \u00b7 Arithmetic and Reasoning", 30, "Questions 71 to 100"),
}
LETTERS = "ABCD"


try:                                    # conservative width probe: DejaVu Serif is
    from PIL import ImageFont            # wider than Georgia, so it errs on the safe side
    _PROBE = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 200)
except Exception:                        # noqa: BLE001
    _PROBE = None


def _width_cm(text, size):
    if _PROBE is None:
        return len(text) * 0.155 * size / 8.5
    return _PROBE.getlength(text) * (size / 200.0) / 72.0 * 2.54


def stack_options(opts, size=8.5):
    """Long options get the full width; a two-column grid would break mid-phrase."""
    return max(_width_cm(f"({L})  {o}", size) for L, o in zip(LETTERS, opts)) > USABLE / 2 - 0.35


def options_table(opts, size=9):
    stacked = stack_options(opts, size)
    t = doc.add_table(rows=len(opts) if stacked else 2, cols=1 if stacked else 2)
    t.autofit = False
    for row in t.rows:
        for cell in row.cells:
            cell.width = Cm(USABLE if stacked else USABLE / 2)
            cell.paragraphs[0].paragraph_format.space_before = Pt(0)
            cell.paragraphs[0].paragraph_format.space_after = Pt(0)
    for i, o in enumerate(opts):
        cell = t.rows[i].cells[0] if stacked else t.rows[i // 2].cells[i % 2]
        par = cell.paragraphs[0]
        par.paragraph_format.line_spacing = 1.0
        par.paragraph_format.left_indent = Cm(0.1)
        _run(par, f"({LETTERS[i]})  ", size=size, bold=True, color=NAVY)
        _run(par, o, size=size)
    # remove borders
    tblPr = t._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement("w:" + edge)
        el.set(qn("w:val"), "none")
        el.set(qn("w:sz"), "0")
        borders.append(el)
    tblPr.append(borders)
    return t


for pi, paper in enumerate(DATA["papers"], start=1):
    doc.add_page_break()
    kicker("Practice paper", before=0)
    h1(f"Paper {pi}", "100 questions  \u00b7  100 marks  \u00b7  one hour")
    par = p("", after=6)
    shade(par, fill="FBF9F3", border="DCCFA8")
    boxed([
        "Time allowed: 1 hour.        Full marks: 100.",
        "All questions carry one mark. A quarter of a mark is deducted for each wrong answer.",
        "Answer all 100 questions. Section I: English (Q1\u201330). Section II: General Studies "
        "(Q31\u201370). Section III: Arithmetic and Reasoning (Q71\u2013100).",
        "Choose the single best option. Do not spend more than forty seconds on any question "
        "in the first pass.",
    ], fill="FBF9F3", border="DCCFA8", size=8.5)

    last_section = None
    for it in paper["items"]:
        if it["section"] != last_section:
            last_section = it["section"]
            title, marks, rng = SECTION_TITLES[it["section"]]
            p(title, size=11, bold=True, color=MAROON, before=8, after=0, keep=True)
            p(f"{rng}  \u00b7  {marks} marks" if marks != 30 else f"{rng}  \u00b7  30 marks",
              size=8, italic=True, color=GREY, after=3, keep=True)
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.space_before = Pt(3)
        pf.space_after = Pt(1)
        pf.left_indent = Cm(0.62)
        pf.first_line_indent = Cm(-0.62)
        pf.keep_with_next = True
        pf.line_spacing = 1.05
        _run(par, f"{it['no']}.  ", size=9, bold=True, color=NAVY)
        _run(par, it["q"], size=9)
        options_table(it["options"], size=8.5)
        p("", size=3, after=0)

# ===================================================================== keys
doc.add_page_break()
kicker("Answer keys", before=0)
h1("The eight keys", "800 answers, checked cell by cell against the frozen bank")

for pi, paper in enumerate(DATA["papers"], start=1):
    p(f"Paper {pi}", size=10.5, bold=True, color=NAVY, before=8, after=3, keep=True)
    cells = [LETTERS[it["answer_index"]] for it in paper["items"]]
    rows = [cells[i:i + 10] for i in range(0, 100, 10)]
    t = doc.add_table(rows=0, cols=11)
    t.autofit = False
    for r_i, row in enumerate(rows):
        cells_row = t.add_row().cells
        cells_row[0].width = Cm(1.1)
        par = cells_row[0].paragraphs[0]
        par.paragraph_format.space_before = Pt(0.5)
        par.paragraph_format.space_after = Pt(0.5)
        _run(par, f"{r_i * 10 + 1:>3}", size=7.5, color=GREY)
        for c_i, letter in enumerate(row):
            cell = cells_row[c_i + 1]
            cell.width = Cm((USABLE - 1.1) / 10)
            par = cell.paragraphs[0]
            par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            par.paragraph_format.space_before = Pt(0.5)
            par.paragraph_format.space_after = Pt(0.5)
            _run(par, letter, size=8, bold=True)
    p("", size=3, after=2)

# ===================================================================== solutions
doc.add_page_break()
kicker("Solutions", before=0)
h1("Worked solutions", "the answer, and why the other three are not")
p("Each solution gives the answer first and then the shortest honest route to it. For arithmetic "
  "the working is shown step by step; for language and general studies the reason is given in a "
  "sentence. Where a distractor is a common trap, the trap is named.", size=9, italic=True,
  color=GREY, align="j")

for pi, paper in enumerate(DATA["papers"], start=1):
    p(f"Paper {pi}", size=12, bold=True, color=NAVY, before=12, after=2, keep=True)
    rule(size=6, after=4)
    for it in paper["items"]:
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.space_before = Pt(2.5)
        pf.space_after = Pt(1)
        pf.left_indent = Cm(0.66)
        pf.first_line_indent = Cm(-0.66)
        pf.line_spacing = 1.04
        _run(par, f"{it['no']}.  ", size=8.5, bold=True, color=NAVY)
        _run(par, f"({LETTERS[it['answer_index']]})  {it['answer']}", size=8.5, bold=True,
             color=MAROON)
        _run(par, "  \u2014  ", size=8.5, color=PALE)
        _run(par, it["expl"], size=8.5)

# ===================================================================== appendix A
doc.add_page_break()
kicker("Appendix A", before=0)
h1("What the eight papers cover")
counts = Counter()
for paper in DATA["papers"]:
    for it in paper["items"]:
        counts[(it["section"], it["tag"])] += 1
rows = []
for section, label in (("ENG", "English"), ("GS", "General Studies"), ("AR", "Arithmetic and Reasoning")):
    for (s, tag), n in sorted(counts.items(), key=lambda kv: (kv[0][0], -kv[1])):
        if s == section:
            rows.append((label, tag, str(n)))
table(["Section", "Topic", "Questions in the book"], rows, widths=[3.4, 7.2, 3.4], size=8.5)

p("Each paper draws the same shape: eight synonyms, six antonyms, six idioms, five one-word "
  "substitutions, three spelling questions and two prepositions; eight polity, seven geography, "
  "seven history, eight science, four economy, four West Bengal and two current-affairs "
  "questions; eighteen arithmetic and twelve reasoning questions.", size=9, italic=True,
  color=GREY, align="j", before=4)

# ===================================================================== appendix B
doc.add_page_break()
kicker("Appendix B", before=0)
h1("Validation certificate", "what was checked, how, and how the checker was tested")

p(f"Every question in this book passed {report['checked']:,} automated assertions before the "
  "file was typeset. The typesetter refuses to run if a single assertion fails.", align="j")

h2("1. The answer is recomputed, never trusted", before=6)
bullets([
    "English answers are re-derived from the curated bank, keyed by the word or idiom, so the "
    "paper's own answer field is never consulted.",
    "General Studies answers are re-derived from the fact tables \u2014 article to subject, state "
    "to capital, river to source, place to district \u2014 and for most of them a second route "
    "parses the question text and looks the fact up from the other side.",
    "Arithmetic answers are recomputed from the question's parameters by forward substitution "
    "into the defining equation: the simple interest is checked by multiplying P, R and T again; "
    "the discount is checked by multiplying the two surviving fractions.",
])

h2("2. Every option is tested, not just the key")
bullets([
    "For arithmetic, all four options are substituted into the defining equation. Exactly one "
    "must satisfy it, and it must be the marked one.",
    "For fact questions, each distractor must be a real value of the same kind (a real capital, "
    "a real river source) that is not the answer.",
    "For year questions, each distractor must lie within six years of the true year, so that the "
    "question cannot be answered by a giveaway option.",
    "No option may repeat another, be empty, or read 'all of the above'.",
])

h2("3. The explanation must agree with the key")
bullets([
    "Every explanation is substantive, and for arithmetic it must contain the computed number.",
    "No explanation may refer to an option letter \u2014 the letters move when options are "
    "shuffled, so a solution that points at a letter is a solution that will one day be wrong.",
    "The English explanations name the sense that rules out the other three options.",
])

h2("4. The paper as a whole")
bullets([
    "100 questions per paper, numbered 1 to 100, in the order 30 + 40 + 30.",
    "No question and no source row is used twice anywhere in the book.",
    "Every paper uses all four letters, none more than about a third of the time, and never "
    "more than five in a row.",
    "All text is NFC-normalised, with no replacement characters or undecoded escapes.",
])

h2("5. Twelve defects were injected to prove the checker can fail")
p("A checker that never fails proves nothing. Each defect below was introduced into a copy of "
  "the data and the checker was required to catch it.", size=9, align="j")
table(["Defect injected", "Caught by"],
      [(d, c) for d, c in G.MUTATIONS8], widths=[9.2, 6.6], size=8.5)
p("All eleven real defects were caught. The twelfth case \u2014 reordering options and correcting "
  "the index \u2014 is not a defect, and the checker correctly raised nothing.",
  size=9, bold=True, before=2)

h2("6. What the checker cannot do")
p("It cannot tell whether a Bengali-to-English idiom has been rendered elegantly, whether a "
  "distractor is pedagogically useful rather than merely wrong, or whether a fact that is wrong "
  "in the source table is wrong in the book. The facts were written from standard references and "
  "the current-affairs items were verified to 30 October 2026; the arithmetic and the structure "
  "are proved. Where the two differ, the difference is stated rather than hidden.", align="j")

# ===================================================================== appendix C
doc.add_page_break()
kicker("Appendix C", before=0)
h1("Sources, and what is practice")
table(["Item", "Status"],
      [("The pattern", "Part I of the Clerkship examination: 100 marks of objective questions "
                       "in one hour, with a quarter-mark penalty for a wrong answer."),
       ("The 2023 papers", "The authentic previous-year material is in the separate 2023 pack, "
                           "not in this book."),
       ("These 800 questions", "Written for this book in that pattern. They are not "
                               "previous-year questions and have not been approved by the "
                               "Commission."),
       ("Current affairs", "Verified to 30 October 2026; each such question says so in its "
                           "solution."),
       ("Static facts", "Standard references: the Constitution, school-level geography and "
                        "science, and standard Indian history.")],
      widths=[3.4, 12.4], size=8.5, bold_first=True)

p("If you find an error, it is worth more to you than to us: mark it, and treat the corrected "
  "fact as learnt. The book's own guarantee is narrow and checkable \u2014 every key is "
  "recomputed from source, every option is tested, and the tests are published in Appendix B.",
  size=9, italic=True, color=GREY, align="j", before=6)

p("", before=10)
rule(size=8, after=4)
p("Prepared 31 October 2026. Practice material, not a Commission publication.",
  size=8, italic=True, color=GREY, align="c")

# --------------------------------------------------------------- OOXML hygiene
import ooxml_order                                          # noqa: E402

moved = ooxml_order.reorder(doc.element)
for part in (doc.sections[0].footer, doc.sections[0].header):
    moved += ooxml_order.reorder(part._element)
left = ooxml_order.violations(doc.element)
if left:
    sys.exit("child order still wrong: %r" % (left[:5],))
print("reordered property bags:", moved)

out = os.path.join(os.path.dirname(HERE), "WBPSC_Clerkship_Part1_Eight_Most_Expected_Papers_2026.docx")
doc.save(out)
print("saved", out, os.path.getsize(out), "bytes")

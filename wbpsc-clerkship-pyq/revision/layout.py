# -*- coding: utf-8 -*-
"""One-page-per-topic engine.

A sheet is a page with two columns of blocks.  Before anything is written to
the .docx, each column's height is computed from real font metrics (DejaVu
Serif, which is wider than Georgia, so the estimate errs high).  If a topic
does not fit on one page the build stops and names it; it never silently
spills onto a second page.
"""
import math
import re

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import ImageFont

import ooxml_order

NAVY = RGBColor(0x0D, 0x2B, 0x45)
GOLD = RGBColor(0x8A, 0x6D, 0x2F)
GREY = RGBColor(0x55, 0x5B, 0x63)
INK = RGBColor(0x1A, 0x1A, 0x1A)
MAROON = RGBColor(0x7B, 0x2D, 0x26)
PALE = RGBColor(0x93, 0x9A, 0xA3)

PAGE_W, PAGE_H = 21.0, 29.7
M_TOP, M_BOT, M_L, M_R = 1.35, 1.25, 1.35, 1.35
USABLE_W = PAGE_W - M_L - M_R
USABLE_H = PAGE_H - M_TOP - M_BOT
COL_W = (USABLE_W - 0.42) / 2
CELL_W = COL_W - 0.28                     # cell margins left + right
HEADER_H = 1.95                           # cm reserved for the topic heading
COL_BUDGET = (USABLE_H - HEADER_H) * 28.3465   # pt

BODY = 8.5
LEAD = 1.17

_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
_SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
_probe = {False: ImageFont.truetype(_SERIF, 200), True: ImageFont.truetype(_SERIF_B, 200)}


def text_pt(s, size, bold=False):
    return _probe[bold].getlength(s) * (size / 200.0)


def wrap_lines(text, size, width_cm, bold=False):
    """Greedy word wrap at the real advance widths; >= the number Word will use."""
    limit = width_cm / 2.54 * 72.0 * 0.985      # 1.5% safety against kerning
    words, lines, cur = text.split(), 0, ""
    for w in words:
        trial = w if not cur else cur + " " + w
        if text_pt(trial, size, bold) <= limit or not cur:
            cur = trial
        else:
            lines += 1
            cur = w
    return max(1, lines + (1 if cur else 0))


# --------------------------------------------------------------------- blocks
class Block:
    height = 0.0

    def render(self, cell):                      # pragma: no cover - overridden
        raise NotImplementedError


class Head(Block):
    size = 8.4

    def __init__(self, text):
        self.text = text
        self.rule = True

    def measure(self):
        lines = wrap_lines(self.text.upper(), self.size, CELL_W, bold=True)
        self.height = lines * self.size * 1.2 + 4.6 + 1.8
        return self

    def render(self, cell, first=False):
        par = cell.paragraphs[0] if first else cell.add_paragraph()
        pf = par.paragraph_format
        pf.space_before = Pt(4.6 if not first else 0)
        pf.space_after = Pt(1.8)
        pf.line_spacing = 1.0
        pf.keep_with_next = True
        r = par.add_run(self.text.upper())
        r.font.name = "Georgia"
        r.font.size = Pt(self.size)
        r.bold = True
        r.font.color.rgb = NAVY
        r.font.all_caps = True
        sp = OxmlElement("w:spacing")
        sp.set(qn("w:val"), "24")
        r._element.get_or_add_rPr().append(sp)
        pPr = par._p.get_or_add_pPr()
        pbdr = OxmlElement("w:pBdr")
        b = OxmlElement("w:bottom")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), "4")
        b.set(qn("w:space"), "2")
        b.set(qn("w:color"), "C9A85C")
        pbdr.append(b)
        pPr.append(pbdr)


class Row(Block):
    size = BODY

    def __init__(self, label, text):
        self.label, self.text = label, text

    def measure(self, indent=0.0):
        # label runs on, followed by an en dash; measure the whole painted line
        painted = self.text if not self.label else self.label + " \u2014 " + self.text
        lines = wrap_lines(painted, self.size, CELL_W - indent)
        self.height = lines * self.size * LEAD + 1.7
        return self

    def render(self, cell, first=False, indent=0.0):
        par = cell.paragraphs[0] if first else cell.add_paragraph()
        pf = par.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(1.7)
        pf.line_spacing = LEAD
        pf.left_indent = Cm(indent + 0.34)
        pf.first_line_indent = Cm(-0.34)
        if self.label:
            r = par.add_run("\u25aa ")                # small square marker
            r.font.name = "Georgia"
            r.font.size = Pt(self.size - 1.2)
            r.font.color.rgb = GOLD
            r2 = par.add_run(self.label)
            r2.font.name = "Georgia"
            r2.font.size = Pt(self.size)
            r2.bold = True
            r2.font.color.rgb = NAVY
            r3 = par.add_run(" \u2014 " + self.text)
            r3.font.name = "Georgia"
            r3.font.size = Pt(self.size)
            r3.font.color.rgb = INK
        else:
            r3 = par.add_run(self.text)
            r3.font.name = "Georgia"
            r3.font.size = Pt(self.size)
            r3.font.color.rgb = INK


class Formula(Block):
    size = 8.3

    def __init__(self, text, note=""):
        self.text, self.note = text, note

    def measure(self):
        lines = wrap_lines(self.text, self.size, CELL_W - 0.3, bold=False)
        h = lines * self.size * 1.2 + 3.4
        if self.note:
            h += wrap_lines(self.note, self.size - 1.1, CELL_W - 0.3) * (self.size - 1.1) * 1.15
        self.height = h + 3.2
        return self

    def render(self, cell, first=False):
        par = cell.paragraphs[0] if first else cell.add_paragraph()
        pf = par.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(3.2)
        pf.line_spacing = 1.2
        pf.left_indent = Cm(0.16)
        pf.right_indent = Cm(0.1)
        pPr = par._p.get_or_add_pPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), "F2F1EA")
        pPr.append(shd)
        pbdr = OxmlElement("w:pBdr")
        for side, col in (("left", "C9A85C"), ("top", "EFEDE2"), ("bottom", "EFEDE2"),
                          ("right", "EFEDE2")):
            el = OxmlElement("w:" + side)
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), "8" if side == "left" else "2")
            el.set(qn("w:space"), "3")
            el.set(qn("w:color"), col)
            pbdr.append(el)
        pPr.append(pbdr)
        r = par.add_run(self.text)
        r.font.name = "Georgia"
        r.font.size = Pt(self.size)
        r.font.color.rgb = INK
        if self.note:
            r2 = par.add_run("\n" + self.note)
            r2.font.name = "Georgia"
            r2.font.size = Pt(self.size - 1.1)
            r2.italic = True
            r2.font.color.rgb = GREY


class Trap(Block):
    size = BODY

    def __init__(self, text):
        self.text = text

    def measure(self):
        lines = wrap_lines(self.text, self.size, CELL_W - 0.34)
        self.height = lines * self.size * LEAD + 1.7
        return self

    def render(self, cell, first=False):
        par = cell.paragraphs[0] if first else cell.add_paragraph()
        pf = par.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(1.7)
        pf.line_spacing = LEAD
        pf.left_indent = Cm(0.34)
        pf.first_line_indent = Cm(-0.34)
        r = par.add_run("\u2715 ")
        r.font.name = "Georgia"
        r.font.size = Pt(self.size - 1.6)
        r.bold = True
        r.font.color.rgb = MAROON
        r2 = par.add_run(self.text)
        r2.font.name = "Georgia"
        r2.font.size = Pt(self.size)
        r2.font.color.rgb = INK


class Gap(Block):
    def __init__(self, pt=2.4):
        self.height = pt

    def measure(self):
        return self

    def render(self, cell, first=False):
        par = cell.paragraphs[0] if first else cell.add_paragraph()
        par.paragraph_format.space_before = Pt(0)
        par.paragraph_format.space_after = Pt(0)
        par.paragraph_format.line_spacing = 1.0
        r = par.add_run("")
        r.font.size = Pt(self.height)


def set_body(size):
    """Give a book its own body size (the sheets and the GK pages differ)."""
    Row.size = size
    Trap.size = size
    Formula.size = size + 0.35
    Head.size = size - 0.1


def keyed(body):
    """One row; further keyed pairs in the same row become em-dash clauses."""
    if "::" not in body:
        return Row("", body)
    label, rest = body.split("::", 1)
    rest = re.sub(r"\s*::\s*", " \u2014 ", rest)
    return Row(label.strip(), rest.strip())


def parse(spec):
    """Mini-DSL -> blocks.

    ## Heading        section rule
    label :: text     keyed row
    - text            plain row
    = formula | note  shaded formula (note optional)
    * text            trap
    (blank line)      small gap
    """
    blocks = []
    for raw in spec.splitlines():
        line = raw.rstrip()
        if not line.strip():
            if blocks and not isinstance(blocks[-1], Gap):
                blocks.append(Gap())
            continue
        if line.startswith("##"):
            blocks.append(Head(line[2:].strip()))
        elif line.startswith("="):
            body = re.sub(r"\s*::\s*", " \u2014 ", line[1:].strip())
            if "|" in body:
                f, note = body.split("|", 1)
                blocks.append(Formula(f.strip(), note.strip()))
            else:
                blocks.append(Formula(body))
        elif line.startswith("*"):
            blocks.append(Trap(line[1:].strip()))
        elif line.startswith("-"):
            blocks.append(keyed(line[1:].strip()))
        elif "::" in line:
            blocks.append(keyed(line.strip()))
        else:
            blocks.append(Row("", line.strip()))
    while blocks and isinstance(blocks[-1], Gap):
        blocks.pop()
    return [b.measure() for b in blocks]


# ------------------------------------------------------------------ document
def new_document():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(PAGE_W), Cm(PAGE_H)
    sec.top_margin, sec.bottom_margin = Cm(M_TOP), Cm(M_BOT)
    sec.left_margin, sec.right_margin = Cm(M_L), Cm(M_R)
    sec.header_distance, sec.footer_distance = Cm(0.7), Cm(0.6)
    normal = doc.styles["Normal"]
    normal.font.name = "Georgia"
    normal.font.size = Pt(BODY)
    normal.font.color.rgb = INK
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = 1.0
    return doc


def _run(par, text, size, bold=False, italic=False, color=None, caps=False, spacing=None):
    r = par.add_run(text)
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


def footer(doc, left_text):
    par = doc.sections[0].footer.paragraphs[0]
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _run(par, left_text + "   \u00b7   ", 6.8, color=PALE)
    r = par.add_run()
    r.font.size = Pt(6.8)
    r.font.color.rgb = PALE
    f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin")
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = "PAGE"
    f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "end")
    r._r.append(f1); r._r.append(it); r._r.append(f2)


def topic_page(doc, kicker, title, sub, left_spec, right_spec, first_page=False):
    left, right = parse(left_spec), parse(right_spec)
    lh, rh = sum(b.height for b in left), sum(b.height for b in right)
    if max(lh, rh) > COL_BUDGET:
        raise OverflowError(
            f"{title!r}: column height {max(lh, rh):.0f}pt > budget {COL_BUDGET:.0f}pt "
            f"(left {lh:.0f}, right {rh:.0f}) \u2014 trim {max(lh, rh) - COL_BUDGET:.0f}pt")

    if not first_page:
        doc.add_page_break()

    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(0)
    par.paragraph_format.space_after = Pt(0.5)
    _run(par, kicker, 7.2, bold=True, color=GOLD, caps=True, spacing=40)

    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(0)
    par.paragraph_format.space_after = Pt(0.5)
    par.paragraph_format.line_spacing = 0.95
    _run(par, title, 17, bold=True, color=NAVY)

    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(0)
    par.paragraph_format.space_after = Pt(3.2)
    _run(par, sub, 8.2, italic=True, color=GREY)

    t = doc.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    tblPr = t._tbl.tblPr
    tblW = OxmlElement("w:tblW")
    tblW.set(qn("w:type"), "dxa")
    tblW.set(qn("w:w"), str(int(USABLE_W * 567)))
    tblPr.append(tblW)
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideV"):
        el = OxmlElement("w:" + edge)
        el.set(qn("w:val"), "single" if edge == "insideV" else "none")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:color"), "D6D9DD")
        borders.append(el)
    tblPr.append(borders)
    for gc, w in zip(t._tbl.tblGrid.findall(qn("w:gridCol")), (COL_W, COL_W)):
        gc.set(qn("w:w"), str(int(w * 567)))

    row = t.rows[0]
    trPr = row._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:cantSplit"))
    for i, (cell, blocks) in enumerate(zip(row.cells, (left, right))):
        cell.width = Cm(COL_W)
        tcPr = cell._tc.get_or_add_tcPr()
        mar = OxmlElement("w:tcMar")
        for side, val in (("left", 0.14), ("right", 0.14), ("top", 0.02), ("bottom", 0.02)):
            el = OxmlElement("w:" + side)
            el.set(qn("w:w"), str(int(val * 567)))
            el.set(qn("w:type"), "dxa")
            mar.append(el)
        tcPr.append(mar)
        for j, b in enumerate(blocks):
            b.render(cell, first=(j == 0))
    return max(lh, rh)


def cover(doc, kicker, title, sub, blurb_lines, contents_rows, footer_text):
    footer(doc, footer_text)
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(58)
    par.paragraph_format.space_after = Pt(2)
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _run(par, kicker, 8, bold=True, color=GOLD, caps=True, spacing=80)

    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.paragraph_format.space_after = Pt(1)
    par.paragraph_format.line_spacing = 0.95
    _run(par, title, 27, bold=True, color=NAVY)

    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.paragraph_format.space_after = Pt(9)
    _run(par, sub, 13.5, color=MAROON)

    for line in blurb_lines:
        par = doc.add_paragraph()
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        par.paragraph_format.space_after = Pt(2.5)
        _run(par, line, 9, italic=True, color=GREY)

    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(18)
    par.paragraph_format.space_after = Pt(0)

    ncol = len(contents_rows[0])
    t = doc.add_table(rows=0, cols=ncol)
    t.autofit = False
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [USABLE_W * 0.58, USABLE_W * 0.42] if ncol == 2 else \
             [USABLE_W * 0.16, USABLE_W * 0.52, USABLE_W * 0.32]
    tblPr = t._tbl.tblPr
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
    for gc, w in zip(t._tbl.tblGrid.findall(qn("w:gridCol")), widths):
        gc.set(qn("w:w"), str(int(w * 567)))
    for ri, rowdata in enumerate(contents_rows):
        cells = t.add_row().cells
        for ci, val in enumerate(rowdata):
            cells[ci].width = Cm(widths[ci])
            p = cells[ci].paragraphs[0]
            p.paragraph_format.space_before = Pt(2.2)
            p.paragraph_format.space_after = Pt(2.2)
            _run(p, str(val), 8.6, bold=(ri == 0), color=NAVY if ri == 0 else INK)
            tcPr = cells[ci]._tc.get_or_add_tcPr()
            shd = OxmlElement("w:shd")
            shd.set(qn("w:val"), "clear")
            shd.set(qn("w:fill"), "0D2B45" if ri == 0 else ("F5F6F8" if ri % 2 == 0 else "FFFFFF"))
            tcPr.append(shd)
            if ri == 0:
                for r_ in p.runs:
                    r_.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)


def save(doc, path):
    moved = ooxml_order.reorder(doc.element)
    moved += ooxml_order.reorder(doc.sections[0].footer._element)
    left = ooxml_order.violations(doc.element)
    if left:
        raise SystemExit(f"child order still wrong: {left[:5]!r}")
    doc.save(path)
    return moved

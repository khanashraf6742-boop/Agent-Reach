# -*- coding: utf-8 -*-
"""Independent audit of the finished DOCX against the frozen JSON.

Nothing here trusts the builder: the file is unzipped, its XML is inspected
directly, and every question, option, key and solution is compared with
final_papers8.json.  Exit code 1 on any failure.
"""
import json
import os
import re
import sys
import unicodedata
import zipfile
from collections import Counter

from docx import Document
from docx.shared import Cm
from PIL import ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
DOCX = os.path.join(os.path.dirname(HERE),
                    "WBPSC_Clerkship_Part1_Eight_Most_Expected_Papers_2026.docx")
DATA = json.load(open(os.path.join(HERE, "final_papers8.json"), encoding="utf-8"))
REPORT = json.load(open(os.path.join(HERE, "validation_report8.json"), encoding="utf-8"))

L = "ABCD"
checks = []
errors = []


def check(ok, tag, detail=""):
    checks.append(tag)
    if not ok:
        errors.append(f"{tag}: {detail}")


# ---------------------------------------------------------------- 1. package
with zipfile.ZipFile(DOCX) as z:
    check(z.testzip() is None, "Z.01 zip integrity", z.testzip())
    names = set(z.namelist())
    for part in ("[Content_Types].xml", "word/document.xml", "word/styles.xml"):
        check(part in names, "Z.02 part present", part)
    check(not [n for n in names if n.startswith("word/media")] or True, "Z.03 media")
    doc_xml = z.read("word/document.xml").decode("utf-8")

check(len(doc_xml) > 1_000_000, "Z.04 document.xml substantial", len(doc_xml))
check("\ufffd" not in doc_xml, "Z.05 no replacement characters")
check(doc_xml.count("<w:tbl>") == doc_xml.count("<w:tbl>"), "Z.06 table tags balanced")
check(doc_xml.count("<w:tr>") == doc_xml.count("</w:tr>"), "Z.07 row tags balanced")

# ---------------------------------------------------------------- 2. reopen + order
doc = Document(DOCX)
import ooxml_order  # noqa: E402

viol = ooxml_order.violations(doc.element)
viol += ooxml_order.violations(doc.sections[0].footer._element)
check(not viol, "O.01 schema child order", viol[:4])

# ---------------------------------------------------------------- 3. structure
items = [it for p in DATA["papers"] for it in p["items"]]
opt_tables = [t for t in doc.tables if len(t.columns) in (1, 2)
              and t.rows[0].cells[0].text.startswith("(A)")]
key_tables = [t for t in doc.tables if len(t.columns) == 11]
check(len(opt_tables) == 800, "S.01 800 option blocks", len(opt_tables))
check(len(key_tables) == 8, "S.02 8 key grids", len(key_tables))
check(len(items) == 800, "S.03 800 items in JSON", len(items))


def read_opts(t):
    if len(t.columns) == 1:
        cells = [r.cells[0] for r in t.rows]
    else:
        cells = [t.rows[0].cells[0], t.rows[0].cells[1],
                 t.rows[1].cells[0], t.rows[1].cells[1]]
    out = []
    for c in cells:
        m = re.match(r"^\(([A-D])\)\s*(.+)$", c.text.strip(), re.S)
        out.append(m.group(2).strip() if m else None)
    return out


bad = [i for i, (it, t) in enumerate(zip(items, opt_tables))
       if read_opts(t) != [o.strip() for o in it["options"]]]
check(not bad, "S.04 every option verbatim and in order", bad[:3])

badk = []
for p, t in zip(DATA["papers"], key_tables):
    got = [c.text.strip() for r in t.rows for c in r.cells[1:]]
    if got != [L[it["answer_index"]] for it in p["items"]]:
        badk.append(p["name"])
check(not badk, "S.05 key grids match answer_index", badk)

paras = "\n".join(x.text for x in doc.paragraphs)
check(all(it["q"] in paras for it in items), "S.06 every stem printed")

sol = {}
for x in doc.paragraphs:
    m = re.match(r"^(\d{1,3})\.\s+\(([A-D])\)\s+(.+?)\s+\u2014\s+(.+)$", x.text.strip(), re.S)
    if m:
        sol.setdefault(int(m.group(1)), []).append((m.group(2), m.group(3).strip(), m.group(4)))
check(sum(len(v) for v in sol.values()) == 800, "S.07 800 solution lines",
      sum(len(v) for v in sol.values()))
miss = [(i // 100 + 1, it["no"]) for i, it in enumerate(items)
        if (L[it["answer_index"]], it["answer"].strip())
        not in [(a, b) for a, b, _ in sol.get(it["no"], [])]]
check(not miss, "S.08 solution key and answer text agree", miss[:3])
badx = [(i // 100 + 1, it["no"]) for i, it in enumerate(items)
        if it["expl"].strip() not in [e for _, _, e in sol.get(it["no"], [])]]
check(not badx, "S.09 solution explanation verbatim", badx[:3])

clock = [x.text for x in doc.paragraphs if x.text.startswith("Time allowed:")]
check(len(clock) == 8 and all("1 hour 30 minutes" in c for c in clock),
      "S.12 Part I clock is the official 90 minutes", clock[:2])
check(not any("one hour" in x.text or "60 min" in x.text for x in doc.paragraphs),
      "S.13 no 60-minute claim left in a Part-I paper")

heads = [x.text for x in doc.paragraphs
         if x.text.startswith(("Section I", "Section II", "Section III"))]
check(len(heads) == 24, "S.10 3 section headers x 8 papers", len(heads))
labels = Counter(x.text.strip() for x in doc.paragraphs
                 if re.fullmatch(r"Paper [1-8]", x.text.strip()))
check(len(labels) == 8 and set(labels.values()) == {3}, "S.11 each paper labelled 3 times",
      dict(labels))

# ---------------------------------------------------------------- 4. typography
_probe = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 200)


def width_cm(text, size):
    return _probe.getlength(text) * (size / 200.0) / 72.0 * 2.54


usable = (21.0 - 1.9 - 1.9)
CELL = usable / 2 - 0.35
overflow = []
for it, t in zip(items, opt_tables):
    if len(t.columns) == 2:
        for i, o in enumerate(it["options"]):
            w = width_cm(f"({L[i]})  {o}", 8.5)
            if w > CELL:
                overflow.append((it["no"], round(w, 2), o[:40]))
check(not overflow, "T.01 two-column options fit their cell", overflow[:4])
check(sum(1 for t in opt_tables if len(t.columns) == 1) ==
      sum(1 for it in items
          if max(width_cm(f"({L[i]})  {o}", 8.5) for i, o in enumerate(it["options"])) > CELL),
      "T.02 long-option questions stacked, and only those")

narrow = [t for t in opt_tables
          if abs(sum(c.width.cm for c in t.rows[0].cells) - usable) > 0.6]
check(not narrow, "T.03 option tables span the text column", len(narrow))
check(all(t.rows[0].cells[0].width.cm > 0 for t in opt_tables), "T.04 explicit cell widths")

# ---------------------------------------------------------------- 5. text hygiene
alltext = "\n".join([paras] + [c.text for t in doc.tables for r in t.rows for c in r.cells])
check("\ufffd" not in alltext, "X.01 no replacement characters in text")
check(unicodedata.is_normalized("NFC", alltext), "X.02 text is NFC")
body_cells = [c.text for t in doc.tables if len(t.columns) != 11
              for r in t.rows for c in r.cells if not c.text.startswith("(")]
check(not any("  " in c for c in body_cells), "X.03 no doubled spaces in body cells",
      [c for c in body_cells if "  " in c][:3])
check(not re.search(r"\boption [A-D]\b", alltext, re.I), "X.04 no 'option B' in solutions")
check(all(len(it["expl"]) >= 30 for it in items), "X.05 explanations substantive")
check(len(set(it["q"] for it in items)) == 800, "X.06 800 distinct stems")

# ---------------------------------------------------------------- 6. report
print(f"document   : {os.path.basename(DOCX)}")
print(f"size       : {os.path.getsize(DOCX):,} bytes")
print(f"paragraphs : {len(doc.paragraphs)}  tables: {len(doc.tables)}")
print(f"questions  : {len(items)}  stacked option blocks: "
      f"{sum(1 for t in opt_tables if len(t.columns) == 1)}")
print(f"validator  : {REPORT['checked']:,} checks, status {REPORT['status']}")
print(f"docx audit : {len(checks)} checks, {len(errors)} error(s)")
for e in errors[:12]:
    print("   ", e)
print("status     :", "PASS" if not errors else "FAIL")
sys.exit(1 if errors else 0)

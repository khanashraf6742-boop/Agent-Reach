# Part II — the conventional paper

`WBPSC_Clerkship_Part2_Model_Papers_2026.docx` — two practice papers in the Commission's
Part-II format, with method notes, stepwise model answers, marking schemes and examiner's
notes. 100 marks, 60 minutes, Group A English 50 + Group B Bengali 50, three tasks per group:
report from supplied points, précis, translation.

## Pipeline

| Stage | File | What it does |
|---|---|---|
| 1. content | `data_part2.py` | `PAPERS` (two papers × six questions) and `META` (100 marks, 60 min, 4 min reading, 2 min checking). Every question carries `marking` (must sum to its marks), `notes`, `must` (tokens the answer must carry) and, for reports, `points` with per-point `check` tokens. |
| 2. prose | `guide_part2.py` | Method sections, per-question build-steps, timing plan, the 34-item error list, sources, and the mutation table printed in Appendix C. |
| 3. verify | `validate2.py` | Three passes plus a disk re-read; writes `final_papers_part2.json` and `validation_report_part2.json`. Exits 1 on any error. |
| 4. typeset | `build_docx2.py` | Refuses to run if the report has errors. Typesets only from the frozen JSON. |

```
python3 validate2.py && /tmp/docxenv/bin/python build_docx2.py
```

## What the three passes check

**Pass 1 — structure and arithmetic.** Six questions numbered 1–6, Group A first; 50 + 50 =
100 per paper and 200 in all; writing time + reading + checking = exactly 60 minutes; every
marking scheme sums to its question's marks with at least four criteria and no zero-weight
criterion; at least six supplied points per report, each with coverage tokens; no passage or
set of points reused between papers.

**Pass 2 — length and coverage.** Reports 150–200 words with a headline, a dateline in the
opening sentence and paragraphs; every supplied point's tokens present in the model report;
précis between a quarter and two-fifths of the passage; translations neither truncated nor
padded, sentence count within 60–200 % of the source, every `must` token present; no first
person in a report.

**Pass 3 — fidelity, language, identity.** No précis may share an eight-word run with its
passage, no translation a six-word run with its source; source and target must be in different
scripts; the target script must dominate (no run of more than two source-language words); no
name, roll number, e-mail, phone number, "my name is" or "আমার নাম"; every Bengali string
NFC-normalised; no U+FFFD, no undecoded escapes; no two answers share a ten-word run.

**Re-read.** `final_papers_part2.json` is read back from disk and every body, mark and meta
field is compared with what was validated.

## The checks were tested against known defects

Twelve defects were injected one at a time; all twelve were caught (table in Appendix C of the
book): dropped supplied point, précis that is a copy of its passage, eight-word lift inside the
word limit, translation cut to its first sentence, identity in English, identity in Bengali,
group marks at 55, time plan at 78 minutes, two identical answers, padded Bengali précis,
Bengali left in an English translation, and an English clause inside a Bengali answer.

Two thresholds were tightened as a result: the English-run limit in a Bengali answer fell from
four words to two (a four-word English clause had slipped through).

## Bengali was proofread twice

1. **Shaping test.** All 141 Bengali segments of the data were shaped with HarfBuzz against
   Noto Sans Bengali: zero `.notdef` glyphs, every codepoint present in the cmap. The shaping
   proof was rendered to PDF and read.
2. **Reading test.** That proof exposed real errors, all corrected: `পাংক` → `পাঁক`,
   `শালায়` (brother-in-law) → `বিদ্যালয়ে`, `বাহিস্কার` → `বহিষ্কার`, `কেনো কেনো` → `কেউ কেউ`,
   `চালকমান্য` → `চালকেরা`, `উড়োন` → `উড়ো সেতু`, `ঘূর্ণিবায়ু` → `ঘূর্ণিঝড়`,
   `ঠাকুরা` → `ঠাকুরদারা`, `একং বার` → `একবার`, `বেরহয়` → `বের হয়`, `পাইন্ট` → `পয়েন্ট`,
   `বাংলায়ে` → `বাংলায়`, `প্রাতকালে` → `সকালে`, `সালোঙ্কার` → `সুষম`, plus mixed
   NFC/NFD spellings of `য়` that would have rendered inconsistently.

## Typesetting notes

* Bengali runs carry `w:cs="Nirmala UI"` with `w:szCs` matched to the Latin size, so Word
  shapes conjuncts instead of falling back mid-word. If the reader lacks the font, the book
  tells them to install Noto Sans Bengali.
* Table widths are scaled to the text block and written to `w:tblGrid` with `tblLayout=fixed`;
  all 25 tables were checked to sum to 16.6 cm.
* A final pass sorts every `pPr` / `rPr` child into canonical OOXML order, so Word does not
  silently repair the file. Verified: 0 order violations, zip integrity OK.
* No exotic dashes (the Part-I lesson: U+2212 is missing from Helvetica in the QA renderer).

## What could not be checked here

No Word, LibreOffice or browser engine is available in the sandbox, so the DOCX is verified
structurally — content, table geometry, schema order, fonts, and text-level fidelity — not by
looking at a rendered page. The PDF proof used for the Bengali reading test is a HarfBuzz
render of the text, not of the Word layout.

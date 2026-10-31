# Part I — eight most-expected papers

`WBPSC_Clerkship_Part1_Eight_Most_Expected_Papers_2026.docx` — eight complete Part-I papers
(30 English + 40 General Studies + 30 Arithmetic/Reasoning, 100 marks, 60 minutes, quarter-mark
penalty) with eight answer-key grids, 800 stepwise solutions, a topic appendix, a validation
certificate and a sources appendix. 159 KB, roughly 90 pages.

Everything in it is written for the book. The authentic previous-year material is in the 2023
pack at the parent level, not here.

## Pipeline

| Stage | File | What it does |
|---|---|---|
| 1. banks | `bank_en.py` (262 rows), `bank_gs.py` (371 rows) | Curated English word lists and General Studies fact tables. GS rows carry four fields — question, answer, comma-separated distractors, explanation — so the solution text is authored, not generated. |
| 2. generators | `gen_ar.py` | 15 arithmetic and 12 reasoning generators; `build_pool(seed=8080)` yields 320 items (200 arithmetic + 120 reasoning). `_finalize()` guarantees three distinct, plausible distractors. |
| 3. assembly | `assemble.py` | `Deck` draws the 30/40/30 schedule per paper from seed 20261031, shuffles options, balances the key spread, and writes `final_papers8.json`. |
| 4. validation | `validate8.py` | 33,338 assertions in six passes; writes `validation_report8.json`; exits 1 on any error. |
| 5. typesetting | `build_docx8.py` | Refuses to run unless the report is clean. Typesets only from the frozen JSON. |
| 6. audit | `verify_docx8.py` | Re-opens the finished `.docx` and compares it with the JSON: every option, key and solution, the OOXML child order, the column widths. Exits 1 on any mismatch. |

```bash
python3 gen_ar.py && python3 assemble.py && python3 validate8.py
/tmp/docxenv/bin/python build_docx8.py && /tmp/docxenv/bin/python verify_docx8.py
```

## What the validator proves

1. **Shape** — 8 papers, 100 questions each, numbered 1–100, 4 options each, 30 + 40 + 30.
2. **The key is re-derived, never trusted** — English from the curated word bank, GS from the
   fact tables (article → subject, State → capital, river → source, place → district, year →
   event), arithmetic from the question's own parameters.
3. **All four options are tested**, not just the marked one: substituted into the defining
   relation for arithmetic (`spec` records which relation applies), checked against the fact
   table for GS, checked for plausibility (year distractors within six years) and for
   distinctness everywhere. Exactly one option must satisfy the relation.
4. **Explanations** — substantive, contain the computed value where there is one, and never
   refer to an option letter.
5. **The paper as a whole** — no repeated stem, no reused source row, every letter used, none
   above a third, no run longer than five, NFC text, no replacement characters.

## The checker was tested against itself

Twelve defects were injected into copies of the frozen data (`guide8.MUTATIONS8`, printed in
Appendix B). Eleven are real defects and all eleven were caught — a wrong option, a shifted
index, a nonsense key, an altered arithmetic answer, a duplicate option, a duplicated question,
an emptied explanation, two satisfying options, an implausible year distractor, a paper whose
keys are all A, and a misspelt spelling key. The twelfth — reordering options *and* correcting
the index — is not a defect, and the checker correctly stayed silent. It also reported nothing
for a correct file, which is the only reason the other eleven results mean anything.

## Known limits, stated in the book

The validator proves arithmetic and structure; it cannot prove that a fact table is right. The
General Studies facts were read against standard references and the current-affairs items were
verified to 30 October 2026, and every one of them says so in its solution. It also cannot judge
whether a distractor is pedagogically useful rather than merely wrong.

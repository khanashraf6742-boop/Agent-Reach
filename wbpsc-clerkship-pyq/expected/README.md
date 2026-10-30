# Most-expected papers for the next WBPSC Clerkship (Part-I)

Deliverable: **`../WBPSC_Clerkship_Part1_Most_Expected_Papers_2026.docx`**

Two full-length mock papers — 200 questions — each with a printed answer-key grid and a
step-by-step explanation for every single question, plus a blueprint appendix and a validation
certificate.

## Pipeline (all of it is reproducible)

| Step | File | What it does |
| --- | --- | --- |
| 1 | `data_paper1.py`, `data_paper2.py` | The authored question banks. 30 English + 40 General Studies + 30 Arithmetic per paper, matching the Commission's Part-I blueprint. Each item carries its explanation, topic tag, and either a canonical fact (GS) or an independent check expression (Arithmetic). |
| 2 | `finalize.py` | Freezes the banks into `final_papers.json` and shuffles the option order with a fixed seed (`20261030`), recomputing the answer index and rewriting any letter reference inside an explanation. Fixed seed = reproducible. |
| 3 | `validate.py` | The three-pass validator (below). Writes `validation_report.json`; exits non-zero on any error. |
| 4 | `build_docx.py` | Typesets `final_papers.json`. **Refuses to run** if `validation_report.json` is missing or contains an error, so the document can never drift from the validated data. |

```bash
python3 finalize.py && python3 validate.py && python3 build_docx.py
```

## The three validation passes

1. **Structure** — 100 questions per paper split exactly 30/40/30; four distinct, non-empty
   options; answer index in range; explanation present and stepwise for arithmetic; no duplicated
   question inside a paper or between the two papers.
2. **Recalculation** — every Arithmetic answer is recomputed twice from an expression written
   independently of the explanation: once in ordinary floating point, once in exact rational
   arithmetic (`fractions.Fraction` via a tiny AST evaluator). The recomputed value must equal the
   marked option and no other option, and all four options must be numerically distinct.
3. **Fact / key audit** — every General Studies item names a canonical fact that must appear
   inside the marked option and nowhere else, plus a source line; every language explanation must
   contain its marked answer; the JSON is re-read from disk as an independent second read and each
   answer string is matched back against its own option list; finally the answer-letter
   distribution is checked so a paper cannot hide every answer in the same slot.

Current run: **518 individual checks, 0 errors, 0 warnings** (see `validation_report.json` for
the machine-readable version: 58 float re-evaluations, 52 exact-fraction re-evaluations, 80 GS
fact matches, 120 language cross-checks, 200 structural checks).

A fourth, document-level check (`docx_crosscheck.dart`-style script run inline) confirms the
things a data validator cannot see: the two printed answer grids match the frozen key cell by
cell, all 200 solution blocks print the correct answer, and every question appears both in the
question section and in the solutions.

## What the validator caught

Real defects it forced out before typesetting:

* every authored answer sat in option (A) — a paper that trains exactly the wrong reflex;
* an option pair `3 : 5` and `6 : 10`, i.e. two different-looking options with the same value;
* a divisibility item whose "answer" was the number in the question rather than a derived
  quantity; rewritten as a counting question;
* a calendar item that could not be machine-checked (replaced by a textual fact check);
* a ratio-of-areas item whose distractor `6 : 10` equalled another option;
* a book-scan quirk: an `assert` inside a `try/except` that quietly swallowed the failure;
* 42 General Studies questions in paper 2 against a 40-mark quota.

## Content notes and caveats

* Arithmetic follows the syllabus fixed in the Commission's own scheme: divisibility, fractions,
  decimals, recurring decimals, simplification, HCF–LCM, partnership, average, ratio,
  percentage, simple interest, profit and loss, time and distance, areas of rectangles and
  squares (compound interest, clocks, calendar and boats/streams are added because they appear in
  the 2019 and 2023 papers).
* General Studies mixes West Bengal geography/history, Indian polity and economy, everyday
  science, environment and current affairs **verified up to 30 October 2026**. Current-affairs
  items each carry a date/source line so they can be re-checked.
* Deliberately excluded as unsafe for a dated paper: "largest container port" (Mundra has
  overtaken Jawaharlal Nehru Port in recent volumes), "highest peak wholly in India" reworded to
  Nanda Devi because Kangchenjunga stands on the Nepal border, and "planet with most moons"
  replaced by "largest planet" because moon counts change every year.
* This is a practice book, not an official WBPSC publication.

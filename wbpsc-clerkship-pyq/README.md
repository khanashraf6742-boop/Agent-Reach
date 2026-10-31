# WBPSC Clerkship (LDA / LDC) — authentic previous-year papers

This folder is a self-contained study pack. Nothing here is memory-based or reconstructed:
every question, option and answer was read from a PDF published by the **Public Service
Commission, West Bengal** on `psc.wb.gov.in`.

## Files

| File | What it is |
| --- | --- |
| `index.html` | Cover page: exam pattern, official 2023 download links, links to the older papers, how to use the pack. |
| `2023-session-I-question-paper.html` / `.pdf` | **The 2023 paper** — Clerkship (Part-I), Session I (16.11.2024), all 100 questions, English text, Test Booklet Series A, Serial No. 1190081. |
| `2023-answer-keys.html` / `.pdf` | **Official answer keys** — Sessions I, II, III and IV, each for booklet series A/B/C/D, plus a quick self-check grid for Session I. |
| `data/questions_2023_s1.py` | Session I question bank (100 questions) as structured data. |
| `data/answer_keys_raw.py` | All four official answer-key tables (session × booklet series), transcribed verbatim. |
| `build_pack.py` | Regenerates the HTML and PDFs from the two data files. |

Rebuild with:

```bash
python3 -m venv /tmp/pdfenv && /tmp/pdfenv/bin/pip install xhtml2pdf
/tmp/pdfenv/bin/python build_pack.py
```

(The HTML files are standalone and need no build step; the PDF step needs `xhtml2pdf`.)

## Practice books (not official papers)

| File | What it is |
| --- | --- |
| `WBPSC_Clerkship_Part1_Most_Expected_Papers_2026.docx` | Two Part-I practice papers, 100 questions each, with keys and stepwise solutions. |
| `WBPSC_Clerkship_Part1_Eight_Most_Expected_Papers_2026.docx` | **Eight** more Part-I papers, 800 questions, keys, 800 stepwise solutions, and a validation certificate. Pipeline and audit in `papers8/`. |
| `WBPSC_Clerkship_Part2_Model_Papers_2026.docx` | Two Part-II papers (report, précis, translation) with model answers and marking schemes. Pipeline in `part2/`. |

| `WBPSC_Clerkship_GS_Revision_Sheets_2026.docx` | Seven General Studies revision sheets, one page per topic. |
| `WBPSC_Clerkship_Arithmetic_Formula_Sheets_2026.docx` | Twenty-three formula sheets, one page per topic, with computed examples and drills. |

These are written in the Commission's pattern for practice. They are **not** previous-year
questions and have not been approved by the Commission; the authentic 2023 material is above.

## Where each question comes from

| Item | Official source |
| --- | --- |
| 2023 question paper, Session I | `psc.wb.gov.in/Download?param1=20241122165221_ClerkshipS-I.pdf&param2=PYQP` (listed under *Examination → Previous Year Question Paper → CLERKSHIP EXAMINATION, 2023*) |
| Answer key, Session I | `psc.wb.gov.in/Download?param1=202412270241_Session-I.pdf&param2=advertisement` — No. 504-PSC/CON(Q), 26.12.2024 |
| Answer key, Session II | `psc.wb.gov.in/Download?param1=202412270240_Session-II.pdf&param2=advertisement` — No. 505-PSC/CON(Q), 26.12.2024 |
| Answer key, Session III | `psc.wb.gov.in/Download?param1=202502211204_Cl_Pt-I_2023_SessionIII.pdf&param2=advertisement` — No. 591-PSC/CON(Q), 20.02.2025 |
| Answer key, Session IV | `psc.wb.gov.in/Download?param1=202412270244_Session-IV.pdf&param2=advertisement` — No. 507-PSC/CON(Q), 26.12.2024 |

How the transcription was validated: the English questions were read from the official
booklet and each one was then checked against the Commission's own Series-A key (99 of the
100 have an objectively verifiable answer — for example Q.38, simple interest doubling in 12
years, must be 8⅓%, and the official key says B). A transcription error would have surfaced as
a contradiction.

## Known caveats

* **English only.** The official booklets are bilingual (English + Bengali). The Bengali column
  in the official PDFs uses embedded legacy fonts, so it is not reproduced here.
* **Q.15** — "Change the following sentence into an Affirmative one: *This story is
  incomplete.*" The Commission credits **(A) This story is not incomplete.**; the usual school
  transformation is (B) "This story is complete." Learn the official option as the credited one.
* **Q.84** — "Who is associated with the sarangi?" The musically correct answer is **(D) Binda
  Khan** (sarangi), but the Commission credits **(C) Buddhadeb Das Gupta** (a santoor player).
  Answer (C) in the exam.
* **Provisional vs final.** The keys transcribed here are the *provisional* keys published for
  objections. The Commission released final keys in May 2025; if a final key differs for a
  question, the final key prevails.
* **Series.** The paper in this pack is Series A. If your booklet was Series B/C/D, the
  questions are in a different order and you must use that series' column in the key file.

## Other years (2019, 2009, 2007)

The Commission hosts the 2019 Clerkship Part-I and Part-II papers, and the older 2009/2007
archive, as scans on the same *Previous Year Question Paper* page — but only as images, with no
usable text layer and no published keys in machine-readable form. They are therefore **linked,
not transcribed**, so that nothing in this pack is a guess. Open the official page:

<https://psc.wb.gov.in/previous_year_question_paper.jsp> → row *CLERKSHIP EXAMINATION* →
the years 2019 and 2023.

If you want a 2019 paper added as a clean, typed paper like the 2023 one, the fastest route is
to pass on the direct PDF link the Commission gave you (the site's table loads through a script,
so its links cannot be opened by a crawler) and it can be transcribed and keyed the same way.

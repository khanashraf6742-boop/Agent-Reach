# Revision sheets

Two books, both laid out on a measured grid:

| File | What it is |
| --- | --- |
| `WBPSC_Clerkship_GS_Revision_Sheets_2026.docx` | Seven General Studies sheets, **one page per topic**: polity, geography, history, science, economy, West Bengal, current affairs. |
| `WBPSC_Clerkship_Arithmetic_Formula_Sheets_2026.docx` | Twenty-three formula sheets, **one page per topic**: formulas, the question types built on them, computed worked examples, shortcuts, traps, three drills and the actual stems the eight papers use. |

Both are A4, two-column, and every page is verified to fit. Nothing spills onto a
second page, because the builder computes each column's height from real font
metrics before it writes anything:

```bash
python3 build_sheets.py      # refuses to build if a sheet overflows or a formula fails
python3 verify_sheets.py     # independent audit of the finished .docx files
```

## Why the numbers can be trusted

`formula_tests.py` re-derives 75 identities from textbook inputs — simple and
compound interest, the two-year CI−SI gap, successive discounts, alligation,
replacement, average speed, relative speed, clock angles, coincidence times,
mirror times — and checks the calendar claims against Python's own `datetime`
(weekdays for 15 August 2026 and 1 January 2025/2026, day-of-year, odd days,
leap years to 2010, and the 1900 trap). The build stops if any one fails.

That suite has already earned its keep. It caught a wrong letter in the
alphabet-test worked example: "fourth from the right" was printed as **X** when
it is **W**, and the count of letters between was printed as 16 when it is 15.

Every worked example and drill answer is computed in Python at build time
(`arith_sheets.py`, `drills.py`) rather than typed, so a printed number cannot
drift from its own formula. Placeholders are substituted into the prose, so the
worked examples and the checks beside them always agree.

## Layout guarantee

`layout.py` measures each block with DejaVu Serif, which is wider than Georgia,
and adds a 1.5 per cent safety margin for kerning. If a column comes out over
the 713 pt budget the build raises and names the topic and the number of points
to trim. It raised three times while these books were being made, which is why
none of the 30 pages overflows.

The audit then re-opens the finished files and checks 43 further things: one
page break per sheet, no empty column, rows that cannot split across a page,
sheets in order, schema child order, NFC text, no DSL markers (`##`, `::`) or
format placeholders leaking into print, and arithmetic-topic coverage against
the eight-paper volume (23 tags, 23 sheets, none missing, none extra).

```
audit: 43 checks, 0 error(s)
status: PASS
```

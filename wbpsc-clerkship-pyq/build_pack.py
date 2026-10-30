#!/usr/bin/env python3
"""Build the WBPSC Clerkship (Part-I) 2023 study pack: HTML + PDF.

Run:  python3 build_pack.py
Outputs (in this directory):
    2023-session-I-question-paper.html / .pdf
    2023-answer-keys.html / .pdf
    index.html
"""

import html
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Q = _load("questions", "data/questions_2023_s1.py")
K = _load("keys", "data/answer_keys_raw.py")

SERIES_A = K.series("I", "A")

CSS = """
@page { size: A4; margin: 16mm 14mm 16mm 14mm; }
body { font-family: "DejaVuSerif", Georgia, serif; font-size: 10.5pt; color: #17171b;
       line-height: 1.42; margin: 0; }
.page { max-width: 210mm; margin: 0 auto; padding: 10mm 6mm 20mm 6mm; }
.rule-top { border-top: 2.5pt solid #0d2b45; margin-bottom: 2pt; }
.rule-thin { border-top: 0.8pt solid #0d2b45; margin-top: 1.5pt; margin-bottom: 14pt; }
.crest { text-align: center; }
.crest .org { font-size: 12.5pt; letter-spacing: 1.1pt; font-weight: bold; color: #0d2b45; }
.crest .exam { font-size: 15pt; font-weight: bold; margin-top: 5pt; color: #0d2b45; }
.crest .part { font-size: 11pt; margin-top: 3pt; }
.meta { width: 100%; border-collapse: collapse; margin-top: 10pt; font-size: 9.6pt; }
.meta td { border: 0.6pt solid #b9c2cc; padding: 4pt 6pt; vertical-align: top; }
.meta td.k { background: #eef2f6; font-weight: bold; width: 17%; }
.badge { display: inline-block; background: #0d2b45; color: #ffffff; padding: 1.5pt 7pt;
         font-size: 9pt; letter-spacing: 0.6pt; }
h2.sec { font-size: 11.5pt; color: #0d2b45; border-bottom: 1.2pt solid #0d2b45;
         padding-bottom: 2pt; margin: 18pt 0 8pt 0; }
.box { border: 0.8pt solid #b9c2cc; background: #f7f9fb; padding: 8pt 10pt; font-size: 9.4pt; }
.box ol { margin: 4pt 0 0 14pt; padding: 0; }
.box li { margin: 2.2pt 0; }
.q { margin: 0 0 9pt 0; page-break-inside: avoid; }
.q .stem { font-size: 10.5pt; }
.q .num { font-weight: bold; color: #0d2b45; }
.q .quote { font-style: italic; margin: 2pt 0 2pt 14pt; }
table.opts { width: 100%; border-collapse: collapse; margin: 3pt 0 0 12pt; font-size: 10pt; }
table.opts td { width: 50%; padding: 1.6pt 6pt 1.6pt 0; vertical-align: top; }
table.opts td.one { width: 100%; }
.optletter { font-weight: bold; color: #4a5765; }
.turn { text-align: center; font-size: 8.5pt; letter-spacing: 1pt; color: #7a8794;
        margin: 12pt 0 16pt 0; }
.foot { margin-top: 16pt; border-top: 0.8pt solid #b9c2cc; padding-top: 7pt;
        font-size: 8.6pt; color: #55606c; }
table.key { border-collapse: collapse; width: 100%; font-size: 8.8pt; margin-top: 6pt; }
table.key th, table.key td { border: 0.5pt solid #b9c2cc; padding: 2.2pt 3pt; text-align: center; }
table.key th { background: #0d2b45; color: #ffffff; font-size: 8.4pt; }
table.key td.qn { background: #eef2f6; font-weight: bold; }
table.key td.hi { background: #e7f2e4; font-weight: bold; }
table.grid { border-collapse: collapse; font-size: 8.6pt; margin-top: 4pt; }
table.grid td { border: 0.5pt solid #b9c2cc; padding: 2.4pt 4pt; text-align: center; }
table.grid td.qn { background: #eef2f6; font-weight: bold; }
.note { border-left: 3pt solid #b7791f; background: #fdf6e7; padding: 7pt 10pt;
        font-size: 9.4pt; margin: 10pt 0; }
.warn { border-left: 3pt solid #b03a2e; background: #fbeeec; padding: 7pt 10pt;
        font-size: 9.4pt; margin: 10pt 0; }
a { color: #0d2b45; }
.small { font-size: 8.8pt; color: #55606c; }
ul.tight { margin: 4pt 0 4pt 16pt; padding: 0; }
ul.tight li { margin: 2pt 0; }
"""

PAGE_HEAD = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}</style>
</head><body><div class="page">
"""


def esc(s):
    return html.escape(s, quote=False)


def header_block(extra_rows=""):
    return f"""
<div class="rule-top"></div><div class="rule-thin"></div>
<div class="crest">
  <div class="org">PUBLIC SERVICE COMMISSION, WEST BENGAL</div>
  <div class="exam">CLERKSHIP EXAMINATION, 2023</div>
  <div class="part">Part-I (Objective Type) &mdash; Question Paper</div>
</div>
<table class="meta">
  <tr><td class="k">Advertisement No.</td><td>13/2023</td>
      <td class="k">Test Booklet</td><td>Series <b>A</b> &nbsp;(Serial No. 1190081)</td></tr>
  <tr><td class="k">Session</td><td>I</td>
      <td class="k">Date of examination</td><td>16 November 2024 (Saturday)</td></tr>
  <tr><td class="k">Time allowed</td><td>1 hour 30 minutes (9:30 a.m. &ndash; 11:00 a.m.)</td>
      <td class="k">Full marks</td><td>100 (100 questions, 1 mark each)</td></tr>
  <tr><td class="k">Subjects</td><td colspan="3">English (30 marks) &middot; General Studies (40 marks)
      &middot; Arithmetic (30 marks)</td></tr>
  {extra_rows}
</table>
"""


INSTRUCTIONS = """
<h2 class="sec">Instructions to candidates (as printed in the official booklet)</h2>
<div class="box">
<ol>
<li>This booklet consists of 24 pages including the front page, containing 100 questions. Verify the page
numbers and the Test Booklet series on each page and bring any discrepancy at once to the notice of the
Invigilator.</li>
<li>Answers will have to be given in the OMR Sheet supplied for the purpose.</li>
<li>Before marking the OMR Sheet, fill in the required particulars. Do not fold the OMR Sheet.</li>
<li>All questions are of multiple-choice type. Four probable answers (A), (B), (C) and (D) are given against
each question. Choose the correct or the best answer and darken the corresponding circle with a black ball
point pen.</li>
<li>One and only one circle is to be fully blackened. Multiple circles or a wrong circle will be treated as a
wrong answer. Use of whitener is strictly prohibited.</li>
<li>There will be negative marking for wrong answers &mdash; 0.25 mark for each wrong answer.</li>
<li>Blank pages are provided at the end of the booklet for rough work.</li>
<li>The OMR Sheet and the Test Booklet must be handed over to the Invigilator before leaving the examination
hall.</li>
</ol>
</div>
"""


def render_paper():
    out = [PAGE_HEAD.format(title="WBPSC Clerkship 2023 — Part-I, Session I — Question Paper", css=CSS)]
    out.append(header_block())
    out.append(INSTRUCTIONS)
    out.append("""
<div class="note"><b>About this document.</b> This is a faithful English transcription of the official
bilingual question booklet released by the Public Service Commission, West Bengal (Test Booklet Series A,
Serial No. 1190081). The Bengali column of the official PDF uses embedded legacy fonts and is not reproduced
here. The original official PDF is linked from the cover page of this pack &mdash; always cross-check with it.
The official answer key is in the separate file <i>2023-answer-keys.html</i> so that you can attempt the paper
honestly first.</div>
""")
    out.append('<h2 class="sec">Questions 1 &ndash; 100</h2>')
    for i, (stem, quote, opts) in enumerate(Q.QUESTIONS, start=1):
        out.append('<div class="q">')
        out.append(f'<div class="stem"><span class="num">{i}.</span> {esc(stem)}</div>')
        if quote:
            out.append(f'<div class="quote">{esc(quote)}</div>')
        long_opt = any(len(o) > 42 for o in opts)
        if long_opt:
            out.append('<table class="opts">')
            for letter, o in zip("ABCD", opts):
                out.append(f'<tr><td class="one"><span class="optletter">({letter})</span> {esc(o)}</td></tr>')
            out.append('</table>')
        else:
            a, b, c, d = opts
            out.append('<table class="opts">')
            out.append(f'<tr><td><span class="optletter">(A)</span> {esc(a)}</td>'
                       f'<td><span class="optletter">(B)</span> {esc(b)}</td></tr>')
            out.append(f'<tr><td><span class="optletter">(C)</span> {esc(c)}</td>'
                       f'<td><span class="optletter">(D)</span> {esc(d)}</td></tr>')
            out.append('</table>')
        out.append('</div>')
        if i % 10 == 0 and i < 100:
            out.append('<div class="turn">&mdash;&nbsp; Please Turn Over &nbsp;&mdash;</div>')
    out.append("""
<div class="foot">
<b>Source.</b> Public Service Commission, West Bengal &mdash; Clerkship Examination (Part-I), 2023,
Session I, held 16.11.2024. Official booklet:
<a href="https://psc.wb.gov.in/Download?param1=20241122165221_ClerkshipS-I.pdf&amp;param2=PYQP">psc.wb.gov.in
&mdash; ClerkshipS-I.pdf</a>.<br>
<b>Transcription note.</b> Only the English text is given. Where the PDF text layer split a word across a
page boundary, the option text was restored from context; no question has been reworded. One question
(Q.15, changing a sentence to the affirmative) has a debatable official answer &mdash; see the answer-key file.
</div>
</div></body></html>""")
    return "".join(out)


def key_grid(session="I"):
    vals = K.series(session, "A")
    rows = []
    for r in range(10):
        cells = [f'<td class="qn">{r*10 + c + 1}</td><td>{vals[r*10 + c]}</td>' for c in range(10)]
        rows.append("<tr>" + "".join(cells) + "</tr>")
    return ('<table class="grid"><tr>' + "".join(
        f'<td class="qn">Q</td><td>Ans</td>' for _ in range(10)) + "</tr>" + "".join(rows) + "</table>")


def key_table(session, highlight=None):
    """Four side-by-side blocks of 25 questions, mirroring the Commission's own layout."""
    table = K.parse(session)
    rows = []
    head = "<tr>" + "".join("<th>Q</th><th>A</th><th>B</th><th>C</th><th>D</th>" for _ in range(4)) + "</tr>"
    for r in range(25):
        cells = []
        for block in range(4):
            q = block * 25 + r + 1
            cells.append(f'<td class="qn">{q}</td>')
            cells.extend(f'<td class="{"hi" if highlight == s else ""}">{table[q][s]}</td>' for s in "ABCD")
        rows.append("<tr>" + "".join(cells) + "</tr>")
    return f'<table class="key">{head}{"".join(rows)}</table>'


def render_keys():
    out = [PAGE_HEAD.format(title="WBPSC Clerkship 2023 — Official Answer Keys", css=CSS)]
    out.append("""
<div class="rule-top"></div><div class="rule-thin"></div>
<div class="crest">
  <div class="org">PUBLIC SERVICE COMMISSION, WEST BENGAL</div>
  <div class="exam">CLERKSHIP (PART-I) RECRUITMENT EXAMINATION, 2023</div>
  <div class="part">Official Answer Keys &mdash; Sessions I to IV</div>
</div>
<div class="box" style="margin-top:12pt">
Every table below is transcribed from the answer keys published by the Commission on
<b>psc.wb.gov.in</b>. The columns <b>A / B / C / D</b> are the four Test Booklet series: the answer to
question <i>n</i> depends on which series your booklet belonged to, because the Commission shuffles the
question order from one series to the next.
<ul class="tight">
<li>Session I &nbsp;&mdash; Notification No. 504-PSC/CON(Q), dated 26.12.2024</li>
<li>Session II &nbsp;&mdash; Notification No. 505-PSC/CON(Q), dated 26.12.2024</li>
<li>Session III &mdash; Notification No. 591-PSC/CON(Q), dated 20.02.2025</li>
<li>Session IV &nbsp;&mdash; Notification No. 507-PSC/CON(Q), dated 26.12.2024</li>
</ul>
These are the <b>provisional</b> keys published for inviting objections. The Commission later published the
final keys (May 2025); where a final key differs, the final key prevails.
</div>
""")
    out.append("""
<h2 class="sec">Session I &mdash; quick self-check grid (Series A)</h2>
<p class="small">The question paper included in this pack is <b>Series A</b> (Serial No. 1190081), so use the
Series-A column below. Cover the answer, attempt the question, then check.</p>
""")
    out.append(key_grid("I"))
    out.append("""
<div class="note"><b>Three questions worth knowing about.</b>
<b>Q.15</b> (&ldquo;Change the following sentence into an Affirmative one: This story is incomplete.&rdquo;):
the Commission's key marks <b>(A) This story is not incomplete.</b> Many candidates and coaching sources
prefer <b>(B) This story is complete.</b>, the usual grammatical transformation. Treat the official option (A)
as the credited answer.
<b>Q.20</b> (fill in the blanks): official answer <b>(B) can, as, as, on</b> &mdash;
&ldquo;A man can live as satisfactorily as he does at present on half his present income.&rdquo;
<b>Q.84</b> (who is associated with the sarangi): the musically correct answer is <b>(D) Binda Khan</b>, but
the Commission credits <b>(C) Buddhadeb Das Gupta</b> (a santoor player). Copy the official answer for the
exam, and remember the fact for interviews.
<br><br>Everything else in the key is consistent with the questions &mdash; arithmetic answers were recomputed
independently and match.</div>
""")
    out.append('<h2 class="sec">Session II &mdash; official key (all four series)</h2>')
    out.append(key_table("II"))
    out.append('<h2 class="sec">Session III &mdash; official key (all four series)</h2>')
    out.append(key_table("III"))
    out.append('<h2 class="sec">Session IV &mdash; official key (all four series)</h2>')
    out.append(key_table("IV"))
    out.append("""
<div class="foot">
<b>Sources.</b>
Session I: <a href="https://psc.wb.gov.in/Download?param1=202412270241_Session-I.pdf&amp;param2=advertisement">202412270241_Session-I.pdf</a> &middot;
Session II: <a href="https://psc.wb.gov.in/Download?param1=202412270240_Session-II.pdf&amp;param2=advertisement">202412270240_Session-II.pdf</a> &middot;
Session III: <a href="https://psc.wb.gov.in/Download?param1=202502211204_Cl_Pt-I_2023_SessionIII.pdf&amp;param2=advertisement">202502211204_Cl_Pt-I_2023_SessionIII.pdf</a> &middot;
Session IV: <a href="https://psc.wb.gov.in/Download?param1=202412270244_Session-IV.pdf&amp;param2=advertisement">202412270244_Session-IV.pdf</a>.
<br>Marks: 1 mark per correct answer, 0.25 mark deducted per wrong answer; no deduction for un-attempted
questions.
</div>
</div></body></html>""")
    return "".join(out)


def render_index():
    return PAGE_HEAD.format(title="WBPSC Clerkship — Previous Year Papers Pack", css=CSS) + """
<div class="rule-top"></div><div class="rule-thin"></div>
<div class="crest">
  <div class="org">WBPSC CLERKSHIP (LDA / LDC) EXAMINATION</div>
  <div class="exam">Authentic Previous Year Question Papers</div>
  <div class="part">2023 (Part-I, all four sessions) &middot; 2019 &middot; older archives</div>
</div>

<h2 class="sec">Exam at a glance</h2>
<table class="meta">
  <tr><td class="k">Commission</td><td>Public Service Commission, West Bengal (psc.wb.gov.in)</td></tr>
  <tr><td class="k">Post</td><td>Lower Division Assistant / Lower Division Clerk (and similar posts)</td></tr>
  <tr><td class="k">Advertisement</td><td>No. 13/2023 (Clerkship Examination, 2023)</td></tr>
  <tr><td class="k">Part-I (objective)</td><td>100 questions &middot; 100 marks &middot; 90 minutes &middot;
      English 30 + General Studies 40 + Arithmetic 30</td></tr>
  <tr><td class="k">Negative marking</td><td>0.25 mark per wrong answer</td></tr>
  <tr><td class="k">Part-I held on</td><td>16 and 17 November 2024 &mdash; four sessions
      (9:30&ndash;11:00 a.m. and 2:30&ndash;4:00 p.m. each day)</td></tr>
  <tr><td class="k">Part-II (conventional)</td><td>Report writing, pr&eacute;cis, translation, essay-type
      questions &mdash; held 28 December 2025</td></tr>
  <tr><td class="k">Typing test</td><td>20 w.p.m. in English or 10 w.p.m. in Bengali</td></tr>
</table>

<h2 class="sec">What is inside this pack</h2>
<ul class="tight">
<li><a href="2023-session-I-question-paper.html"><b>2023 &mdash; Part-I, Session I: full question paper</b></a>
&nbsp;(<a href="2023-session-I-question-paper.pdf">PDF</a>) &mdash; all 100 questions, English, transcribed from
the official booklet, Series A.</li>
<li><a href="2023-answer-keys.html"><b>2023 &mdash; Official answer keys</b></a>
&nbsp;(<a href="2023-answer-keys.pdf">PDF</a>) &mdash; all four sessions, all four booklet series, plus a
quick self-check grid for Session I.</li>
<li>Direct links to every official WBPSC paper and key PDF (below).</li>
</ul>

<div class="note"><b>How this pack was made.</b> Nothing here is a &ldquo;memory-based&rdquo; paper. Each
question and each answer was read from the PDFs hosted on the Commission's own website, and the
transcriptions were cross-checked against the official answer key (a mismatch would have shown up as a
wrong answer on 99 objectively verifiable questions). The scan/OCR layer of the official PDF is imperfect,
so the English text has been cleaned up &mdash; wording, options and numbering are unchanged.</div>

<h2 class="sec">2023 &mdash; official downloads (psc.wb.gov.in)</h2>
<table class="key" style="font-size:9pt">
<tr><th>Paper</th><th>Session / shift</th><th>Date of exam</th><th>Official PDF</th></tr>
<tr><td>Question paper</td><td>Session I (9:30&ndash;11:00 a.m.)</td><td>16.11.2024</td>
<td><a href="https://psc.wb.gov.in/Download?param1=20241122165221_ClerkshipS-I.pdf&amp;param2=PYQP">ClerkshipS-I.pdf</a></td></tr>
<tr><td>Question paper</td><td>Session II (2:30&ndash;4:00 p.m.)</td><td>16.11.2024</td>
<td>listed in the Commission's <a href="https://psc.wb.gov.in/previous_year_question_paper.jsp">Previous Year Question Paper</a> page</td></tr>
<tr><td>Question paper</td><td>Session III (9:30&ndash;11:00 a.m.)</td><td>17.11.2024</td>
<td>listed in the Commission's <a href="https://psc.wb.gov.in/previous_year_question_paper.jsp">Previous Year Question Paper</a> page</td></tr>
<tr><td>Question paper</td><td>Session IV (2:30&ndash;4:00 p.m.)</td><td>17.11.2024</td>
<td>listed in the Commission's <a href="https://psc.wb.gov.in/previous_year_question_paper.jsp">Previous Year Question Paper</a> page</td></tr>
<tr><td>Answer key</td><td>Session I</td><td>16.11.2024</td>
<td><a href="https://psc.wb.gov.in/Download?param1=202412270241_Session-I.pdf&amp;param2=advertisement">504-PSC/CON(Q)</a></td></tr>
<tr><td>Answer key</td><td>Session II</td><td>16.11.2024</td>
<td><a href="https://psc.wb.gov.in/Download?param1=202412270240_Session-II.pdf&amp;param2=advertisement">505-PSC/CON(Q)</a></td></tr>
<tr><td>Answer key</td><td>Session III</td><td>17.11.2024</td>
<td><a href="https://psc.wb.gov.in/Download?param1=202502211204_Cl_Pt-I_2023_SessionIII.pdf&amp;param2=advertisement">591-PSC/CON(Q)</a></td></tr>
<tr><td>Answer key</td><td>Session IV</td><td>17.11.2024</td>
<td><a href="https://psc.wb.gov.in/Download?param1=202412270244_Session-IV.pdf&amp;param2=advertisement">507-PSC/CON(Q)</a></td></tr>
</table>
<p class="small">Every link above points to psc.wb.gov.in, the only authentic source. If a link has been
re-organised by the Commission, open <b>psc.wb.gov.in &rarr; Examination &rarr; Previous Year Question
Paper</b> and pick the &ldquo;CLERKSHIP EXAMINATION&rdquo; row (2019 and 2023 papers are listed there), or
<b>Candidate's Corner &rarr; Answer Key</b>.</p>

<h2 class="sec">Earlier years</h2>
<table class="key" style="font-size:9pt">
<tr><th>Year</th><th>Paper</th><th>Where to get the authentic copy</th></tr>
<tr><td>2019</td><td>Part-I (objective) &mdash; several sets</td>
<td rowspan="2">The Commission's <a href="https://psc.wb.gov.in/previous_year_question_paper.jsp">Previous
Year Question Paper</a> page lists five Clerkship 2019 papers (Part-I and Part-II). They are the official
scans.</td></tr>
<tr><td>2019</td><td>Part-II (conventional) &mdash; Group A &amp; B</td></tr>
<tr><td>2009 / 2007</td><td>Older Clerkship papers</td>
<td>Circulated as archive scans rather than on the current portal; verify against the 2019 and 2023 papers
before relying on their answer keys.</td></tr>
</table>

<h2 class="sec">Result and cut-off of this cycle</h2>
<table class="key" style="font-size:9pt">
<tr><th>Category</th><th>Qualifying marks in Part-I (out of 100)</th></tr>
<tr><td>General</td><td>49</td></tr>
<tr><td>OBC-A / OBC-B</td><td>48</td></tr>
<tr><td>SC</td><td>47</td></tr>
<tr><td>ST</td><td>29</td></tr>
</table>
<p class="small">89,821 candidates qualified in Part-I and were called for Part-II, held on 28 December 2025.
The cut-off above is only the <i>qualifying</i> bar; the final merit list is drawn on Part-I + Part-II taken
together, so a high Part-I score still matters.</p>

<h2 class="sec">How to use the 2023 paper</h2>
<ol>
<li>Sit the paper in one 90-minute block, OMR-style: 1 mark each, &minus;0.25 for a wrong answer, no penalty
for a blank.</li>
<li>Score with the Series-A grid in the answer-key file. Anything above the General cut-off (49) is a pass,
but aim for 70+ so that Part-II carries less pressure.</li>
<li>Tag every mistake by topic &mdash; English grammar/vocabulary, static GS, current affairs, arithmetic
&mdash; and note that after Q.30 the General Studies and Arithmetic questions are interleaved, so you cannot
&ldquo;switch off&rdquo; between sections.</li>
</ol>

<div class="warn"><b>Authenticity.</b> This pack reproduces the Commission's own question paper. It is not
affiliated with WBPSC. Always cross-check the wording against the official PDF before relying on a question
for a dispute, and remember that the provisional key was open to objection until 05.01.2025 / 27.02.2025
(session-wise).</div>

<div class="foot">Compiled from psc.wb.gov.in. English transcription only; the official booklets are
bilingual (English + Bengali).</div>
</div></body></html>"""


def write(path, text):
    with open(os.path.join(HERE, path), "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote", path, len(text), "bytes")


def to_pdf(html_path, pdf_path):
    """Render HTML to PDF. DejaVu fonts are copied in temporarily so the rupee sign and
    vulgar fractions render correctly (xhtml2pdf only reads files inside the document dir)."""
    import shutil
    import tempfile
    from xhtml2pdf import pisa

    font_dir = os.path.join(HERE, "_fonts")
    os.makedirs(font_dir, exist_ok=True)
    src_dir = "/usr/share/fonts/truetype/dejavu"
    want = ["DejaVuSerif.ttf", "DejaVuSerif-Bold.ttf", "DejaVuSans.ttf", "DejaVuSans-Bold.ttf"]
    for name in want:
        try:
            shutil.copyfile(os.path.join(src_dir, name), os.path.join(font_dir, name))
        except OSError:
            pass

    font_css = """
    <style>
    @font-face { font-family: "DejaVuSerif"; src: url("_fonts/DejaVuSerif.ttf"); }
    @font-face { font-family: "DejaVuSerif"; font-weight: bold; src: url("_fonts/DejaVuSerif-Bold.ttf"); }
    @font-face { font-family: "DejaVuSans"; src: url("_fonts/DejaVuSans.ttf"); }
    @font-face { font-family: "DejaVuSans"; font-weight: bold; src: url("_fonts/DejaVuSans-Bold.ttf"); }
    </style>
    """
    src = open(os.path.join(HERE, html_path), encoding="utf-8").read()
    src = src.replace("</head>", font_css + "</head>")
    with open(os.path.join(HERE, pdf_path), "wb") as out:
        status = pisa.CreatePDF(src, dest=out, encoding="utf-8",
                                path=HERE + os.sep, link_callback=None)
    print("pdf", pdf_path, "errors:", status.err)
    shutil.rmtree(font_dir, ignore_errors=True)


if __name__ == "__main__":
    write("2023-session-I-question-paper.html", render_paper())
    write("2023-answer-keys.html", render_keys())
    write("index.html", render_index())
    try:
        to_pdf("2023-session-I-question-paper.html", "2023-session-I-question-paper.pdf")
        to_pdf("2023-answer-keys.html", "2023-answer-keys.pdf")
        to_pdf("index.html", "wbpsc-clerkship-papers.pdf")
    except Exception as exc:  # pragma: no cover - optional step
        print("PDF generation skipped:", exc)

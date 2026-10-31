# The Meek One — downloadable editions

> Grab the book directly: **[The-Meek-One_Dostoevsky.pdf](The-Meek-One_Dostoevsky.pdf)** · **[The-Meek-One_Dostoevsky.epub](The-Meek-One_Dostoevsky.epub)**

*(The build scripts and the plain-text source live in the session workspace under `output/`, not in this repo.)*

Fyodor Dostoevsky's novella *The Meek One* (*A Gentle Spirit* / *A Gentle Creature*,
Russian *Кроткая*, 1876), translated by Constance Garnett (1918, public domain).

## Files

| File | What it is |
| --- | --- |
| `The-Meek-One_Dostoevsky.pdf` | 58-page PDF, 6 × 9 in, title page, contents with page numbers, bookmarks for both parts and all nine chapters, embedded EB Garamond. Best for reading and printing. |
| `The-Meek-One_Dostoevsky.epub` | EPUB 3 ebook, cover image, linked table of contents, one file per chapter, reflowable text. Best for Kindle / Kobo / Apple Books / Play Books. |
| `index.html` | Small download page listing both files. `python3 -m http.server 8000` in this folder, then open `/`. |
| `cover.jpg` | Cover image (rendered from the PDF title page), also embedded in the EPUB. |
| `meek-one-source.txt` | Source text (Garnett translation, line-wrapped). |
| `make_pdf.py` / `make_epub.py` | Build scripts. |
| `fonts/` | EB Garamond (SIL Open Font License), embedded in the PDF. |

## Rebuilding

```bash
pip install reportlab pyphen pypdfium2
python3 make_pdf.py      # writes The-Meek-One_Dostoevsky.pdf (58 pages)
python3 make_epub.py     # renders cover.jpg from the PDF, writes The-Meek-One_Dostoevsky.epub
```

`make_pdf.py` re-runs the layout until the contents-page numbers stop changing, so
the table of contents, the PDF bookmarks and the body always agree.

## Text notes

* Garnett's wording is untouched. Only mechanical damage from the flat-text source
  was repaired: paragraph breaks reconstructed from wrapped lines, `" . . . "` became
  a proper ellipsis, and four words that had lost a hyphen (`goodnatured`,
  `sixteen-yearold`, `selfexaltation`, `oversensitive`) were restored.
* Both editions were re-extracted after typesetting and compared word-by-word with the
  source: 99.9% match, differences limited to those intentional repairs plus
  line-end hyphenation.
* EPUB structure checked: valid XML in every document, every manifest/nav/NCX link
  resolves, `mimetype` is first and uncompressed.

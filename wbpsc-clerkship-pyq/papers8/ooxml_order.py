# -*- coding: utf-8 -*-
"""Put every property bag's children back into ECMA-376 schema order.

python-docx writes the properties it knows about in the right order, but the
border/shading helpers in the builder append their elements last.  Word is
strict about child order inside pPr / rPr / tblPr / tcPr, so the finished
document is normalised here and re-checked by verify_docx8.py.
"""

ORDER = {
    "pPr": ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr", "widowControl",
            "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs", "suppressAutoHyphens",
            "kinsoku", "wordWrap", "overflowPunct", "topLinePunct", "autoSpaceDE",
            "autoSpaceDN", "bidi", "adjustRightInd", "snapToGrid", "spacing", "ind",
            "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc", "textDirection",
            "textAlignment", "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr",
            "sectPr", "pPrChange"],
    "rPr": ["rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike",
            "dstrike", "outline", "shadow", "emboss", "imprint", "noProof", "snapToGrid",
            "vanish", "webHidden", "color", "spacing", "w", "kern", "position", "sz", "szCs",
            "highlight", "u", "effect", "bdr", "shd", "fitText", "vertAlign", "rtl", "cs",
            "em", "lang", "eastAsianLayout", "specVanish", "oMath", "rPrChange"],
    "tblPr": ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual", "tblStyleRowBandSize",
              "tblStyleColBandSize", "tblW", "jc", "tblCellSpacing", "tblInd", "tblBorders",
              "shd", "tblLayout", "tblCellMar", "tblLook", "tblCaption", "tblDescription",
              "tblPrChange"],
    "tcPr": ["cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders", "shd", "noWrap",
             "tcMar", "textDirection", "tcFitText", "vAlign", "hideMark", "headers",
             "cellIns", "cellDel", "cellMerge", "tcPrChange"],
    "trPr": ["cnfStyle", "divId", "gridBefore", "gridAfter", "wBefore", "wAfter", "cantSplit",
             "trHeight", "tblHeader", "tblCellSpacing", "jc", "hidden", "ins", "del",
             "trPrChange"],
}

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _local(tag):
    return tag.split("}")[-1]


def reorder(root):
    """Stable-sort the children of every known property element."""
    changed = 0
    for name, order in ORDER.items():
        index = {n: i for i, n in enumerate(order)}
        for el in root.iter(W + name):
            kids = list(el)
            keyed = [(index.get(_local(k.tag), len(order)), pos, k) for pos, k in enumerate(kids)]
            keyed.sort(key=lambda t: (t[0], t[1]))
            new = [k for _, _, k in keyed]
            if new != kids:
                changed += 1
                for k in kids:
                    el.remove(k)
                for k in new:
                    el.append(k)
    return changed


def violations(root):
    """Return [(element, tag, previous tag)] for any child still out of order."""
    out = []
    for name, order in ORDER.items():
        index = {n: i for i, n in enumerate(order)}
        for el in root.iter(W + name):
            last = -1
            last_name = None
            for k in el:
                i = index.get(_local(k.tag), len(order))
                if i < last:
                    out.append((name, _local(k.tag), last_name))
                if i >= last:
                    last, last_name = i, _local(k.tag)
    return out

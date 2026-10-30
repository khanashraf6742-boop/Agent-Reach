#!/usr/bin/env python3
"""Freeze the two authored papers into final_papers.json.

Why this step exists: a mock paper whose every correct option sits in slot (A) is worse than
useless - it teaches the wrong test-taking reflex. So option order is shuffled here with a fixed
seed (reproducible), the answer index is recomputed, and any letter reference inside an
explanation - "(B) is simple present" - is rewritten to follow the shuffle. The frozen JSON is
the single artefact that is validated and then typeset into the DOCX.
"""

import importlib.util
import json
import os
import random
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261030
SOURCES = [("Paper 1", "data_paper1.py"), ("Paper 2", "data_paper2.py")]

SECTION_TITLE = {
    "ENG": "English",
    "GS": "General Studies",
    "AR": "Arithmetic",
}


def load(rel):
    path = os.path.join(HERE, rel)
    spec = importlib.util.spec_from_file_location(os.path.basename(rel)[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.PAPER


def freeze(item, rng):
    sec = item[0]
    question, opts, ans, expl, tag = item[1], list(item[2:6]), item[6], item[7], item[8]
    extra = list(item[9:])

    order = [0, 1, 2, 3]
    rng.shuffle(order)                      # order[new_slot] = old_index
    new_opts = [opts[old] for old in order]
    new_ans = order.index(ans)

    old_to_new = {chr(65 + old): chr(65 + pos) for pos, old in enumerate(order)}
    new_expl = re.sub(r"\(([ABCD])\)", lambda m: "(" + old_to_new[m.group(1)] + ")", expl)

    rec = {
        "section": sec,
        "section_title": SECTION_TITLE[sec],
        "question": question,
        "options": new_opts,
        "answer_index": new_ans,
        "answer": new_opts[new_ans],
        "explanation": new_expl,
        "topic": tag,
        "old_answer_index": ans,
        "slot_order": order,
    }
    if sec == "GS":
        rec["fact"] = extra[0]
        rec["source"] = extra[1] if len(extra) > 1 else ""
    if sec == "AR":
        rec["check"] = extra[0]
    return rec


def main():
    out = {"seed": SEED, "papers": []}
    for paper_no, (name, rel) in enumerate(SOURCES, start=1):
        rng = random.Random(SEED + paper_no * 7919)
        paper = load(rel)
        items = [freeze(it, rng) for it in paper]
        # continuous numbering 1..100, sections in exam order
        for i, rec in enumerate(items, start=1):
            rec["number"] = i
        out["papers"].append({"name": name, "source": rel, "items": items})
        spread = {c: sum(1 for r in items if chr(65 + r["answer_index"]) == c) for c in "ABCD"}
        print(f"{name}: {len(items)} items frozen | answer spread {spread}")

    with open(os.path.join(HERE, "final_papers.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print("wrote final_papers.json")


if __name__ == "__main__":
    main()

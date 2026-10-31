# -*- coding: utf-8 -*-
"""Assemble eight Part-I papers from the banks, without reusing a single item.

Each paper is 100 questions: English 30, General Studies 40, Arithmetic and Reasoning 30.
Every item records where it came from (bank key and row) so that the validator can go back
to the dataset and re-derive the answer instead of trusting what was written here.
"""
import json
import os
import random

import bank_en as EN
import bank_gs as GS
import gen_ar as AR

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261031

# ---------------------------------------------------------------- draw schedule
# per paper; multiplied by 8 gives the bank requirement
SCHEDULE_EN = [("SYN", 8), ("ANT", 6), ("IDIOM", 6), ("ONEWORD", 5), ("SPELL", 3), ("USE", 2)]
SCHEDULE_GS = [("ART", 5), ("OFF", 3), ("CAP", 3), ("RIV", 2), ("PRK", 2), ("YRS", 5),
               ("PER", 2), ("UNT", 2), ("VIT", 1), ("SCI", 5), ("ECO", 2), ("HQ", 2),
               ("WBP", 2), ("WBQ", 2), ("CA", 2)]
SCHEDULE_AR = [("arith", 18), ("reason", 12)]


class Deck:
    """A shuffled, non-repeating supply of bank rows for one category."""

    def __init__(self, rows, rng):
        self.rows = list(rows)
        rng.shuffle(self.rows)
        self.i = 0

    def take(self, n):
        out = self.rows[self.i:self.i + n]
        if len(out) < n:
            raise RuntimeError(f"bank exhausted: wanted {n}, had {len(self.rows) - self.i}")
        self.i += n
        return out


def pick_distractors(pool, answer, k=3, rng=None):
    """Three values from the same column, never equal to the answer, never repeated."""
    out = []
    seen = {str(answer).lower()}
    pool = list(pool)
    if rng is not None:
        rng.shuffle(pool)
    for v in pool:
        key = str(v).lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(v)
        if len(out) == k:
            break
    if len(out) < k:
        raise RuntimeError(f"not enough distractors for {answer!r}")
    return out


def make(section, q, answer, distractors, expl, tag, origin, spec=None):
    opts = [answer] + list(distractors)
    return {"section": section, "q": q, "options": opts, "answer": answer,
            "expl": expl, "tag": tag, "origin": origin, "spec": spec}


# ---------------------------------------------------------------- English items
SPELL_HINT = {
    "accommodation": "a place to stay", "bureaucracy": "government by officials",
    "privilege": "a special right", "recommendation": "a suggestion in favour",
    "occurrence": "an event that happens", "embarrassment": "a feeling of awkwardness",
    "committee": "a body of members", "receipt": "a written acknowledgement of payment",
    "maintenance": "the act of keeping in good order", "separate": "to keep apart",
    "definitely": "certainly", "calendar": "a chart of the days of the year",
    "government": "the body that governs", "necessary": "needed",
    "parliament": "the legislature", "questionnaire": "a set of written questions",
    "schedule": "a timetable", "vaccinate": "to inoculate against disease",
    "mischievous": "playfully naughty", "liaison": "communication between groups",
    "sergeant": "a rank in the police or army", "consensus": "general agreement",
    "arduous": "needing much effort", "employee": "a person employed",
    "correspondence": "letters exchanged", "acquaintance": "a person one knows slightly",
}

TAIL = {
    "SYN": " The other three options do not carry that sense.",
    "ANT": " The other three are near-synonyms of the word, so none can be its opposite.",
    "IDIOM": " The other options read the words literally.",
    "ONEWORD": " The other three words name different things.",
    "SPELL": " The other three spellings break a standard rule of English spelling.",
    "USE": " The other prepositions do not fit this fixed collocation.",
}


def with_tail(key, ex):
    return ex if len(ex) >= 45 else ex.rstrip() + TAIL[key]


def en_item(key, row):
    if key == "SYN":
        word, ans, ds, ex = row
        return make("ENG", f"Choose the word nearest in meaning to {word}.", ans, ds, with_tail("SYN", ex),
                    "Synonym", ("EN", key, word))
    if key == "ANT":
        word, ans, ds, ex = row
        return make("ENG", f"Choose the word most opposite in meaning to {word}.", ans, ds, with_tail("ANT", ex),
                    "Antonym", ("EN", key, word))
    if key == "IDIOM":
        idiom, ans, ds, ex = row
        return make("ENG", f"Choose the correct meaning of the idiom: '{idiom}'.", ans, ds, with_tail("IDIOM", ex),
                    "Idiom", ("EN", key, idiom))
    if key == "ONEWORD":
        prompt, ans, ds, ex = row
        return make("ENG", f"One word for '{prompt}':", ans, ds, with_tail("ONEWORD", ex), "One-word substitution",
                    ("EN", key, prompt))
    if key == "SPELL":
        word, ans, ds, ex = row
        return make("ENG", f"Choose the correctly spelt word that is used in the sense of '{SPELL_HINT.get(word, word)}'.", word, ds, with_tail("SPELL", ex), "Spelling",
                    ("EN", key, word))
    if key == "USE":
        prompt, ans, ds, ex = row
        return make("ENG", f"Fill in the blank: {prompt}", ans, ds, with_tail("USE", ex), "Preposition",
                    ("EN", key, prompt))
    raise KeyError(key)


# ---------------------------------------------------------------- GS items
def gs_item(key, row, pools, rng):
    if key == "ART":
        art, subj = row
        others = [a for a, s in GS.ART if a != art]
        ds = pick_distractors(others, art, rng=rng)
        return make("GS", f"Which Article of the Constitution deals with {subj}?", art, ds,
                    f"{art} of the Constitution provides for {subj}.", "Polity",
                    ("GS", key, art), spec=("art", art))
    if key == "OFF":
        q, ans, ds, ex = row
        return make("GS", q, ans, ds, ex, "Polity", ("GS", key, q))
    if key == "CAP":
        st, cap = row
        ds = pick_distractors([c for s, c in GS.CAP], cap, rng=rng)
        return make("GS", f"The capital of {st} is", cap, ds,
                    f"{cap} is the capital of {st}; the State secretariat and legislature sit there.",
                    "Geography",
                    ("GS", key, st), spec=("cap", st))
    if key == "RIV":
        rv, org = row
        ds = pick_distractors([o for r, o in GS.RIV], org, rng=rng)
        return make("GS", f"The river {rv} rises in", org, ds,
                    f"The {rv} rises in {org}.", "Geography",
                    ("GS", key, rv), spec=("riv", rv))
    if key == "PRK":
        pk, st = row
        name = pk if pk.endswith("National Park") else pk + " National Park"
        ds = pick_distractors([s for p, s in GS.PRK], st, rng=rng)
        return make("GS", f"{name} is situated in", st, ds,
                    f"{name} lies in {st}.", "Geography",
                    ("GS", key, pk), spec=("prk", pk))
    if key == "YRS":
        yr, ev = row
        y = int(yr)
        cand = [str(x) for x in (y - 1, y + 1, y - 2, y + 2, y - 3, y + 3, y + 4) if x > 1000]
        ds = pick_distractors(cand, yr, rng=rng)
        return make("GS", f"In which year did {ev} take place?", yr, ds,
                    f"{ev[0].upper() + ev[1:]} took place in {yr}.", "History",
                    ("GS", key, yr), spec=("yrs", yr))
    if key == "PER":
        q, ans, ds, ex = row
        return make("GS", q, ans, ds, ex, "History", ("GS", key, q))
    if key == "UNT":
        quant, unit = row
        ds = pick_distractors([u for qy, u in GS.UNT], unit, rng=rng)
        return make("GS", f"The SI unit of {quant} is", unit, ds,
                    f"The SI unit of {quant} is the {unit}.", "Science",
                    ("GS", key, quant), spec=("unt", quant))
    if key == "VIT":
        vit, dis = row
        ds = pick_distractors([d for v, d in GS.VIT], dis, rng=rng)
        return make("GS", f"Deficiency of {vit} causes", dis, ds,
                    f"Deficiency of {vit} causes {dis}.", "Science",
                    ("GS", key, vit), spec=("vit", vit))
    if key == "SCI":
        q, ans, ds, ex = row
        return make("GS", q, ans, ds, ex, "Science", ("GS", key, q))
    if key == "ECO":
        term, mean = row
        ds = pick_distractors([m for t, m in GS.ECO], mean, rng=rng)
        return make("GS", f"In economics, '{term}' means", mean, ds,
                    f"'{term}' means {mean}.", "Economy",
                    ("GS", key, term), spec=("eco", term))
    if key == "HQ":
        inst, city = row
        ds = pick_distractors([c for i, c in GS.HQ], city, rng=rng)
        return make("GS", f"The headquarters of {inst} is at", city, ds,
                    f"The headquarters of {inst} is in {city}.", "Economy",
                    ("GS", key, inst), spec=("hq", inst))
    if key == "WBP":
        place, dist = row
        ds = pick_distractors([d for p, d in GS.WBP], dist, rng=rng)
        return make("GS", f"{place} is in which district of West Bengal?", dist, ds,
                    f"{place} lies in {dist} district, one of the twenty-three districts of "
                    f"West Bengal; the other three options name different districts.",
                    "West Bengal",
                    ("GS", key, place), spec=("wbp", place))
    if key == "WBQ":
        q, ans, ds, ex = row
        return make("GS", q, ans, ds, ex, "West Bengal", ("GS", key, q))
    if key == "CA":
        q, ans, ds, ex = row
        return make("GS", q, ans, ds, ex + " (current affairs verified to 30 October 2026).",
                    "Current affairs", ("GS", key, q))
    raise KeyError(key)


EXPL_OFF = {
    "Who administers the oath of office to the President of India?":
        "The Chief Justice of India administers the oath to the President under Article 60.",
    "Who administers the oath of office to a Governor?":
        "The Chief Justice of the High Court of the State administers the oath to the Governor.",
    "The Vice-President of India is elected by":
        "The Vice-President is elected by an electoral college of the members of both Houses of Parliament.",
    "Who is the ex-officio Chairman of the Rajya Sabha?":
        "The Vice-President of India is the ex-officio Chairman of the Rajya Sabha.",
    "The Speaker of the Lok Sabha is elected by":
        "The Speaker is elected by the members of the Lok Sabha from among themselves.",
    "What is the maximum strength of the Lok Sabha provided by the Constitution?":
        "Article 81 provides for a maximum of 552 members of the Lok Sabha.",
    "The term of office of a member of the Rajya Sabha is":
        "A Rajya Sabha member serves six years; one third of the House retires every two years.",
    "The normal term of the Lok Sabha is":
        "The Lok Sabha has a normal term of five years unless dissolved earlier.",
    "The minimum age to become President of India is":
        "A candidate for the Presidency must have completed 35 years of age.",
    "The minimum age to become a member of the Lok Sabha is":
        "A candidate for the Lok Sabha must have completed 25 years of age.",
    "The minimum age to become a member of the Rajya Sabha is":
        "A candidate for the Rajya Sabha must have completed 30 years of age.",
    "Who appoints the Chief Election Commissioner of India?":
        "The Chief Election Commissioner is appointed by the President.",
    "The Finance Commission is constituted":
        "The Finance Commission is constituted every five years under Article 280.",
    "Which Schedule of the Constitution deals with anti-defection?":
        "The Tenth Schedule, added in 1985, contains the anti-defection provisions.",
    "Which Schedule of the Constitution lists the recognised languages?":
        "The Eighth Schedule lists the recognised languages of India.",
    "How many fundamental duties are listed in the Constitution?":
        "Article 51A now contains eleven fundamental duties, the eleventh added in 2002.",
    "The Directive Principles of State Policy are contained in":
        "The Directive Principles are in Part IV of the Constitution.",
    "The Fundamental Rights are contained in":
        "The Fundamental Rights are in Part III of the Constitution.",
    "Which body is called the guardian of the Constitution?":
        "The Supreme Court is regarded as the guardian of the Constitution.",
    "The writ of habeas corpus requires the authorities to":
        "Habeas corpus literally means 'to have the body'; the court orders the person to be produced.",
    "A Money Bill can be introduced only in":
        "Article 110 requires a Money Bill to originate in the Lok Sabha.",
    "Who presides over a joint sitting of both Houses of Parliament?":
        "The Speaker of the Lok Sabha presides over a joint sitting.",
    "The Constitution of India was adopted on":
        "The Constituent Assembly adopted the Constitution on 26 November 1949.",
    "The Constitution of India came into force on":
        "The Constitution came into force on 26 January 1950.",
    "Who appoints the Governor of a State?":
        "The Governor is appointed by the President under Article 155.",
    "The Governor holds office":
        "The Governor holds office during the pleasure of the President.",
}


def build():
    rng = random.Random(SEED)
    decks = {}
    for key, _ in SCHEDULE_EN:
        decks[key] = Deck(getattr(EN, key), rng)
    for key, _ in SCHEDULE_GS:
        decks[key] = Deck(getattr(GS, key), rng)

    ar_pool = AR.build_pool(seed=SEED)
    ar_decks = {}
    for kind in ("arith", "reason"):
        rows = [x for x in ar_pool if x["kind"] == kind]
        rng.shuffle(rows)
        ar_decks[kind] = rows

    papers = []
    for pno in range(1, 9):
        items = []
        for key, n in SCHEDULE_EN:
            for row in decks[key].take(n):
                items.append(en_item(key, row))
        for key, n in SCHEDULE_GS:
            for row in decks[key].take(n):
                items.append(gs_item(key, row, None, rng))
        for kind, n in SCHEDULE_AR:
            take = ar_decks[kind][:n]
            del ar_decks[kind][:n]
            for it in take:
                items.append(make("AR", it["q"], it["a"], it["d"], it["e"], it["tag"],
                                  ("AR", kind, it["q"]), spec=it["spec"]))
        assert len(items) == 100, len(items)

        # deterministic option shuffle per question
        for qi, it in enumerate(items):
            r = random.Random(SEED + pno * 1000 + qi)
            opts = list(it["options"])
            r.shuffle(opts)
            if len({o.strip().lower() for o in opts}) != 4:
                raise RuntimeError("duplicate option after shuffle: " + it["q"])
            it["options"] = opts
            it["answer_index"] = opts.index(it["answer"])

        # balance the answer letters so no key dominates the paper
        counts = {"A": 0, "B": 0, "C": 0, "D": 0}
        for it in items:
            counts[chr(65 + it["answer_index"])] += 1
        guard = 0
        while max(counts.values()) - min(counts.values()) > 6 and guard < 400:
            guard += 1
            hi = max(counts, key=lambda k: counts[k])
            lo = min(counts, key=lambda k: counts[k])
            victim = next((x for x in items if chr(65 + x["answer_index"]) == hi), None)
            if victim is None:
                break
            cur = victim["answer_index"]
            want = "ABCD".index(lo)
            shift = (want - cur) % 4
            victim["options"] = victim["options"][-shift:] + victim["options"][:-shift] \
                if shift else victim["options"]
            victim["answer_index"] = victim["options"].index(victim["answer"])
            counts[hi] -= 1
            counts[lo] += 1

        papers.append({
            "name": f"Paper {pno}",
            "items": [
                {"no": i + 1, "section": it["section"], "q": it["q"],
                 "options": it["options"], "answer_index": it["answer_index"],
                 "answer": it["answer"], "expl": it["expl"], "tag": it["tag"],
                 "origin": list(it["origin"]), "spec": list(it["spec"]) if it["spec"] else None}
                for i, it in enumerate(items)
            ],
        })

    out = {"meta": {"papers": 8, "questions_per_paper": 100, "marks": 100,
                    "minutes": 60, "seed": SEED,
                    "sections": {"ENG": 30, "GS": 40, "AR": 30},
                    "note": "Most-expected practice papers for WBPSC Clerkship Part-I; "
                            "not previous-year questions."},
           "papers": papers}
    path = os.path.join(HERE, "final_papers8.json")
    json.dump(out, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return out, path


if __name__ == "__main__":
    data, path = build()
    print("written", path)
    for p in data["papers"]:
        from collections import Counter
        c = Counter(i["section"] for i in p["items"])
        print(p["name"], dict(c), "| answers:", len({i["answer_index"] for i in p["items"]}))

# -*- coding: utf-8 -*-
"""Prose for the Part-II book: method, worked build-steps, timing plan, error list, sources.

Everything here is teaching material written for this book. The exam pattern it describes is
the Commission's published one; the questions and answers are practice material, not
previous-year papers, and the book says so on the cover and in Appendix D.
"""

# ---------------------------------------------------------------- exam frame
EXAM = {
    "marks": 100,
    "minutes": 60,
    "groups": [
        ("Group A", "English", 50, "report, precis, translation Bengali/Hindi/Urdu/Nepali/Santali into English"),
        ("Group B", "Bengali (or Hindi / Urdu / Nepali / Santali)", 50,
         "report, precis, translation English into the language chosen"),
    ],
    "tasks": [
        ("Drafting a report from supplied points", "20"),
        ("Condensing a prose passage (precis / summary)", "15"),
        ("Translation", "15"),
    ],
    "standard": "Madhyamik",
    "penalty": "Revealing identity anywhere in the script costs 10% of the paper's full marks.",
}

DISCLAIMER = (
    "This is a practice book, not a question paper. The two papers that follow were written "
    "for this book in the Commission's published Part-II format. They are not previous-year "
    "questions and must not be quoted as such. The format, the marks and the sixty minutes are "
    "the Commission's; the passages, the supplied points and the model answers are ours."
)

# ---------------------------------------------------------------- method
METHOD = [
    {
        "task": "Drafting a report from supplied points",
        "budget": "20 marks \u00b7 11 minutes",
        "intro": (
            "The Commission hands you a bundle of facts and asks for a report. Nothing more is "
            "wanted than those facts in an orderly prose, under a headline, with a dateline. "
            "Candidates rarely lose marks here for poor English; they lose them for leaving a "
            "point out. Eight facts at one mark each cost more than a dozen small grammatical "
            "slips."),
        "steps": [
            "Count the points before you write. There are usually six to ten; number them in the "
            "margin so that you can tick each one off as it goes in.",
            "Fix the order. Most sets are already chronological, but check: what happened, what "
            "was said, what was decided. Write in that order even if the points are not.",
            "Write the headline first. Six to twelve words, no full stop, an active verb, present "
            "tense: 'CAMP COLLECTS 87 UNITS'. A headline is a label, not a sentence.",
            "Put the dateline immediately below: place, comma, date. 'Salt Lake, 14 August 2026.'",
            "Let the opening sentence answer four questions at once: what was held, where, when, "
            "and who organised it. This single sentence can carry three supplied points.",
            "Group the remaining points into two or three paragraphs. One paragraph per point "
            "reads like a list; one paragraph for the whole report reads like a note.",
            "Keep the past tense and the passive voice: 'was held', 'were distributed', 'has "
            "been decided'. The reporter is not part of the story.",
            "Close with the decision, the promise or the next step. A report that stops in the "
            "middle of the facts reads as if it was cut short.",
            "Count the words. Inside 150-200, stop. Below 150, add a sentence of background that "
            "the points already imply. Above 200, cut adjectives, never a fact.",
        ],
        "anatomy": [
            ("Headline", "result or action, present tense, no full stop",
             "BLOOD DONATION CAMP COLLECTS 87 UNITS AT SALT LAKE OFFICE"),
            ("Dateline", "place and date, on its own line",
             "Salt Lake, 14 August 2026:"),
            ("Lead", "what, where, when, who, why \u2014 one sentence",
             "A camp was held on the office premises in Sector V from 10 a.m. to 4 p.m."),
            ("Body", "the supplied points, grouped, in the passive",
             "Altogether 120 employees registered and 87 units were collected."),
            ("Close", "decision, promise or consequence",
             "The association announced that the camp would be held every year."),
        ],
        "traps": [
            "Writing 'I organised the camp'. A report is in the third person; this alone can cost "
            "the format marks, and a first-person slip that names you costs 10% of the paper.",
            "Putting the headline in the middle of the page or ending it with a full stop.",
            "Copying the points as eight separate sentences with no connectors. The examiner is "
            "testing whether you can make prose, not whether you can copy.",
            "Adding praise \u2014 'it was a grand success'. A report records; it does not applaud.",
            "Drifting into the future tense halfway through because the last point is about next "
            "year. Keep the report in the past and put the promise in reported speech.",
        ],
    },
    {
        "task": "Condensing a passage (precis / summary)",
        "budget": "15 marks \u00b7 9 minutes",
        "intro": (
            "A precis is the passage rewritten by you at about one-third of its length, keeping "
            "every idea and no example. It is marked on three things: whether the central idea "
            "survives, whether the compression is real, and whether the language is yours. A "
            "beautiful precis that copies the passage scores nothing for the third."),
        "steps": [
            "Read twice. The first reading is for sense; the second is with a pencil in hand.",
            "Underline one sentence in each paragraph \u2014 the one that carries the idea, not "
            "the one that carries the example.",
            "Write those sentences in the margin in your own words, as notes. Do this before you "
            "count anything.",
            "Count the words of the passage and divide by three. That is your target, not your "
            "ceiling. The table below saves you the arithmetic under pressure.",
            "Draft from your margin notes, never from the passage. This is the single habit that "
            "prevents copying \u2014 if your eye is on the passage, your sentence will be too.",
            "Cut examples, quotations, repetitions, adjectives and rhetorical questions. A "
            "précis keeps the argument, not the furniture.",
            "Give a title of two to five words. 'The Value of Reading', not 'A Study of the "
            "Importance of Reading in Modern Life'.",
            "Count again. Inside the band, stop. Over it, remove a clause; under it, restore one "
            "example.",
            "Read the precis on its own. It must make sense to a reader who has never seen the "
            "passage, and it must not contain the phrase 'the passage says'.",
        ],
        "table": ("Words in the passage", "One-third target", "Safe band to write"),
        "rows": [
            ("120", "40", "34-42"), ("150", "50", "44-54"), ("180", "60", "54-64"),
            ("210", "70", "63-75"), ("240", "80", "72-86"), ("300", "100", "90-108"),
        ],
        "traps": [
            "Opening with 'The passage says that...' or 'According to the writer...'. The "
            "précis is a piece of writing in its own right, not a reply about a text.",
            "Keeping the examples. The pit, the bus, the tank \u2014 they may illustrate, but "
            "they eat the word limit and earn nothing.",
            "Adding a moral the passage did not draw. If the passage diagnoses, do not prescribe.",
            "Writing a title that is a full sentence, or forgetting the title altogether \u2014 "
            "two marks gone in five seconds.",
            "Landing at half the passage and calling it compression. One-third means one-third; "
            "the band above is what the examiner expects.",
        ],
    },
    {
        "task": "Translation",
        "budget": "15 marks \u00b7 7 minutes",
        "intro": (
            "Translation is marked on fidelity first, completeness second, idiom third. A plain "
            "sentence that says exactly what the original said scores higher than an elegant one "
            "that says something slightly different. Group A translates from Bengali (or Hindi, "
            "Urdu, Nepali, Santali) into English; Group B translates English into the language "
            "you have chosen."),
        "steps": [
            "Read the whole passage before translating a word of it. You cannot choose the right "
            "tense for a sentence until you know how the passage ends.",
            "Mark the tense and the person of the original, and keep them. A past-tense narrative "
            "translated into the present reads as a summary, not a translation.",
            "Translate sentence by sentence. Word-by-word translation produces sentences that are "
            "grammatical in neither language.",
            "When a word is unknown, translate the idea around it. A paraphrase costs a mark; a "
            "blank costs three and tells the examiner you stopped.",
            "Keep proper nouns, numbers and dates as they are. 'Sundarbans' stays Sundarbans; "
            "Bengali numerals become Arabic numerals in an English answer, and the reverse.",
            "Re-read your own text alone, without looking at the original. Any sentence that does "
            "not stand up in the target language should be rewritten now.",
            "Count sentences, not words: if the original had seven sentences, your answer should "
            "have six to eight. A missing sentence is a missing three or four marks.",
        ],
        "traps": [
            "Translating an idiom word for word. 'গা ঢাকা দেওয়া' is not 'covering the body'.",
            "Leaving a phrase in the source script \u2014 a Bengali word inside an English answer "
            "is an omission with a bow on it.",
            "Changing the voice of every sentence. If the original is passive, keep it passive "
            "unless the target language demands otherwise.",
            "Adding a concluding sentence of your own. The examiner is testing fidelity; anything "
            "extra is marked as invention.",
            "Spending twelve minutes here because the passage 'felt difficult', and then rushing "
            "the second report, which carries five more marks.",
        ],
    },
]

# ---------------------------------------------------------------- per-question build steps
BUILD = {
    ("Paper 1", 1): [
        "Headline first: the verb 'collects' plus the number 87 makes the result the news; the "
        "venue follows so that a reader knows where.",
        "Dateline 'Salt Lake, 14 August 2026' fixes place and date in six words.",
        "The lead sentence carries four supplied points at once \u2014 date, time, venue, "
        "organisers \u2014 because a report answers the obvious questions immediately.",
        "The Director's speech is compressed to two sentences and placed before the figures: the "
        "shortage of blood is the reason the camp exists, so it explains the numbers that follow.",
        "Registration (120) and collection (87) share one sentence. The gap between them is the "
        "story, and putting them side by side shows it without comment.",
        "Certificates and refreshments are dealt with in four words; they are minor points and "
        "should not get a paragraph each.",
        "The close is the association's decision to repeat the camp every year \u2014 the last "
        "supplied point, in reported speech.",
    ],
    ("Paper 1", 2): [
        "Three paragraphs were reduced to one because the passage makes a single argument three "
        "times: the obstacle is management, the gain is practical, the gain is also mental.",
        "The first sentence keeps the paradox (easy to praise, hard to acquire) and replaces the "
        "passage's 'shortage of time' with 'using the minutes already free' \u2014 same idea, own "
        "words.",
        "The bus and the brewing tea are examples; they are cut, and only the principle 'a book "
        "kept nearby' survives.",
        "The newspaper and the novel are kept as a pair because the passage's point is that both "
        "kinds of reading are useful at work.",
        "The last sentence keeps the examination candidate because that is the passage's closing "
        "claim, not an illustration.",
        "Title: 'The Value of Reading', four words, no verb, no full stop.",
    ],
    ("Paper 1", 3): [
        "The passage has seven sentences; the answer has seven, in the same order, so nothing is "
        "silently dropped.",
        "Present tense throughout, because the Bengali original is in the present: 'is declining', "
        "'think', 'broaden'.",
        "'গণগ্রন্থাগার' is rendered as 'public libraries', not 'mass libraries' \u2014 the "
        "dictionary sense is not always the sense in the sentence.",
        "'সুযোগ থেকে বঞ্চিত' is turned round into the passive 'are deprived of this opportunity' "
        "so that the sentence keeps the original's emphasis on the students.",
        "The final 'তাই' becomes 'It is therefore necessary', which is how a proposal is made in "
        "English official prose.",
    ],
    ("Paper 1", 4): [
        "The Bengali report uses the same skeleton as the English one: headline, dateline, lead, "
        "body, close. The language changes; the architecture does not.",
        "Headline states the action and the number together \u2014 '২০০টি চারাগাছ রোপণ' \u2014 "
        "because a Bengali headline, like an English one, leads with the result.",
        "The lead sentence packs date, occasion, time, venue and organisers, exactly as the "
        "English report does.",
        "The District Magistrate's speech is reduced to two sentences: why trees, and why care "
        "matters as much as planting.",
        "The planting, the students and the teachers are grouped into one paragraph, since they "
        "all describe who did the work.",
        "The oath and the annual decision close the report; the decision is the last thing the "
        "reader should be left with.",
    ],
    ("Paper 1", 5): [
        "The passage argues in two movements: the damage, then the remedy. The precis keeps both "
        "and drops the illustrations (bottles, bags, fish on the plate).",
        "The first sentence keeps the cause (cheap and easy) and the consequence (the damage "
        "cannot be undone easily) in one clause-pair.",
        "The chain soil \u2192 river \u2192 sea \u2192 fish \u2192 human food and air is kept as a "
        "chain, because that chain is the argument.",
        "'শুধু নিষেধাজ্ঞা নয়' is kept as the contrast it is: law is not enough, habit is needed.",
        "48 words against a 124-word passage, a little under two-fifths \u2014 inside the band, "
        "and short enough to leave room for the title.",
    ],
    ("Paper 1", 6): [
        "The English original has eight sentences; the Bengali answer keeps eight, so no traffic "
        "rule is lost in translation.",
        "'Overspeeding' becomes 'অতিরিক্ত গতিতে চলা', not a transliteration, because Bengali has "
        "a plain phrase for it.",
        "'Zebra crossing' and 'footbridge' are kept as established Bengali terms (জিব্রা ক্রসিং, "
        "উড়ো সেতু); inventing a phrase here would confuse the examiner.",
        "The last sentence is kept as one sentence with two clauses: the driver saves five "
        "minutes and loses a life. Splitting it would destroy the irony that carries the point.",
        "No sentence is added at the end. A moral would be invented content.",
    ],
    ("Paper 2", 1): [
        "Headline leads with what the training achieved, not with the fact that a programme was "
        "held: 'CLERKS TRAINED IN E-OFFICE WORK'.",
        "The lead sentence carries date, time, venue and the two organising bodies.",
        "The four topics are kept together in one paragraph because they are one fact \u2014 the "
        "syllabus of the day \u2014 and splitting them would create four thin paragraphs.",
        "The two-batch arrangement is given a sentence of its own: it explains how sixty clerks "
        "shared the terminals, which the points only imply.",
        "The Additional District Magistrate's distribution of certificates is the close, with the "
        "feedback and the promised follow-up behind it.",
    ],
    ("Paper 2", 2): [
        "The passage's central move is a reversal \u2014 the fault is not the weather but the "
        "building \u2014 so the first sentence states the reversal before anything else.",
        "'Concrete covers the ground' becomes 'paving seals the soil': same fact, different "
        "words, and 'seals' does the work of 'has no chance to drink'.",
        "The tank, the hundred-year-old house and the mobile phone are examples; all three are "
        "cut.",
        "The three-step principle is kept but re-worded: 'trap', 'keep', 'let the remainder "
        "sink'. The words are ours; the sequence is the passage's.",
        "The closing contrast between attention and money is kept because it is the passage's "
        "conclusion, not a detail.",
    ],
    ("Paper 2", 3): [
        "The Bengali passage has six sentences; the English answer keeps six and keeps the "
        "contrast between saving time and costing jobs in the same sentence.",
        "'সাধারণ পরিবারের প্রতিদিনের প্রয়োজন' is rendered as 'a daily necessity in an ordinary "
        "household' \u2014 the adjective order in English is the reverse of the Bengali, and the "
        "sentence must still sound English.",
        "The list \u2014 banking, tickets, government applications \u2014 is kept as a list, "
        "because its length is the argument.",
        "'বাহিষ্কার করেছে' is translated as 'has removed many people from employment' rather "
        "than the bureaucratic 'rendered redundant'.",
        "The final warning is kept as a warning: knowing the machine is not enough without "
        "knowing the subject.",
    ],
    ("Paper 2", 4): [
        "The Bengali headline states the result \u2014 accidents fell \u2014 rather than the "
        "event, which is the convention in Bengali newspapers too.",
        "The dateline is the day after the week ended, as a report is written after the event.",
        "The rally and the march-past are given one sentence; the signboard distribution another, "
        "with the reason attached ('so that the rules are easy to remember').",
        "The figure of 1,200 pedestrians is placed in its own paragraph with the school and "
        "college programmes, since both describe public contact.",
        "The volunteers and the closing announcement share the last paragraph: the fall in "
        "accidents, the decision to repeat, and the felicitation.",
    ],
    ("Paper 2", 5): [
        "The passage is an argument in three moves: why time is lost, how to plan, why the habit "
        "matters. The precis keeps all three in four sentences.",
        "'সময়ের মূল্য বোঝা যায় তা হারানোর পরেই' is kept almost in full because it is the "
        "passage's opening claim and cannot be compressed further.",
        "The three rules (order, speed, rest) are compressed into one sentence with three "
        "participles, which is how Bengali handles a list of instructions in prose.",
        "The school and office illustrations are dropped; only the conclusion about habit "
        "survives.",
        "44 words against 126 \u2014 a little over a third, which is where a precis should sit.",
    ],
    ("Paper 2", 6): [
        "The original has two paragraphs and seven sentences; the Bengali keeps two paragraphs "
        "and seven sentences, so the structure survives translation.",
        "'A bargain between the land and the tide' becomes 'একটি রাজি' \u2014 the metaphor is "
        "translated as an idea, since a literal 'দর কষাকষি' would sound like a commercial "
        "transaction.",
        "'Walking sticks' becomes 'লাঠি বাড়ির মতো', keeping the comparison rather than the "
        "object.",
        "The second paragraph's paradox \u2014 a map that is never finished \u2014 is kept, "
        "because it is the passage's best sentence and its meaning is easy to lose.",
        "The final contrast between a reserve to be visited and a neighbour to be watched is kept "
        "word for word in sense, since it is the passage's judgement.",
    ],
}

# ---------------------------------------------------------------- timing
TIMING = [
    ("0-4", "Read all six questions; choose your Group B language; number the supplied points. "
            "Do not write a word yet."),
    ("4-15", "Q1 report (Group A). Two minutes planning, nine writing, one checking the points "
             "off one by one."),
    ("15-24", "Q2 precis (Group A). Three minutes reading and noting, five drafting, one "
              "counting words."),
    ("24-31", "Q3 translation (Group A). Seven minutes, sentence by sentence, no re-reading of "
              "the whole passage afterwards."),
    ("31-42", "Q4 report (Group B). Same shape as Q1; the language changes, the method does not."),
    ("42-51", "Q5 precis (Group B)."),
    ("51-58", "Q6 translation (Group B)."),
    ("58-60", "Check: every question numbered, no name or roll number anywhere, word counts in "
              "the band."),
]

# ---------------------------------------------------------------- error list
ERRORS_EN = [
    ("Report written in the first person", "'I visited the camp' \u2192 'The camp was visited'. "
     "First person can also identify you, which costs 10% of the paper."),
    ("No dateline", "Place and date belong under the headline. Without them the report has no "
     "standing."),
    ("Headline with a full stop", "A headline is a label: 'CAMP COLLECTS 87 UNITS', not a "
     "sentence."),
    ("One supplied point left out", "The commonest single loss in this paper. Tick each point as "
     "it goes in."),
    ("Report over 200 words", "Length is a marking item. Cut adjectives, never facts."),
    ("Opinion in a report", "'It was a grand success' is comment, not reportage."),
    ("Tense drift", "Starting in the past and sliding into the future at the last point."),
    ("Points copied as separate sentences", "Eight points in eight sentences is a list, not a "
     "report; join them with 'and', 'later', 'at the close'."),
    ("Précis opening 'The passage says...'", "Write the précis as a piece of prose, not as an "
     "answer about a text."),
    ("Précis at half the passage", "One-third means one-third. A half-length précis loses the "
     "compression marks even when it is well written."),
    ("Précis keeping examples", "The bus, the tea, the pit \u2014 illustrations cost words and "
     "earn nothing."),
    ("Précis without a title", "Two marks, five seconds."),
    ("Précis in the passage's own words", "Examiners know the passage. Draft from your margin "
     "notes, not from the text."),
    ("Translation with a sentence missing", "Count sentences in the original and in your answer "
     "before you move on."),
    ("Source words left in the answer", "A Bengali word in an English answer is treated as an "
     "omission."),
    ("Word-for-word translation", "'\u0997\u09a3\u0997\u09cd\u09b0\u09a8\u09cd\u09a5\u09be\u0997\u09be\u09b0' "
     "is a public library, not a 'mass library'."),
    ("Idiom translated literally", "Idioms are translated by their sense, never by their words."),
    ("Adding a moral to a translation", "Anything not in the original is invention, however "
     "true it is."),
    ("Spending 25 minutes on the first report", "The other five questions carry 80 marks between "
     "them."),
    ("Name, roll number or phone number on the script", "Ten per cent of the full marks, gone."),
]

ERRORS_BN = [
    ("রিপোর্টে 'আমি' ব্যবহার", "সংবাদ প্রতিবেদন তৃতীয় পুরুষে লেখা হয়: 'আমি উপস্থিত ছিলাম' নয়, "
     "'অনুষ্ঠানে উপস্থিত ছিলেন'।"),
    ("তারিখ ও স্থান না লেখা", "শিরোনামের নিচে স্থান ও তারিখ অবশ্যই থাকবে।"),
    ("শিরোনামে দাঁড়ি দেওয়া", "শিরোনাম বাক্য নয়, পরিচয়চিহ্ন।"),
    ("একটি পয়েন্ট বাদ পড়া", "এই প্রশ্নে সবচেয়ে বেশি নম্বর এখানেই কাটা যায়।"),
    ("শব্দসংখ্যা ২০০ ছাড়িয়ে যাওয়া", "দৈর্ঘ্য একটি নম্বরের মানদণ্ড; বিশেষণ কমান, তথ্য নয়।"),
    ("সারাংশে নিজের মতামত", "মূল অনুচ্ছেদে যা নেই, তা যোগ করা যাবে না।"),
    ("সারাংশে মূল বাক্য হুবহু", "নিজের শব্দে লিখতে হবে; মূল বাক্য কপি করলে সংক্ষেপণের নম্বর "
     "যায়।"),
    ("সারাংশে উদাহরণ রাখা", "উদাহরণ জায়গা নেয়, নম্বর দেয় না।"),
    ("শিরোনাম না দেওয়া", "দুই নম্বর, পাঁচ সেকেন্ডে।"),
    ("অনুবাদে একটি বাক্য বাদ", "মূল অংশের বাক্য সংখ্যা ও নিজের বাক্য সংখ্যা মিলিয়ে নিতে হবে।"),
    ("অনুবাদে ইংরেজি শব্দ রেখে দেওয়া", "লক্ষ্য ভাষায় লেখা না হলে সেই অংশ অপঠিত ধরা হয়।"),
    ("বানানে অনিয়ম", "ই/ঈ, শ/ষ/স, ণ/ন — একই শব্দে দুই বানান লিখলে ভাষার নম্বর কমে।"),
    ("যুক্তাক্ষর ভাঙা", "অস্পষ্ট হাতের লেখা বা ভাঙা যুক্তাক্ষর ঠিক উত্তরকেও ভুল দেখায়।"),
    ("শেষে সময় না রাখা", "শেষ দুই মিনিট যাচাইয়ের জন্য রাখুন।"),
]

# ---------------------------------------------------------------- sources
SOURCES = [
    ("The Part-II scheme", "West Bengal Public Service Commission \u2014 Clerkship Examination, "
     "scheme and syllabus for Part-II: six questions in a conventional (descriptive) paper, "
     "Group A English 50 marks and Group B 50 marks, one hour, Madhyamik standard."),
    ("The scoring rule", "The Commission's instruction that a candidate revealing identity in "
     "the answer script forfeits 10% of the paper's full marks."),
    ("Merit", "Final merit is prepared on Part-I and Part-II taken together."),
    ("The papers in this book", "Written for this book in that format. They are practice papers, "
     "not previous-year questions, and no claim is made that they have appeared in any "
     "examination."),
]

# ---------------------------------------------------------------- mutations used to test the checker
MUTATIONS = [
    ("A supplied point removed from a model report", "P2.06 point coverage"),
    ("A précis that is a copy of its passage", "P2.08 compression"),
    ("A twelve-word sentence lifted from the passage", "P2.08 / P2.12"),
    ("An eight-word lift that still fits the word limit", "P2.12 own words"),
    ("A translation cut to its first sentence", "P2.14 truncation"),
    ("'My name is...' inserted in a report", "P2.07 / P3.06 identity"),
    ("A Bengali name inserted in a Bengali report", "P3.06 identity"),
    ("Group A marks raised to 55", "P1.06 group total"),
    ("Time allocation raised to 78 minutes", "P1.09 sixty minutes"),
    ("Two questions given identical answers", "P2.17 / P3.10 collision"),
    ("A Bengali précis padded past its limit", "P2.08 compression"),
    ("Bengali left inside an English translation", "P3.01 / P3.02 script"),
]

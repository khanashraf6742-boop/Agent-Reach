"""Expected paper 1 -- WBPSC Clerkship Part-I.

Format per entry:
  ENG: ("ENG", question, A, B, C, D, answer_index, explanation, tag)
  GS : ("GS",  question, A, B, C, D, answer_index, explanation, tag, fact, source)
  AR : ("AR",  question, A, B, C, D, answer_index, explanation, tag, check_expression)

`fact`   = canonical correct value; the validator requires it to appear in the marked
           option and in no other option.
`check`  = an independently evaluated Python expression that must reproduce the marked
           option numerically (see validate.py, pass 2).
"""

PAPER = [
    # ------------------------------------------------------------------ ENGLISH
    ("ENG", "Fill in the blank with the correct preposition: She is very good ____ mathematics.",
     "at", "in", "on", "for", 0,
     "'Good at' is the fixed collocation used for skill in a subject or activity (good at maths, "
     "good at chess). 'Good in' is used only for a field or a role, e.g. 'good in health'. "
     "Rule: adjective + at + skill.", "Preposition"),
    ("ENG", "Fill in the blank: The clerk was accused ____ accepting a bribe.",
     "of", "for", "with", "at", 0,
     "The verb 'accuse' always takes 'of': accuse somebody of something. The trap is the "
     "parallel pattern 'charge somebody with', which tempts candidates into writing 'accused "
     "with'. Rule: accused of / charged with.",
     "Preposition"),
    ("ENG", "Choose the word nearest in meaning to OBSTINATE.",
     "Stubborn", "Flexible", "Indifferent", "Generous", 0,
     "Obstinate = refusing to change one's opinion, i.e. stubborn. 'Flexible' and 'generous' are "
     "positive/neutral qualities, and 'indifferent' means unconcerned - none carries the idea of "
     "wilful refusal to change.", "Synonym"),
    ("ENG", "Choose the word most opposite in meaning to FRUGAL.",
     "Extravagant", "Thrifty", "Economical", "Careful", 0,
     "Frugal means sparing with money. Its opposite must be wasteful - extravagant. Options (B) and "
     "(C) are synonyms of frugal, and (D) is a mild synonym, so they cannot be antonyms.",
     "Antonym"),
    ("ENG", "Replace the underlined part with the correct idiom: The manager ____ to all our "
     "complaints and did nothing.",
     "turned a deaf ear", "turned his head", "made his ears", "paid his ears", 0,
     "'Turn a deaf ear to' means to deliberately refuse to listen. The other three are not English "
     "idioms - they are invented forms that simply repeat the idea of 'ear'.", "Idiom"),
    ("ENG", "Fill in the blank with the correct phrasal verb: The cricket match was ____ because of "
     "heavy rain.",
     "called off", "called on", "called for", "called up", 0,
     "Call off = cancel. Call on = visit somebody; call for = demand/require; call up = telephone or "
     "summon. Only 'called off' fits the meaning 'cancelled'.", "Phrasal verb"),
    ("ENG", "Change the voice: Who wrote this letter?",
     "By whom was this letter written?", "Whom was this letter written by?",
     "Who was this letter written?", "By who was this letter written?", 0,
     "In a passive 'who' question, 'who' becomes 'by whom' and the auxiliary comes before the "
     "subject: By whom + was + this letter + written? Option (D) uses 'who' after a preposition, "
     "which is wrong; (C) drops 'by whom' entirely.", "Voice"),
    ("ENG", "Change the voice: The teacher is explaining the lesson.",
     "The lesson is being explained by the teacher.", "The lesson is explained by the teacher.",
     "The lesson was being explained by the teacher.", "The lesson has been explained by the teacher.",
     0,
     "Present continuous active -> 'is/am/are + being + past participle'. 'Is explaining' therefore "
     "becomes 'is being explained'. Option (B) is simple present, (C) is past continuous, (D) is "
     "present perfect - each changes the tense.", "Voice"),
    ("ENG", "Change into indirect speech: He said, \"I am busy now.\"",
     "He said that he was busy then.", "He said that he is busy now.",
     "He said that he had been busy then.", "He told that he was busy now.", 0,
     "When the reporting verb is in the past, present tense shifts to past ('am' -> 'was') and 'now' "
     "becomes 'then'. (B) keeps the present tense, (C) shifts one step too far, and (D) uses 'told' "
     "without an object.", "Narration"),
    ("ENG", "Fill in the blank with the correct article: He is ____ honest man.",
     "an", "a", "the", "no article", 0,
     "The choice depends on sound, not spelling. 'Honest' begins with a vowel sound (the h is "
     "silent), so 'an' is required. Compare 'a hotel' (h pronounced) with 'an hour' (h silent).",
     "Article"),
    ("ENG", "Choose the correct verb: Neither of the two boys ____ present in the class today.",
     "was", "were", "have been", "are", 0,
     "'Neither of' is singular: it means 'not one of the two'. So the verb must be singular - 'was'. "
     "The plural noun after 'of' does not control the verb; the subject is 'neither'.",
     "Subject-verb agreement"),
    ("ENG", "Fill in the blank with the correct tense: My uncle ____ in this town since 2015.",
     "has been living", "is living", "lives", "lived", 0,
     "'Since + point of time' signals the present perfect continuous when the action continues: "
     "has/have been + V-ing. 'Is living' and 'lives' ignore the 'since' clause; 'lived' would be "
     "complete past.", "Tense"),
    ("ENG", "One-word substitution: A person who loves mankind is called a",
     "philanthropist", "philatelist", "misanthrope", "pedestrian", 0,
     "Philanthropist = lover of mankind (philos + anthropos). Philatelist = stamp collector; "
     "misanthrope = hater of mankind; pedestrian = walker. The prefix 'phil-' and suffix '-anthrope' "
     "carry the clue.", "One-word substitution"),
    ("ENG", "One-word substitution: A word having the opposite meaning of another word is called",
     "an antonym", "a synonym", "a homonym", "an acronym", 0,
     "Antonym = opposite meaning; synonym = same meaning; homonym = same sound/spelling, different "
     "meaning; acronym = word formed from initials. The prefix 'anti-' (against) gives it away.",
     "One-word substitution"),
    ("ENG", "Fill in the blank with the correct collective noun: A ____ of ships sailed into the "
     "harbour.",
     "fleet", "flock", "herd", "swarm", 0,
     "Fleet is the collective noun for ships (also for vehicles of an airline). Flock is for birds or "
     "sheep, herd for cattle, swarm for bees or insects.", "Collective noun"),
    ("ENG", "The feminine gender of BACHELOR is",
     "spinster", "widow", "bride", "madam", 0,
     "Bachelor (an unmarried man) pairs with spinster (an unmarried woman). Widow is the feminine of "
     "widower, bride of bridegroom, and madam of sir.", "Gender"),
    ("ENG", "In the sentence 'She sings beautifully', the word 'beautifully' is a/an",
     "adverb", "adjective", "noun", "conjunction", 0,
     "'Beautifully' modifies the verb 'sings', telling us how she sings - that is the job of an "
     "adverb. An adjective would modify a noun, e.g. 'a beautiful song'.", "Parts of speech"),
    ("ENG", "Identify the type of sentence: If it rains, we shall stay indoors.",
     "Complex", "Simple", "Compound", "Exclamatory", 0,
     "The sentence has one main clause ('we shall stay indoors') and one dependent clause introduced "
     "by 'if' - that is a complex sentence. A compound sentence joins two independent clauses with "
     "and/but/or.", "Sentence type"),
    ("ENG", "Fill in the blank: He is senior ____ me by two years.",
     "to", "than", "from", "by", 0,
     "Latin comparatives senior, junior, superior, inferior, prior take 'to', not 'than'. This is a "
     "very common error in West Bengal PSC papers: 'senior to', not 'senior than'.",
     "Preposition"),
    ("ENG", "Choose the correctly spelt word.",
     "Millennium", "Milennium", "Millenium", "Milenium", 0,
     "Millennium has a double 'l' and a double 'n': m-i-l-l-e-n-n-i-u-m, from Latin 'mille' (thousand) "
     "+ 'annus' (year). Nothing else in the options preserves both double letters.", "Spelling"),
    ("ENG", "Fill in the blank with the correct word: The drought had a bad ____ on the crops.",
     "effect", "affect", "effort", "afflict", 0,
     "'Effect' is the noun (result); 'affect' is the verb (to influence). The sentence needs a noun "
     "after 'a bad', so 'effect' is correct. Test: if you can put 'the' before it, use effect.",
     "Homophone"),
    ("ENG", "Fill in the blank with the correct conjunction: He is poor ____ honest.",
     "but", "and", "because", "so", 0,
     "The two facts contrast with each other, so an adversative conjunction is needed - 'but'. 'And' "
     "would suggest both facts point the same way; 'because' and 'so' would wrongly claim a "
     "cause-effect relation.", "Conjunction"),
    ("ENG", "Fill in the blank with the correct modal: You ____ obey the rules of the examination "
     "hall.",
     "must", "may", "can", "might", 0,
     "'Must' expresses strong obligation, which fits the sense of a rule. 'May' and 'can' give "
     "permission, and 'might' suggests a weak possibility - none expresses compulsion.",
     "Modal verb"),
    ("ENG", "Spot the error: One of my friend is a doctor.",
     "friend should be friends", "is should be are", "my should be mine",
     "The sentence is correct", 0,
     "The subject is 'One', which is singular, and takes a singular verb ('is' - already correct). "
     "But after 'one of + plural noun' the noun must be plural: one of my friends. Only the noun is "
     "wrong.", "Error spotting"),
    ("ENG", "Choose the word most opposite in meaning to TRANSPARENT.",
     "Opaque", "Clear", "Translucent", "Visible", 0,
     "Transparent = allowing light through so that objects behind can be seen clearly. Its true "
     "opposite is opaque (no light passes). 'Translucent' is a middle state, not the opposite, and "
     "'clear'/'visible' are synonyms.", "Antonym"),
    ("ENG", "Choose the word nearest in meaning to CANDID.",
     "Frank", "Cunning", "Rude", "Shy", 0,
     "Candid = openly honest and direct, i.e. frank. 'Cunning' and 'shy' are quite different; 'rude' "
     "is the trap, because a candid remark can offend, but candour itself means honesty, not bad "
     "manners.", "Synonym"),
    ("ENG", "Read the italicised phrase and choose the correct meaning: The news of his transfer "
     "came as ____, because nobody had expected it.",
     "a bolt from the blue", "a bed of roses", "a fish out of water", "a snake in the grass", 0,
     "'A bolt from the blue' means a complete and unexpected shock, which matches 'nobody had "
     "expected it'. 'A bed of roses' means a comfortable situation; 'a fish out of water' means "
     "awkwardness; 'a snake in the grass' means a hidden enemy.", "Idiom"),
    ("ENG", "Replace the underlined word with the correct phrasal verb: The meeting has been ____ to "
     "next Monday.",
     "put off", "put on", "put up", "put out", 0,
     "Put off = postpone. Put on = wear or switch on; put up = erect or accommodate; put out = "
     "extinguish. The sense 'moved to a later date' fixes 'put off'.", "Phrasal verb"),
    ("ENG", "Fill in the blank with the correct form: This is the ____ book I have ever read.",
     "best", "better", "good", "most best", 0,
     "The superlative 'best' is used with 'the' when one thing is compared with all others ('ever "
     "read'). 'Better' is comparative and needs only two things; 'most best' is a double superlative, "
     "which is grammatically wrong.", "Degrees of comparison"),
    ("ENG", "The plural form of CRISIS is",
     "crises", "crisises", "crisi", "crisis", 0,
     "Nouns ending in -is of Greek origin form the plural with -es: crisis -> crises, analysis -> "
     "analyses, thesis -> theses, axis -> axes. The ending is pronounced '-eez'.", "Number"),

    # ------------------------------------------------------------ GENERAL STUDIES
    ("GS", "Which district of West Bengal has the largest area under the Sundarbans mangrove forest?",
     "South 24 Parganas", "North 24 Parganas", "Purba Medinipur", "Nadia", 0,
     "The Indian Sundarbans lies in the delta of the Ganga-Brahmaputra and is shared by South 24 "
     "Parganas and North 24 Parganas, with the larger and more famous tiger reserve portion in South "
     "24 Parganas.", "WB Geography", "South 24 Parganas", "WBPSC Clerkship 2019-2023 pattern; "
     "NCERT Geography"),
    ("GS", "Which river is known as the 'Sorrow of Bengal'?",
     "Damodar", "Hooghly", "Teesta", "Mahanadi", 0,
     "The Damodar was called the Sorrow of Bengal because of its destructive annual floods before the "
     "Damodar Valley Corporation dams (1948 onwards) tamed it. The Kosi is the 'Sorrow of Bihar'; the "
     "Hooghly is a distributary, not a flood river.", "WB Geography", "Damodar",
     "NCERT Geography; WB Board Class VIII"),
    ("GS", "The Farakka Barrage is built across which river?",
     "Ganga", "Brahmaputra", "Damodar", "Barakar", 0,
     "The Farakka Barrage, in Murshidabad district, diverts Ganga water into the Bhagirathi-Hooghly "
     "through a feeder canal to keep the Kolkata port navigable. It is one of the longest barrages in "
     "the world.", "WB Geography", "Ganga", "NCERT Geography"),
    ("GS", "Haldia port is situated in which district of West Bengal?",
     "Purba Medinipur", "Paschim Medinipur", "Howrah", "South 24 Parganas", 0,
     "Haldia, a riverine port on the Hooghly about 50 km downstream of Kolkata, lies in Purba "
     "Medinipur district. It was developed to relieve pressure on the silt-choked Kolkata port.",
     "WB Geography", "Purba Medinipur", "WB District Gazetteers"),
    ("GS", "The highest peak in West Bengal is",
     "Sandakphu", "Falut", "Tiger Hill", "Namchi", 0,
     "Sandakphu (3,636 m) on the Singalila ridge in Darjeeling district is the highest point in West "
     "Bengal. Tiger Hill is lower and famous only for its sunrise view; Namchi is in Sikkim.",
     "WB Geography", "Sandakphu", "Survey of India; WB Tourism"),
    ("GS", "The state animal of West Bengal is",
     "fishing cat", "Royal Bengal tiger", "red panda", "elephant", 0,
     "West Bengal's state animal is the fishing cat (Prionailurus viverrinus), declared in 2012. The "
     "Royal Bengal tiger is the national animal of India, and the red panda is the state animal of "
     "Sikkim.", "WB Static GK", "fishing cat", "WB Forest Department"),
    ("GS", "The Battle of Plassey was fought in the year",
     "1757", "1764", "1765", "1739", 0,
     "Robert Clive defeated Siraj-ud-Daulah at Plassey (Palashi, Nadia district) on 23 June 1757 after "
     "Mir Jafar's betrayal. 1764 is Buxar, 1765 is the grant of Diwani, and 1739 is Nadir Shah's "
     "invasion.", "Modern History", "1757", "NCERT Class VIII History, Ch. 2"),
    ("GS", "The Permanent Settlement of Bengal was introduced by",
     "Lord Cornwallis", "Warren Hastings", "Lord Wellesley", "Lord Dalhousie", 0,
     "Cornwallis introduced the Permanent Settlement in 1793, fixing land revenue with zamindars "
     "permanently. Warren Hastings had experimented with the system earlier, but the settlement of "
     "1793 is credited to Cornwallis.", "Modern History", "Cornwallis",
     "NCERT Class VIII History, Ch. 3"),
    ("GS", "The partition of Bengal was announced in 1905 by",
     "Lord Curzon", "Lord Minto", "Lord Ripon", "Lord Hardinge", 0,
     "Viceroy Lord Curzon partitioned Bengal on 16 October 1905, dividing it into East Bengal and "
     "Assam and West Bengal. The Swadeshi movement forced its annulment in 1911 under Hardinge.",
     "Modern History", "Curzon", "NCERT Class VIII History, Ch. 8"),
    ("GS", "The founder of the Maurya dynasty was",
     "Chandragupta Maurya", "Bindusara", "Ashoka", "Bimbisara", 0,
     "Chandragupta Maurya (321 BCE) founded the empire with Chanakya's help, overthrowing the Nandas. "
     "Bindusara was his son, Ashoka his grandson, and Bimbisara belonged to the earlier Haryanka "
     "dynasty of Magadha.", "Ancient History", "Chandragupta Maurya",
     "NCERT Class VI History, Ch. 7"),
    ("GS", "Ashoka fought the Kalinga war in",
     "261 BCE", "321 BCE", "298 BCE", "185 BCE", 0,
     "The Kalinga war (261 BCE) is dated from Ashoka's 13th Rock Edict. Its bloodshed turned him to "
     "Buddhism. 321 BCE is the founding of the Maurya empire, 298 BCE Chandragupta's abdication, and "
     "185 BCE the fall of the Mauryas.", "Ancient History", "261 BCE",
     "NCERT Class VI History, Ch. 7"),
    ("GS", "The first session of the Indian National Congress was held in 1885 at",
     "Bombay", "Calcutta", "Madras", "Poona", 0,
     "The first session was held at Gokuldas Tejpal Sanskrit College, Bombay, in December 1885, with "
     "W. C. Bonnerjee as president and A. O. Hume as the moving spirit.", "Modern History", "Bombay",
     "NCERT Class VIII History, Ch. 9"),
    ("GS", "The Tropic of Cancer passes through how many Indian states?",
     "eight", "seven", "nine", "six", 0,
     "The Tropic of Cancer (23.5 deg N) crosses eight states: Gujarat, Rajasthan, Madhya Pradesh, "
     "Chhattisgarh, Jharkhand, West Bengal, Tripura and Mizoram. Keep the list in mind - it is asked "
     "both forwards and backwards.", "Indian Geography", "eight", "NCERT Class IX Geography, Ch. 1"),
    ("GS", "The longest river of India is",
     "Ganga", "Godavari", "Brahmaputra", "Narmada", 0,
     "The Ganga (about 2,525 km within India) is the longest river flowing wholly in Indian territory. "
     "The Godavari is the longest peninsular river and the Brahmaputra the largest by volume.",
     "Indian Geography", "Ganga", "NCERT Class IX Geography, Ch. 3"),
    ("GS", "The highest peak of the Nilgiri hills is",
     "Doddabetta", "Anamudi", "Mahendragiri", "Kalsubai", 0,
     "Doddabetta (2,637 m) is the highest point of the Nilgiris. Anamudi is the highest peak of the "
     "Western Ghats (in Kerala), Mahendragiri is in the Eastern Ghats, and Kalsubai is the highest "
     "peak of Maharashtra.", "Indian Geography", "Doddabetta", "NCERT Class IX Geography"),
    ("GS", "Black soil, the most suitable for cotton cultivation, is also known as",
     "regur soil", "laterite soil", "alluvial soil", "red soil", 0,
     "Black soil, formed from decomposed basalt lava on the Deccan plateau, is called regur or "
     "black-cotton soil for its moisture-retaining, self-ploughing character.", "Indian Geography",
     "regur", "NCERT Class X Geography, Ch. 1"),
    ("GS", "The idea of Fundamental Rights in the Indian Constitution is borrowed from the "
     "Constitution of",
     "the United States", "the United Kingdom", "Ireland", "Canada", 0,
     "Fundamental Rights come from the American Bill of Rights. From the UK we took parliamentary "
     "government, from Ireland the Directive Principles, and from Canada the federal scheme with a "
     "strong centre.", "Polity", "United States", "M. Laxmikanth, Indian Polity"),
    ("GS", "Article 21 of the Indian Constitution deals with",
     "protection of life and personal liberty", "right to equality before law",
     "right against exploitation", "right to freedom of religion", 0,
     "Article 21: no person shall be deprived of life or personal liberty except according to "
     "procedure established by law. Article 14 covers equality, Articles 23-24 exploitation, and "
     "Articles 25-28 religion.", "Polity", "life and personal liberty",
     "Constitution of India, Part III"),
    ("GS", "The President of India is elected by",
     "an electoral college of elected MPs and MLAs", "a direct vote of all citizens",
     "the members of the Lok Sabha only", "the Council of Ministers", 0,
     "Under Article 54, the President is elected indirectly by an electoral college of the elected "
     "members of both Houses of Parliament and of the Legislative Assemblies of the states and Union "
     "territories with legislatures, by proportional representation with single transferable vote.",
     "Polity", "electoral college", "Constitution of India, Article 54"),
    ("GS", "The 73rd Constitutional Amendment is related to",
     "Panchayati Raj", "Urban local bodies", "GST", "Anti-defection", 0,
     "The 73rd Amendment (1992) gave constitutional status to the three-tier Panchayati Raj system and "
     "added Part IX and the Eleventh Schedule. The 74th Amendment deals with urban local bodies.",
     "Polity", "Panchayati Raj", "Constitution of India, Part IX"),
    ("GS", "A Money Bill can be introduced only in",
     "Lok Sabha", "Rajya Sabha", "either House", "a joint sitting", 0,
     "Under Article 110, a Money Bill can be introduced only in the Lok Sabha and only on the "
     "recommendation of the President. The Rajya Sabha may make recommendations within 14 days, but "
     "cannot amend or reject it.", "Polity", "Lok Sabha", "Constitution of India, Article 110"),
    ("GS", "The Governor of a state is appointed by the",
     "President", "Prime Minister", "Chief Justice of India", "state legislature", 0,
     "Article 155: the Governor is appointed by the President by warrant under his hand and seal, and "
     "holds office during the pleasure of the President. He is the constitutional head of the state, "
     "not of the judiciary.", "Polity", "President", "Constitution of India, Article 155"),
    ("GS", "The SI unit of force is",
     "newton", "joule", "pascal", "watt", 0,
     "Force = mass x acceleration, so its unit is kg m/s^2, named the newton (N) after Isaac Newton. "
     "Joule is energy, pascal is pressure and watt is power.", "Physics", "newton",
     "NCERT Class IX Science, Ch. 9"),
    ("GS", "Deficiency of Vitamin C causes",
     "scurvy", "rickets", "beri-beri", "night blindness", 0,
     "Vitamin C (ascorbic acid) deficiency causes scurvy - bleeding gums and slow wound healing. "
     "Rickets is from Vitamin D, beri-beri from Vitamin B1, and night blindness from Vitamin A.",
     "Biology", "scurvy", "NCERT Class X Science, Ch. 6"),
    ("GS", "The largest gland in the human body is the",
     "liver", "pancreas", "thyroid", "pituitary", 0,
     "The liver is the largest gland and the largest internal organ; it secretes bile and performs "
     "detoxification. The pancreas is a mixed gland, the thyroid is endocrine only, and the pituitary "
     "the smallest master gland.", "Biology", "liver", "NCERT Class X Science, Ch. 6"),
    ("GS", "Which gas is absorbed by green plants during photosynthesis?",
     "carbon dioxide", "oxygen", "nitrogen", "hydrogen", 0,
     "Photosynthesis uses carbon dioxide and water in the presence of chlorophyll and sunlight to make "
     "glucose, releasing oxygen. Nitrogen is fixed by bacteria, not by photosynthesis.", "Biology",
     "carbon dioxide", "NCERT Class X Science, Ch. 6"),
    ("GS", "The instrument used to record earthquakes is a",
     "seismograph", "barograph", "hygrometer", "anemometer", 0,
     "A seismograph records the intensity and duration of tremors. A barograph records pressure, a "
     "hygrometer humidity and an anemometer wind speed.", "Science", "seismograph",
     "NCERT Class VIII Science"),
    ("GS", "NITI Aayog replaced which body in 2015?",
     "Planning Commission", "Finance Commission", "National Development Council",
     "Election Commission", 0,
     "NITI Aayog (National Institution for Transforming India) was set up on 1 January 2015, "
     "replacing the Planning Commission of 1950. The Finance Commission and Election Commission are "
     "constitutional bodies and continue.", "Economy", "Planning Commission",
     "NITI Aayog Annual Report"),
    ("GS", "The Reserve Bank of India was established in",
     "1935", "1947", "1949", "1955", 0,
     "The RBI was set up on 1 April 1935 under the RBI Act, 1934, and nationalised on 1 January 1949. "
     "1947 is Independence, and 1955 is the nationalisation of the Imperial Bank into SBI.",
     "Economy", "1935", "RBI Act, 1934"),
    ("GS", "The Goods and Services Tax (GST) came into force in India on",
     "1 July 2017", "1 April 2017", "1 July 2016", "15 August 2017", 0,
     "GST was rolled out at midnight on 1 July 2017 after the 101st Constitutional Amendment. The GST "
     "Council, chaired by the Union Finance Minister, governs its rates.", "Economy", "1 July 2017",
     "GST Council records"),
    ("GS", "Which country won the ICC Men's T20 World Cup 2026?",
     "India", "New Zealand", "Australia", "South Africa", 0,
     "India beat New Zealand by 96 runs in the final at the Narendra Modi Stadium, Ahmedabad, on 8 "
     "March 2026 - their third T20 World Cup title. The tournament was co-hosted by India and Sri "
     "Lanka.", "Current Affairs", "India",
     "ICC / media reports, March 2026 (co-hosts India and Sri Lanka; final 8.3.2026)"),
    ("GS", "The FIFA World Cup 2026 was won by",
     "Spain", "Argentina", "France", "Brazil", 0,
     "Spain beat Argentina 1-0 in extra time in the final at MetLife Stadium, New Jersey, on 19 July "
     "2026. It was Spain's second men's World Cup title after 2010; the tournament was hosted by the "
     "USA, Canada and Mexico.", "Current Affairs", "Spain",
     "NPR / NBC reports, 19-20 July 2026"),
    ("GS", "The 2026 Winter Olympics were held in",
     "Milan and Cortina d'Ampezzo", "Beijing", "Pyeongchang", "Sapporo", 0,
     "The 25th Winter Olympics were held in Milan and Cortina d'Ampezzo, Italy, from 6 to 22 February "
     "2026, with the closing ceremony at the Verona Arena. Norway topped the medal table with 18 golds.",
     "Current Affairs", "Milan and Cortina", "IOC / media reports, February 2026"),
    ("GS", "The Commonwealth Games 2026 were hosted by",
     "Glasgow", "Birmingham", "Melbourne", "Durban", 0,
     "Glasgow stepped in to host the 2026 Commonwealth Games, which concluded on 2 August 2026. India "
     "finished fourth with 39 medals (13 gold, 17 silver, 9 bronze); Australia topped the table.",
     "Current Affairs", "Glasgow", "CGF / media reports, August 2026"),
    ("GS", "Who took oath as the Chief Minister of West Bengal in May 2026?",
     "Suvendu Adhikari", "Mamata Banerjee", "Dilip Ghosh", "Sovandeb Chattopadhyay", 0,
     "Suvendu Adhikari was sworn in on 9 May 2026 as the 9th Chief Minister of West Bengal and the "
     "first from the BJP, after the 2026 assembly election ended 15 years of Trinamool Congress rule.",
     "Current Affairs", "Suvendu Adhikari", "News reports, 8-9 May 2026"),
    ("GS", "Who is the Vice-President of India at present?",
     "C. P. Radhakrishnan", "Jagdeep Dhankhar", "M. Venkaiah Naidu", "Hamid Ansari", 0,
     "C. P. Radhakrishnan assumed office as the 15th Vice-President of India and ex-officio Chairman "
     "of the Rajya Sabha on 12 September 2025, after the resignation of Jagdeep Dhankhar.",
     "Current Affairs", "C. P. Radhakrishnan", "Vice-President's Secretariat; '2026 in India'"),
    ("GS", "Who is the present Chief Justice of India?",
     "Surya Kant", "D. Y. Chandrachud", "Sanjiv Khanna", "N. V. Ramana", 0,
     "Justice Surya Kant took oath as the 53rd Chief Justice of India on 24 November 2025, succeeding "
     "Justice B. R. Gavai. D. Y. Chandrachud was the 50th CJI and Sanjiv Khanna the 51st.",
     "Current Affairs", "Surya Kant", "Supreme Court of India; '2026 in India'"),
    ("GS", "Who is the Governor of the Reserve Bank of India?",
     "Sanjay Malhotra", "Shaktikanta Das", "Urjit Patel", "Raghuram Rajan", 0,
     "Sanjay Malhotra became the 26th Governor of the RBI on 11 December 2024, succeeding Shaktikanta "
     "Das. The RBI Governor is appointed by the Central Government under the RBI Act, 1934.",
     "Current Affairs", "Sanjay Malhotra", "RBI; '2026 in India'"),
    ("GS", "The present Chairman of ISRO is",
     "V. Narayanan", "S. Somanath", "K. Sivan", "A. S. Kiran Kumar", 0,
     "Dr V. Narayanan took charge as Chairman, ISRO and Secretary, Department of Space in January "
     "2025, succeeding S. Somanath. ISRO is headquartered at Bengaluru.", "Current Affairs",
     "V. Narayanan", "ISRO; '2026 in India'"),
    ("GS", "Gaganyaan, India's first human spaceflight programme, is designed to carry how many "
     "astronauts?",
     "three", "two", "four", "one", 0,
     "Gaganyaan will send three astronauts (Gaganyatris) into low earth orbit for up to three days. "
     "The first uncrewed orbital test flight (G1) is targeted for the second half of 2026, ahead of "
     "the crewed mission.", "Current Affairs", "three", "ISRO Gaganyaan programme brief"),

    # ----------------------------------------------------------------- ARITHMETIC
    ("AR", "What is the value of 40% of 250 + 25% of 320?",
     "180", "170", "190", "200", 0,
     "Step 1: 40% of 250 = 0.40 x 250 = 100. Step 2: 25% of 320 = 0.25 x 320 = 80. Step 3: 100 + 80 "
     "= 180.", "Percentage", "0.40*250 + 0.25*320"),
    ("AR", "A shopkeeper buys an article for Rs 400 and sells it for Rs 460. His profit percentage is",
     "15%", "12%", "13%", "16%", 0,
     "Step 1: Profit = SP - CP = 460 - 400 = 60. Step 2: Profit % = (Profit / CP) x 100 = (60/400) x "
     "100 = 15%. Note the base is the cost price, never the selling price.", "Profit and loss",
     "100*(460-400)/400"),
    ("AR", "The simple interest on Rs 8,000 at 7.5% per annum for 3 years is",
     "Rs 1,800", "Rs 1,600", "Rs 2,000", "Rs 1,750", 0,
     "Step 1: SI = (P x R x T)/100. Step 2: = (8000 x 7.5 x 3)/100. Step 3: 8000 x 7.5 = 60,000; x 3 "
     "= 1,80,000; /100 = Rs 1,800.", "Simple interest", "8000*7.5*3/100"),
    ("AR", "The compound interest on Rs 10,000 at 10% per annum for 2 years, compounded annually, is",
     "Rs 2,100", "Rs 2,000", "Rs 2,200", "Rs 1,900", 0,
     "Step 1: A = P(1 + r/100)^t = 10000 x (1.1)^2. Step 2: (1.1)^2 = 1.21, so A = Rs 12,100. Step 3: "
     "CI = A - P = 12100 - 10000 = Rs 2,100. (SI would have been 2,000; the extra 100 is interest on "
     "the first year's interest.)", "Compound interest", "10000*1.1**2 - 10000"),
    ("AR", "Two numbers are in the ratio 3 : 4 and their sum is 84. The larger number is",
     "48", "36", "44", "56", 0,
     "Step 1: Let the numbers be 3x and 4x. Step 2: 3x + 4x = 7x = 84, so x = 12. Step 3: The larger "
     "number is 4x = 48 (the smaller is 36).", "Ratio", "4*84/7"),
    ("AR", "The average of five numbers is 26. When one number is removed, the average of the "
     "remaining four becomes 25. The number removed is",
     "30", "26", "32", "28", 0,
     "Step 1: Sum of five numbers = 5 x 26 = 130. Step 2: Sum of the four remaining = 4 x 25 = 100. "
     "Step 3: Removed number = 130 - 100 = 30.", "Average", "5*26 - 4*25"),
    ("AR", "A can do a piece of work in 12 days and B in 18 days. Working together, they will "
     "complete it in",
     "7 1/5 days", "7 1/2 days", "6 3/5 days", "8 days", 0,
     "Step 1: A's one-day work = 1/12, B's = 1/18. Step 2: Together = 1/12 + 1/18 = (3 + 2)/36 = "
     "5/36. Step 3: Time = 36/5 = 7 1/5 days (7.2 days).", "Time and work", "1/(1/12+1/18)"),
    ("AR", "One pipe can fill a tank in 6 hours and another can empty it in 9 hours. If both are "
     "opened together, the tank will be full in",
     "18 hours", "15 hours", "12 hours", "20 hours", 0,
     "Step 1: Filling rate = 1/6 per hour, emptying rate = 1/9 per hour. Step 2: Net rate = 1/6 - 1/9 "
     "= (3 - 2)/18 = 1/18. Step 3: Time = 18 hours.", "Pipes and cisterns", "1/(1/6-1/9)"),
    ("AR", "A speed of 72 km per hour equals",
     "20 m per second", "18 m per second", "24 m per second", "15 m per second", 0,
     "Step 1: To convert km/h to m/s multiply by 5/18. Step 2: 72 x 5/18 = 4 x 5 = 20. Step 3: So the "
     "speed is 20 m per second. (Reverse: m/s x 18/5 = km/h.)", "Speed conversion", "72*5/18"),
    ("AR", "A train 150 m long is running at 54 km/h. The time it takes to cross a platform 300 m "
     "long is",
     "30 seconds", "24 seconds", "36 seconds", "20 seconds", 0,
     "Step 1: Speed = 54 x 5/18 = 15 m/s. Step 2: Total distance = train + platform = 150 + 300 = 450 "
     "m. Step 3: Time = 450/15 = 30 seconds.", "Trains", "(150+300)/(54*5/18)"),
    ("AR", "A boat's speed in still water is 9 km/h and the speed of the stream is 3 km/h. The total "
     "time to go 36 km downstream and return 36 km upstream is",
     "9 hours", "8 hours", "10 hours", "12 hours", 0,
     "Step 1: Downstream speed = 9 + 3 = 12 km/h; upstream = 9 - 3 = 6 km/h. Step 2: Time downstream "
     "= 36/12 = 3 h; upstream = 36/6 = 6 h. Step 3: Total = 3 + 6 = 9 hours.", "Boats and streams",
     "36/(9+3) + 36/(9-3)"),
    ("AR", "A 40-litre mixture contains milk and water in the ratio 3 : 1. If 8 litres of water is "
     "added, the new ratio of milk to water is",
     "5 : 3", "3 : 2", "2 : 1", "4 : 3", 0,
     "Step 1: Milk = 3/4 x 40 = 30 L; water = 1/4 x 40 = 10 L. Step 2: Adding water does not change "
     "milk, so water becomes 10 + 8 = 18 L. Step 3: Ratio = 30 : 18 = 5 : 3.", "Mixture", "30/18"),
    ("AR", "The HCF of two numbers is 6 and their LCM is 72. If one number is 24, the other is",
     "18", "12", "36", "16", 0,
     "Step 1: For two numbers, HCF x LCM = product of the numbers. Step 2: 6 x 72 = 24 x x, so x = "
     "432/24. Step 3: x = 18. Check: HCF(24, 18) = 6 and LCM = 72.", "HCF and LCM", "6*72/24"),
    ("AR", "3/5 of a number is 72. What is 7/8 of that number?",
     "105", "96", "112", "84", 0,
     "Step 1: Let the number be x; (3/5)x = 72, so x = 72 x 5/3 = 120. Step 2: (7/8) x 120 = 7 x 15 "
     "= 105.", "Fractions", "(72*5/3)*7/8"),
    ("AR", "Five years ago a father was three times as old as his son. If the father is 47 now, the "
     "son's present age is",
     "19 years", "18 years", "21 years", "17 years", 0,
     "Step 1: Five years ago the father was 47 - 5 = 42. Step 2: 42 = 3 x (son's age then), so the "
     "son was 14. Step 3: Present age = 14 + 5 = 19 years.", "Ages", "(47-5)/3 + 5"),
    ("AR", "The angle between the hands of a clock at 3:30 is",
     "75 degrees", "90 degrees", "70 degrees", "85 degrees", 0,
     "Step 1: Hour hand moves 0.5 degree per minute, minute hand 6 degrees per minute. Step 2: At 3:30 "
     "the hour hand is at 3 x 30 + 30 x 0.5 = 105 deg; the minute hand is at 30 x 6 = 180 deg. Step "
     "3: Difference = 75 degrees.", "Clocks", "abs(180 - (3*30 + 30*0.5))"),
    ("AR", "If today is Monday, what day of the week will it be after 100 days?",
     "Wednesday", "Tuesday", "Thursday", "Friday", 0,
     "Step 1: Every 7 days the day repeats, so divide 100 by 7: 100 = 14 x 7 + 2. Step 2: The "
     "remainder 2 is all that matters: Monday + 2 days. Step 3: Wednesday.", "Calendar", "fact:Wednesday"),
    ("AR", "The perimeter of a rectangle is 60 m and its length is 18 m. Its area is",
     "216 sq m", "180 sq m", "198 sq m", "240 sq m", 0,
     "Step 1: 2(l + b) = 60, so l + b = 30. Step 2: b = 30 - 18 = 12 m. Step 3: Area = l x b = 18 x "
     "12 = 216 sq m.", "Area", "18*(60/2-18)"),
    ("AR", "Simplify: 2/3 + 3/4 - 5/6",
     "7/12", "5/12", "1/2", "3/4", 0,
     "Step 1: LCM of 3, 4 and 6 is 12. Step 2: 2/3 = 8/12, 3/4 = 9/12, 5/6 = 10/12. Step 3: (8 + 9 - "
     "10)/12 = 7/12.", "Simplification", "2/3+3/4-5/6"),
    ("AR", "The largest 3-digit number exactly divisible by 8 is",
     "992", "996", "984", "990", 0,
     "Step 1: The largest 3-digit number is 999. Step 2: Divide 999 by 8: 8 x 124 = 992, remainder 7. "
     "Step 3: Subtract the remainder: 999 - 7 = 992.", "Divisibility", "999 - (999%8)"),
    ("AR", "A town's population is 100. It increases by 10% in the first year and then decreases by "
     "10% in the second year. The population at the end of the second year is",
     "99", "100", "101", "98", 0,
     "Step 1: After a 10% rise: 100 x 1.10 = 110. Step 2: After a 10% fall: 110 x 0.90 = 99. Step 3: "
     "The net effect is a 1% fall, not zero, because the second percentage is taken on the larger "
     "figure. Shortcut: a + b + ab/100 = 10 - 10 - 1 = -1%.", "Percentage", "100*1.1*0.9"),
    ("AR", "The marked price of an article is Rs 750. After a 20% discount it is sold at a profit of "
     "25%. The cost price is",
     "Rs 480", "Rs 500", "Rs 450", "Rs 520", 0,
     "Step 1: Selling price = 750 x (1 - 0.20) = 750 x 0.8 = Rs 600. Step 2: SP = CP x 1.25, so CP = "
     "600/1.25. Step 3: CP = Rs 480.", "Discount", "750*0.8/1.25"),
    ("AR", "A invests Rs 5,000 for 12 months and B invests Rs 8,000 for 6 months in a business. In a "
     "profit of Rs 7,200, A's share is",
     "Rs 4,000", "Rs 3,200", "Rs 4,500", "Rs 3,600", 0,
     "Step 1: Profit shares are proportional to capital x time. Step 2: A = 5000 x 12 = 60,000; B = "
     "8000 x 6 = 48,000; ratio = 5 : 4. Step 3: A's share = 7200 x 5/9 = Rs 4,000.",
     "Partnership", "7200*5000*12/(5000*12+8000*6)"),
    ("AR", "If 15 men can complete a work in 12 days, how long will 20 men take (working at the same "
     "rate)?",
     "9 days", "10 days", "8 days", "11 days", 0,
     "Step 1: Work = men x days = 15 x 12 = 180 man-days. Step 2: With 20 men, days = 180/20. Step 3: "
     "9 days. (More men, less time - inverse proportion.)", "Time and work", "15*12/20"),
    ("AR", "45 is what per cent of 180?",
     "25%", "20%", "30%", "40%", 0,
     "Step 1: Percentage = (part / whole) x 100. Step 2: = (45/180) x 100. Step 3: 45/180 = 1/4, so "
     "the answer is 25%.", "Percentage", "100*45/180"),
    ("AR", "At what rate of simple interest will a sum of money double itself in 8 years?",
     "12.5% per annum", "10% per annum", "8% per annum", "15% per annum", 0,
     "Step 1: Doubling means interest = principal, i.e. SI = P. Step 2: P = P x R x 8/100, so R x 8 = "
     "100. Step 3: R = 12.5% per annum.", "Simple interest", "100/8"),
    ("AR", "A can finish 1/3 of a work in 5 days and B can finish 1/4 of it in 6 days. Working "
     "together they will finish the work in",
     "9 3/13 days", "9 days", "10 days", "8 5/13 days", 0,
     "Step 1: A finishes the whole work in 5 x 3 = 15 days; B in 6 x 4 = 24 days. Step 2: Together "
     "one day = 1/15 + 1/24 = (8 + 5)/120 = 13/120. Step 3: Time = 120/13 = 9 3/13 days.",
     "Time and work", "1/(1/15+1/24)"),
    ("AR", "The average of the first 20 natural numbers is",
     "10.5", "10", "11", "9.5", 0,
     "Step 1: Sum = n(n + 1)/2 = 20 x 21/2 = 210. Step 2: Average = 210/20. Step 3: 10.5. Shortcut: "
     "average of the first n natural numbers = (n + 1)/2 = 21/2 = 10.5.", "Average", "(20+1)/2"),
    ("AR", "A trader sells 20 articles at the cost price of 25 articles. His profit percentage is",
     "25%", "20%", "15%", "30%", 0,
     "Step 1: Let CP of one article be Re 1, so CP of 20 = Rs 20 and SP of 20 = Rs 25. Step 2: Profit "
     "= 25 - 20 = Rs 5. Step 3: Profit % = 5/20 x 100 = 25%.", "Profit and loss", "100*(25-20)/20"),
    ("AR", "A car covers 240 km in 4 hours and the next 180 km in 2 hours. Its average speed for the "
     "whole journey is",
     "70 km/h", "65 km/h", "72 km/h", "75 km/h", 0,
     "Step 1: Total distance = 240 + 180 = 420 km. Step 2: Total time = 4 + 2 = 6 h. Step 3: Average "
     "speed = 420/6 = 70 km/h. Never average the two speeds (60 and 90) - that gives a wrong 75.",
     "Speed and distance", "(240+180)/(4+2)"),
]

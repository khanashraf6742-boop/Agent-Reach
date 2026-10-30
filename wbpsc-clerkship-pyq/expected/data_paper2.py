"""Expected paper 2 -- WBPSC Clerkship Part-I.

Same schema as data_paper1.py. Every GS item carries a canonical `fact` (validator pass 3),
every AR item carries an independently evaluated `check` expression (validator pass 2).
"""

PAPER = [
    # ------------------------------------------------------------------ ENGLISH
    ("ENG", "Fill in the blank with the correct preposition: He is married ____ my cousin.",
     "to", "with", "by", "for", 0,
     "'Marry' and 'married' take 'to' when a person follows: married to my cousin. 'With' is the "
     "common Indian-English error. Note the verb form: she married him (no preposition), but she is "
     "married to him.", "Preposition"),
    ("ENG", "Fill in the blank with the correct preposition: The bus is bound ____ Siliguri.",
     "for", "to", "at", "in", 0,
     "'Bound for' means travelling towards a place: bound for Siliguri / bound for Kolkata. 'Bound to' "
     "means certain or obliged ('bound to happen'), which changes the meaning completely.",
     "Preposition"),
    ("ENG", "Choose the word nearest in meaning to ABANDON.",
     "Forsake", "Retain", "Repair", "Admire", 0,
     "Abandon = give up completely, i.e. forsake. 'Retain' is nearly its opposite; 'repair' and "
     "'admire' have no relation to the sense of leaving something behind.", "Synonym"),
    ("ENG", "Choose the word most opposite in meaning to BENEVOLENT.",
     "Cruel", "Kind", "Generous", "Helpful", 0,
     "Benevolent = wishing good to others. The opposite must be cruel (wishing harm). 'Kind', "
     "'generous' and 'helpful' are all synonyms of benevolent, so none can be the antonym.",
     "Antonym"),
    ("ENG", "Choose the correct meaning of the idiom: The decision was taken at the eleventh hour.",
     "at the last possible moment", "at eleven o'clock exactly", "very early",
     "after a long delay", 0,
     "'At the eleventh hour' means at the last possible moment, just before it is too late. It has "
     "nothing to do with clock time, and 'very early' is its opposite.", "Idiom"),
    ("ENG", "Fill in the blank with the correct phrasal verb: The committee ____ the proposal "
     "outright.",
     "turned down", "turned up", "turned in", "turned over", 0,
     "Turn down = reject. Turn up = arrive or increase; turn in = submit or go to bed; turn over = "
     "hand over or flip. 'Outright' signals rejection, so 'turned down' fits.", "Phrasal verb"),
    ("ENG", "Change the voice: They are building a new bridge.",
     "A new bridge is being built by them.", "A new bridge is built by them.",
     "A new bridge was being built by them.", "A new bridge has been built by them.", 0,
     "Present continuous passive = is/am/are + being + past participle. 'Are building' therefore "
     "becomes 'is being built' (the object 'a new bridge' is singular, so 'is').", "Voice"),
    ("ENG", "Change the voice: Someone has stolen my pen.",
     "My pen has been stolen.", "My pen was stolen.", "My pen is stolen.", "My pen had been stolen.",
     0,
     "Present perfect active -> has/have + been + past participle: 'has stolen' becomes 'has been "
     "stolen'. When the doer is 'someone/somebody', the agent ('by someone') is dropped in the "
     "passive.", "Voice"),
    ("ENG", "Change into indirect speech: She said, \"I will come tomorrow.\"",
     "She said that she would come the next day.", "She said that she will come tomorrow.",
     "She said that she would come tomorrow.", "She said that she comes the next day.", 0,
     "Two shifts happen together: 'will' -> 'would', and 'tomorrow' -> 'the next day' (or 'the "
     "following day'). Option (C) shifts the verb but forgets the time word; (B) shifts neither.",
     "Narration"),
    ("ENG", "Fill in the blank with the correct article: ____ Ganga is a holy river.",
     "The", "A", "An", "No article", 0,
     "Names of rivers take the definite article: the Ganga, the Hooghly, the Nile. The definite "
     "article marks a particular, identifiable thing, and there is only one Ganga.", "Article"),
    ("ENG", "Choose the correct verb: Each of the students ____ a book.",
     "has", "have", "are having", "were having", 0,
     "'Each of + plural noun' is singular: each one of the students has a book. The plural noun after "
     "'of' is not the subject. The same rule applies to 'every one of', 'either of' and 'neither of'.",
     "Subject-verb agreement"),
    ("ENG", "Fill in the blank with the correct tense: He ____ here for two hours.",
     "has been waiting", "is waiting", "waits", "waited", 0,
     "'For + period of time' with an action still going on needs the present perfect continuous: has "
     "been waiting. 'Is waiting' ignores the duration, and 'waited' would mean the waiting is over.",
     "Tense"),
    ("ENG", "One-word substitution: A person who writes the story of his own life is called",
     "an autobiographer", "a biographer", "a bibliographer", "a calligrapher", 0,
     "Auto (self) + bio (life) + grapher (writer) = one who writes his own life story. A biographer "
     "writes someone else's life, a bibliographer lists books, and a calligrapher does ornamental "
     "handwriting. The word for such a writer is an autobiographer.", "One-word substitution"),
    ("ENG", "One-word substitution: Government by the people is called",
     "democracy", "autocracy", "oligarchy", "theocracy", 0,
     "Demos (people) + kratos (power) = democracy. Autocracy is one-person rule, oligarchy is rule by "
     "a few, and theocracy is rule in the name of God.", "One-word substitution"),
    ("ENG", "Fill in the blank with the correct collective noun: A ____ of cattle was grazing in the "
     "field.",
     "herd", "flock", "pack", "swarm", 0,
     "Herd is used for cattle (and also elephants and deer). Flock is for sheep or birds, pack for "
     "wolves or dogs, and swarm for bees or insects.", "Collective noun"),
    ("ENG", "The feminine gender of NEPHEW is",
     "niece", "nephewess", "cousin", "aunt", 0,
     "Nephew (brother's or sister's son) pairs with niece (brother's or sister's daughter). Aunt is "
     "the feminine of uncle, and cousin is common gender - it is used for both.",
     "Gender"),
    ("ENG", "In the phrase 'a golden ring', the word 'golden' is a/an",
     "adjective", "adverb", "noun", "verb", 0,
     "'Golden' describes the noun 'ring', so it is an adjective. Note the difference between 'golden' "
     "(made of / like gold, adjectival) and 'gold' (the metal, a noun).", "Parts of speech"),
    ("ENG", "Identify the type of sentence: He worked hard, yet he failed.",
     "Compound", "Simple", "Complex", "Exclamatory", 0,
     "Two independent clauses ('He worked hard' and 'he failed') are joined by the coordinating "
     "conjunction 'yet' - that is a compound sentence. A complex sentence would need a subordinator "
     "such as although, because or if.", "Sentence type"),
    ("ENG", "Fill in the blank with the correct preposition: He is incapable ____ doing such a thing.",
     "of", "to", "for", "in", 0,
     "Incapable of + gerund: incapable of doing. The pair is 'capable of' / 'incapable of'. Students "
     "often write 'incapable to do', which is wrong in standard English.", "Preposition"),
    ("ENG", "Choose the correctly spelt word.",
     "Accommodation", "Accomodation", "Acommodation", "Accommudation", 0,
     "Accommodation has double 'c' and double 'm': a-c-c-o-m-m-o-d-a-t-i-o-n. It comes from Latin "
     "'accommodare' (to fit), and both consonants are doubled.", "Spelling"),
    ("ENG", "Fill in the blank with the correct word: He is the ____ of our school.",
     "principal", "principle", "principally", "principality", 0,
     "Principal (noun) = the head of an institution; principle (noun) = a rule or belief. The mnemonic "
     "is that the princiPAL is your PAL. 'Principally' is an adverb and 'principality' means a "
     "territory ruled by a prince.", "Homophone"),
    ("ENG", "Fill in the blank with the correct conjunction: ____ he is rich, he is not happy.",
     "Although", "Because", "Since", "Unless", 0,
     "The sentence contrasts wealth with unhappiness, so a concessive conjunction is needed - "
     "although / though / even though. 'Because' and 'since' would wrongly assert a cause.",
     "Conjunction"),
    ("ENG", "Fill in the blank with the correct modal: You ____ not smoke here; it is a hospital.",
     "must", "can", "may", "would", 0,
     "'Must not' expresses prohibition. 'Can not'/'cannot' would state inability, and 'may not' gives "
     "only a mild negative permission - far too weak for a hospital rule.", "Modal verb"),
    ("ENG", "Spot the error: The furnitures in this room are very old.",
     "furnitures should be furniture", "are should be is", "very should be much",
     "The sentence is correct", 0,
     "'Furniture' is an uncountable noun and has no plural form: furniture, not furnitures. Other "
     "common uncountables of this type are information, luggage, advice, equipment and scenery.",
     "Error spotting"),
    ("ENG", "Choose the word most opposite in meaning to SCARCE.",
     "Abundant", "Rare", "Limited", "Costly", 0,
     "Scarce = in short supply. Its opposite is abundant (plentiful). 'Rare' and 'limited' are "
     "synonyms of scarce, and 'costly' describes price, not quantity.", "Antonym"),
    ("ENG", "Choose the word nearest in meaning to DILIGENT.",
     "Hardworking", "Careless", "Lazy", "Intelligent", 0,
     "Diligent = showing careful and persistent effort, i.e. hardworking. 'Careless' and 'lazy' are "
     "opposites, while 'intelligent' describes ability, not effort - a common trap.", "Synonym"),
    ("ENG", "Choose the correct meaning of the idiom: The clerk let the cat out of the bag about the "
     "new transfer order.",
     "revealed a secret", "made an error", "started a quarrel", "escaped from duty", 0,
     "'Let the cat out of the bag' means to reveal a secret, usually by accident. The other options "
     "describe different situations and do not match the idiom at all.", "Idiom"),
    ("ENG", "Fill in the blank with the correct phrasal verb: He ____ his father in appearance.",
     "takes after", "takes off", "takes on", "takes in", 0,
     "Take after = resemble (a parent or relative). Take off = remove or leave the ground; take on = "
     "accept or hire; take in = deceive or absorb. 'In appearance' signals resemblance.",
     "Phrasal verb"),
    ("ENG", "Fill in the blank with the correct form: He is the ____ of the two brothers.",
     "taller", "tallest", "tall", "more taller", 0,
     "When two people or things are compared, use the comparative ('taller'), even though 'the' is "
     "often used before it ('the taller of the two'). The superlative 'tallest' needs three or more. "
     "'More taller' is a double comparative and is wrong.", "Degrees of comparison"),
    ("ENG", "The plural form of DATUM is",
     "data", "datums", "datae", "datas", 0,
     "Datum is a Latin singular ending in -um; its plural is data (-a). The same pattern gives "
     "medium -> media, memorandum -> memoranda, criterion -> criteria.", "Number"),

    # ------------------------------------------------------------ GENERAL STUDIES
    ("GS", "Kolkata is situated on the bank of which river?",
     "Hooghly", "Damodar", "Teesta", "Kangsabati", 0,
     "Kolkata stands on the east bank of the Hooghly, a distributary of the Ganga. The Damodar and "
     "Kangsabati flow through south-western West Bengal, and the Teesta drains north Bengal.",
     "WB Geography", "Hooghly", "NCERT Class IX Geography"),
    ("GS", "The Sundarbans was declared a UNESCO World Heritage Site in",
     "1987", "1973", "1984", "1992", 0,
     "The Sundarbans National Park became a UNESCO World Heritage Site in 1987; it had been declared "
     "a tiger reserve in 1973 and a national park in 1984. Distinguish the three years carefully.",
     "WB Static GK", "1987", "UNESCO World Heritage List"),
    ("GS", "The Damodar Valley Corporation was set up in",
     "1948", "1951", "1955", "1962", 0,
     "The DVC, modelled on the Tennessee Valley Authority of the USA, was established in 1948 as "
     "India's first multipurpose river valley project. It controls floods and generates power in the "
     "Damodar basin.", "WB Static GK", "1948", "DVC Act, 1948"),
    ("GS", "The Durgapur Steel Plant was set up with the collaboration of",
     "the United Kingdom", "the Soviet Union", "Germany", "Japan", 0,
     "Durgapur (1962) was built with British help; Bhilai and Bokaro with the Soviet Union, Rourkela "
     "with Germany, and Salem with Japan. This pairing is a favourite in PSC papers.", "Economy",
     "United Kingdom", "SAIL corporate history"),
    ("GS", "Which social reformer is associated with the Widow Remarriage Act of 1856?",
     "Ishwar Chandra Vidyasagar", "Raja Ram Mohan Roy", "Swami Vivekananda",
     "Keshab Chandra Sen", 0,
     "Vidyasagar's campaign led to the Hindu Widows' Remarriage Act of 1856. Ram Mohan Roy is linked "
     "to the abolition of sati (1829), Vivekananda to the Ramakrishna Mission, and Keshab Chandra Sen "
     "to the Brahmo Samaj of India.", "Modern History", "Ishwar Chandra Vidyasagar",
     "NCERT Class VIII History, Ch. 8"),
    ("GS", "The Young Bengal Movement in Bengal was led by",
     "Henry Vivian Derozio", "David Hare", "Alexander Duff", "William Carey", 0,
     "Henry Vivian Derozio, a teacher at Hindu College, inspired the Young Bengal group in the 1820s "
     "with ideas of rationalism and free enquiry. Hare and Duff were educationists, and Carey was a "
     "Baptist missionary and translator.", "Modern History", "Henry Vivian Derozio",
     "NCERT Class VIII History, Ch. 8"),
    ("GS", "Which district of West Bengal has the largest area?",
     "South 24 Parganas", "Paschim Medinipur", "Bankura", "Jalpaiguri", 0,
     "South 24 Parganas, about 9,960 sq km, is the largest district of West Bengal by area; it also "
     "contains the Indian Sundarbans. Kolkata, at roughly 185 sq km, is the smallest.", "WB Geography",
     "South 24 Parganas", "Census of India, District Handbook"),
    ("GS", "The Quit India Movement was launched in",
     "1942", "1930", "1940", "1946", 0,
     "Gandhiji launched the Quit India Movement on 8 August 1942 from Gowalia Tank Maidan, Bombay, "
     "with the slogan 'Do or Die'. 1930 is the Salt Satyagraha and 1946 the Naval Mutiny.",
     "Modern History", "1942", "NCERT Class VIII History, Ch. 11"),
    ("GS", "Who founded the Arya Samaj?",
     "Swami Dayananda Saraswati", "Swami Vivekananda", "Raja Ram Mohan Roy", "Annie Besant", 0,
     "Swami Dayananda Saraswati founded the Arya Samaj in 1875 at Bombay and gave the call 'Back to "
     "the Vedas'. Vivekananda founded the Ramakrishna Mission (1897) and Besant led the Theosophical "
     "Society.", "Modern History", "Swami Dayananda Saraswati", "NCERT Class VIII History"),
    ("GS", "The Battle of Buxar was fought in",
     "1764", "1757", "1765", "1739", 0,
     "The Battle of Buxar (1764) was won by the English under Hector Munro against Mir Qasim, Shuja-ud"
     "-Daulah and Shah Alam II. It led directly to the grant of the Diwani of Bengal in 1765. Plassey "
     "was 1757.", "Modern History", "1764", "NCERT Class VIII History, Ch. 2"),
    ("GS", "Mohenjo-daro is situated on the bank of which river?",
     "Indus", "Ravi", "Ghaggar", "Saraswati", 0,
     "Mohenjo-daro lies on the right bank of the Indus in Sindh (Pakistan). Harappa is on the Ravi, "
     "and Kalibangan on the Ghaggar. The Great Bath and the Great Granary are Mohenjo-daro's famous "
     "structures.", "Ancient History", "Indus", "NCERT Class VI History, Ch. 3"),
    ("GS", "Who is known as the 'Grand Old Man of India'?",
     "Dadabhai Naoroji", "Gopal Krishna Gokhale", "Bal Gangadhar Tilak", "Surendranath Banerjee", 0,
     "Dadabhai Naoroji, the first Indian elected to the British House of Commons, is called the Grand "
     "Old Man of India. Gokhale was the 'Mahatma' of Indian politics, Tilak the 'Father of Indian "
     "Unrest', and Banerjee the 'Rashtraguru'.", "Modern History", "Dadabhai Naoroji",
     "NCERT Class VIII History"),
    ("GS", "Which state of India has the largest area?",
     "Rajasthan", "Madhya Pradesh", "Maharashtra", "Uttar Pradesh", 0,
     "Rajasthan (3,42,239 sq km) is the largest state by area; Madhya Pradesh is second and "
     "Maharashtra third. Rajasthan is also the largest state by area in India and accounts for about "
     "10.4% of the country's land.", "Indian Geography", "Rajasthan",
     "NCERT Class IX Geography"),
    ("GS", "Which river is called the 'Sorrow of Bihar'?",
     "Kosi", "Gandak", "Son", "Ghaghara", 0,
     "The Kosi, which shifts its course dramatically every few years in north Bihar, is called the "
     "Sorrow of Bihar. The Damodar is the Sorrow of Bengal and the Brahmaputra causes heavy floods in "
     "Assam.", "Indian Geography", "Kosi", "NCERT Class IX Geography"),
    ("GS", "Which Indian port is known as the 'Queen of the Arabian Sea'?",
     "Kochi", "Mumbai", "Mangaluru", "Chennai", 0,
     "Kochi (Cochin) in Kerala, a natural harbour built around the Vembanad lagoon, is called the "
     "Queen of the Arabian Sea. It also has the Indian Navy's Southern Command base, INS Venduruthy.",
     "Indian Geography", "Kochi", "Ministry of Ports, Shipping and Waterways"),
    ("GS", "The highest mountain peak that lies wholly within Indian territory is",
     "Nanda Devi", "Kangchenjunga", "Kamet", "Saltoro Kangri", 0,
     "Nanda Devi (7,816 m) in Uttarakhand is the highest peak standing entirely inside Indian "
     "territory. Kangchenjunga (8,586 m) is taller but sits on the India-Nepal border, and K2 "
     "(8,611 m) lies in Pakistan-occupied Kashmir - so both fail the word 'wholly'.",
     "Indian Geography", "Nanda Devi", "Survey of India"),
    ("GS", "Which soil covers the largest area of India?",
     "alluvial soil", "black soil", "red soil", "laterite soil", 0,
     "Alluvial soil covers roughly 40% of India's area - the entire northern plains and the coastal "
     "deltas. It is rich in potash and lime but poor in nitrogen and humus, and it supports the "
     "densest population.", "Indian Geography", "alluvial", "NCERT Class X Geography, Ch. 1"),
    ("GS", "Fundamental Duties were added to the Constitution by which amendment?",
     "42nd Amendment", "44th Amendment", "73rd Amendment", "52nd Amendment", 0,
     "The 42nd Amendment Act, 1976, inserted Part IV-A (Article 51A) with ten Fundamental Duties on "
     "the recommendation of the Swaran Singh Committee. The 86th Amendment later added the eleventh "
     "duty (education of children).", "Polity", "42nd Amendment",
     "Constitution of India, Part IV-A"),
    ("GS", "The maximum strength of the Lok Sabha as provided in the Constitution is",
     "552", "545", "550", "560", 0,
     "Article 81 allows a maximum of 552 members: 530 from states, 20 from Union Territories and 2 "
     "nominated Anglo-Indians (the nomination lapsed in 2020). The present strength is 545.",
     "Polity", "552", "Constitution of India, Article 81"),
    ("GS", "The Speaker of the Lok Sabha is elected by",
     "the members of the Lok Sabha", "the President", "the Prime Minister", "both Houses of Parliament",
     0,
     "Under Article 93, the Speaker and the Deputy Speaker are elected by the House from among its own "
     "members. The Speaker does not have to resign from the party but must resign his seat; he votes "
     "only to break a tie.", "Polity", "the members of the Lok Sabha",
     "Constitution of India, Article 93"),
    ("GS", "The Election Commission of India is a",
     "constitutional body", "statutory body", "advisory body", "department of the Home Ministry", 0,
     "The Election Commission is established by Article 324 and is therefore a constitutional body. "
     "NITI Aayog is an executive body and the Central Vigilance Commission a statutory one - do not "
     "mix them up.", "Polity", "constitutional body", "Constitution of India, Article 324"),
    ("GS", "The Finance Commission of India is constituted under",
     "Article 280", "Article 324", "Article 356", "Article 148", 0,
     "Article 280 provides for a Finance Commission every five years to recommend the distribution of "
     "tax proceeds between the Union and the states. Article 324 is the Election Commission, 356 "
     "President's rule and 148 the CAG.", "Polity", "Article 280",
     "Constitution of India, Article 280"),
    ("GS", "Which organ of the human body is called the 'master gland'?",
     "pituitary", "thyroid", "adrenal", "pancreas", 0,
     "The pituitary, at the base of the brain, controls the other endocrine glands by secreting "
     "stimulating hormones, so it is called the master gland. The thyroid controls metabolism and the "
     "adrenal glands produce adrenaline and cortisol.", "Biology", "pituitary",
     "NCERT Class X Science, Ch. 7"),
    ("GS", "Which blood group is called the universal donor?",
     "O negative", "AB positive", "A positive", "B negative", 0,
     "O negative red cells carry neither A nor B antigens nor the Rh antigen, so they can be given to "
     "any patient. AB positive is the universal recipient because its plasma has no antibodies.",
     "Biology", "O negative", "NCERT Class X Science"),
    ("GS", "The normal human body temperature is about",
     "37 degrees Celsius", "35 degrees Celsius", "39 degrees Celsius", "40 degrees Celsius", 0,
     "Normal core body temperature is about 37 deg C (98.6 deg F). The hypothalamus regulates it. "
     "Fever is usually taken as above 38 deg C, and hypothermia below 35 deg C.", "Biology",
     "37 degrees Celsius", "NCERT Class X Science"),
    ("GS", "The speed of light in vacuum is approximately",
     "3 x 10^8 m/s", "3 x 10^6 m/s", "3 x 10^10 m/s", "3 x 10^5 m/s", 0,
     "Light travels at about 2.998 x 10^8 m/s, rounded to 3 x 10^8 m/s. That is why sunlight takes "
     "about 8 minutes 20 seconds to reach the Earth, and it is the speed limit of the universe.",
     "Physics", "3 x 10^8 m/s", "NCERT Class X Science, Ch. 10"),
    ("GS", "The SI unit of electrical resistance is",
     "ohm", "ampere", "volt", "watt", 0,
     "Resistance is measured in ohms (the Greek letter omega), from Ohm's law V = IR. Ampere measures "
     "current, volt potential difference and watt power.", "Physics", "ohm",
     "NCERT Class X Science, Ch. 12"),
    ("GS", "Which is the largest planet of the solar system?",
     "Jupiter", "Saturn", "Neptune", "Earth", 0,
     "Jupiter is the largest planet - its mass is about 2.5 times that of all the other planets put "
     "together, and it carries the Great Red Spot. Saturn is second in size, but it overtook Jupiter "
     "in 2023-25 in the number of confirmed moons, so size and moon count are two different "
     "questions.", "Science", "Jupiter", "NASA planetary fact sheets"),
    ("GS", "The Ramsar Convention is associated with the conservation of",
     "wetlands", "deserts", "forests", "marine mammals", 0,
     "The Ramsar Convention (1971, Ramsar in Iran) protects wetlands of international importance. "
     "India has over 80 Ramsar sites, including the East Kolkata Wetlands and the Sundarbans.",
     "Environment", "wetlands", "Ramsar Convention Secretariat"),
    ("GS", "The Montreal Protocol deals with",
     "ozone-depleting substances", "greenhouse gases", "biodiversity", "hazardous waste", 0,
     "The Montreal Protocol (1987) phases out CFCs and other ozone-depleting substances. Greenhouse "
     "gases are covered by the Kyoto Protocol and the Paris Agreement, biodiversity by the CBD, and "
     "hazardous waste by the Basel Convention.", "Environment", "ozone-depleting substances",
     "UNEP Montreal Protocol"),
    ("GS", "India's First Five Year Plan was launched in",
     "1951", "1947", "1956", "1961", 0,
     "The First Five Year Plan ran from 1951 to 1956 and concentrated on agriculture and irrigation, "
     "following the Harrod-Domar model. The Planning Commission itself was set up in 1950, and the "
     "Second Plan (1956-61) shifted focus to heavy industry.", "Economy", "1951",
     "Planning Commission archives"),
    ("GS", "The National Food Security Act was passed in",
     "2013", "2011", "2015", "2009", 0,
     "The NFSA, 2013, gives legal entitlement to subsidised foodgrain to about two-thirds of the "
     "population under the Antyodaya and priority-household categories. It is implemented through "
     "the PDS.", "Economy", "2013", "NFSA, 2013"),
    ("GS", "Which city will host the 2028 Summer Olympics?",
     "Los Angeles", "Paris", "Brisbane", "Tokyo", 0,
     "Los Angeles will host the 2028 Summer Olympics, after Paris 2024. Brisbane hosts in 2032. LA "
     "previously hosted the Games in 1932 and 1984.", "Current Affairs", "Los Angeles",
     "International Olympic Committee"),
    ("GS", "The 2026 Asian Games were held in",
     "Aichi-Nagoya, Japan", "Hangzhou, China", "Jakarta, Indonesia", "Doha, Qatar", 0,
     "The 20th Asian Games, Aichi-Nagoya 2026, run from 19 September to 4 October 2026 in Japan. "
     "Hangzhou hosted in 2023 (held in 2023 after a delay) and Jakarta in 2018.", "Current Affairs",
     "Aichi-Nagoya, Japan", "Olympic Council of Asia / media reports, September 2026"),
    ("GS", "Where was the final of the ICC Men's T20 World Cup 2026 played?",
     "Ahmedabad", "Kolkata", "Colombo", "Mumbai", 0,
     "The final was played at the Narendra Modi Stadium, Ahmedabad, on 8 March 2026, where India beat "
     "New Zealand by 96 runs. India and Sri Lanka co-hosted the tournament.", "Current Affairs",
     "Ahmedabad", "ICC / media reports, March 2026"),
    ("GS", "At the Commonwealth Games 2026, India finished",
     "fourth", "second", "third", "sixth", 0,
     "India finished fourth at Glasgow 2026 with 39 medals - 13 gold, 17 silver and 9 bronze - behind "
     "Australia, England and Canada. Boxing gave India its highest haul, with 7 golds.",
     "Current Affairs", "fourth", "CGF / media reports, August 2026"),
    ("GS", "Which country topped the medal table at the 2026 Winter Olympics?",
     "Norway", "United States", "Germany", "Italy", 0,
     "Norway topped the Milano-Cortina 2026 table with 18 golds and 41 medals, followed by the USA "
     "(12 golds) and the Netherlands (10 golds). The Games ran from 6 to 22 February 2026 in Italy.",
     "Current Affairs", "Norway", "IOC / media reports, February 2026"),
    ("GS", "Which party formed the government in West Bengal after the 2026 Assembly election?",
     "Bharatiya Janata Party", "All India Trinamool Congress", "Indian National Congress",
     "Communist Party of India (Marxist)", 0,
     "The BJP won a majority in the 2026 West Bengal Assembly election, ending 15 years of Trinamool "
     "Congress rule, and Suvendu Adhikari was sworn in as Chief Minister on 9 May 2026.",
     "Current Affairs", "Bharatiya Janata Party", "Election Commission of India / media, May 2026"),
    ("GS", "Who is the present Chief Election Commissioner of India?",
     "Gyanesh Kumar", "Rajiv Kumar", "Sushil Chandra", "Sunil Arora", 0,
     "Gyanesh Kumar took charge as the Chief Election Commissioner on 19 February 2025. The CEC heads "
     "the three-member Election Commission, a constitutional body under Article 324.",
     "Current Affairs", "Gyanesh Kumar", "Election Commission of India; '2026 in India'"),
    ("GS", "Who is the present Finance Minister of India?",
     "Nirmala Sitharaman", "Piyush Goyal", "Amit Shah", "Nitin Gadkari", 0,
     "Nirmala Sitharaman has been the Union Finance Minister since 31 May 2019 and presented her "
     "ninth consecutive Union Budget on 1 February 2026, the longest continuous run by any Finance "
     "Minister. She is India's first full-time woman Finance Minister.", "Current Affairs",
     "Nirmala Sitharaman", "Ministry of Finance, Budget 2026-27"),

    # ----------------------------------------------------------------- ARITHMETIC
    ("AR", "Simplify: 0.75 + 0.25 x 2.4",
     "1.35", "1.30", "1.40", "1.25", 0,
     "Step 1: Multiplication before addition (BODMAS): 0.25 x 2.4 = 0.6. Step 2: 0.75 + 0.6 = 1.35. "
     "The common mistake is to add 0.75 + 0.25 first, which gives a wrong 2.4.", "Decimals",
     "0.75 + 0.25*2.4"),
    ("AR", "The recurring decimal 0.444... is equal to the fraction",
     "4/9", "2/5", "4/11", "1/2", 0,
     "Step 1: Let x = 0.444... Step 2: 10x = 4.444..., so 10x - x = 4. Step 3: 9x = 4, hence x = 4/9. "
     "Rule: a single repeating digit d is d/9; two repeating digits give a multiple of 1/99.",
     "Recurring decimals", "4/9"),
    ("AR", "The HCF of 36, 60 and 84 is",
     "12", "6", "18", "24", 0,
     "Step 1: 36 = 2^2 x 3^2, 60 = 2^2 x 3 x 5, 84 = 2^2 x 3 x 7. Step 2: Take the common factors "
     "with the lowest powers: 2^2 x 3. Step 3: 4 x 3 = 12.", "HCF and LCM", "math.gcd(36, math.gcd(60, 84))"),
    ("AR", "The LCM of 12, 15 and 20 is",
     "60", "120", "180", "90", 0,
     "Step 1: 12 = 2^2 x 3, 15 = 3 x 5, 20 = 2^2 x 5. Step 2: Take every prime with the highest power: "
     "2^2 x 3 x 5. Step 3: 4 x 3 x 5 = 60.", "HCF and LCM", "60"),
    ("AR", "Two numbers are in the ratio 5 : 7 and their difference is 24. The smaller number is",
     "60", "84", "48", "72", 0,
     "Step 1: Let the numbers be 5x and 7x; difference = 2x = 24. Step 2: x = 12. Step 3: Smaller = 5x "
     "= 60 (the larger is 84).", "Ratio", "5*24/2"),
    ("AR", "The average of six numbers is 15. When one number, 20, is removed, the average of the "
     "remaining five is",
     "14", "13", "15", "12", 0,
     "Step 1: Sum of six numbers = 6 x 15 = 90. Step 2: After removing 20 the sum is 70 for 5 numbers. "
     "Step 3: New average = 70/5 = 14.", "Average", "(6*15-20)/5"),
    ("AR", "A number increased by 20% becomes 360. The original number is",
     "300", "288", "320", "280", 0,
     "Step 1: Let the number be x; then 1.20x = 360. Step 2: x = 360/1.20. Step 3: x = 300. Check: 20% "
     "of 300 is 60, and 300 + 60 = 360.", "Percentage", "360/1.2"),
    ("AR", "A sum of money earns a simple interest of Rs 1,200 at 5% per annum in 3 years. The sum is",
     "Rs 8,000", "Rs 6,000", "Rs 7,500", "Rs 9,000", 0,
     "Step 1: SI = P x R x T/100, so P = SI x 100/(R x T). Step 2: P = 1200 x 100/(5 x 3). Step 3: P "
     "= 1,20,000/15 = Rs 8,000.", "Simple interest", "1200*100/(5*3)"),
    ("AR", "An article costing Rs 250 is sold at a loss of 8%. The selling price is",
     "Rs 230", "Rs 232", "Rs 228", "Rs 235", 0,
     "Step 1: Loss = 8% of 250 = 0.08 x 250 = 20. Step 2: SP = CP - loss = 250 - 20. Step 3: SP = Rs "
     "230. (Shortcut: SP = CP x 0.92.)", "Profit and loss", "250*0.92"),
    ("AR", "Successive discounts of 20% and 10% are given on an article marked at Rs 500. The price "
     "paid is",
     "Rs 360", "Rs 350", "Rs 370", "Rs 340", 0,
     "Step 1: After the first discount, price = 500 x 0.80 = 400. Step 2: The second discount is on the "
     "reduced price: 400 x 0.90 = 360. Step 3: Price paid = Rs 360. (Do not add 20% + 10% = 30%. The "
     "single equivalent discount here is 28%.)", "Discount", "500*0.8*0.9"),
    ("AR", "A man covers 6 km at 4 km/h and another 6 km at 6 km/h. His average speed for the whole "
     "journey is",
     "4.8 km/h", "5 km/h", "4.5 km/h", "5.2 km/h", 0,
     "Step 1: Time for the first part = 6/4 = 1.5 h; second part = 6/6 = 1 h. Step 2: Total distance "
     "12 km, total time 2.5 h. Step 3: Average speed = 12/2.5 = 4.8 km/h. (For equal distances, the "
     "average is the harmonic mean, not 5.)", "Speed and distance", "12/(6/4+6/6)"),
    ("AR", "A train 200 m long, running at 72 km/h, crosses a signal post in",
     "10 seconds", "12 seconds", "8 seconds", "15 seconds", 0,
     "Step 1: Convert speed: 72 x 5/18 = 20 m/s. Step 2: To cross a post (a point) the train covers "
     "only its own length, 200 m. Step 3: Time = 200/20 = 10 seconds.", "Trains",
     "200/(72*5/18)"),
    ("AR", "A and B together finish a work in 10 days; A alone takes 15 days. B alone will take",
     "30 days", "25 days", "20 days", "35 days", 0,
     "Step 1: Together one day = 1/10; A one day = 1/15. Step 2: B one day = 1/10 - 1/15 = (3 - 2)/30 "
     "= 1/30. Step 3: B alone takes 30 days.", "Time and work", "1/(1/10-1/15)"),
    ("AR", "A pipe fills a tank in 12 hours and a drain empties it in 20 hours. If both are opened "
     "when the tank is empty, it will be full in",
     "30 hours", "24 hours", "32 hours", "36 hours", 0,
     "Step 1: Filling rate = 1/12, emptying rate = 1/20. Step 2: Net rate = 1/12 - 1/20 = (5 - 3)/60 = "
     "2/60 = 1/30. Step 3: Time = 30 hours.", "Pipes and cisterns", "1/(1/12-1/20)"),
    ("AR", "A boat covers 30 km downstream in 2 hours. If the speed of the stream is 3 km/h, the "
     "speed of the boat in still water is",
     "12 km/h", "15 km/h", "10 km/h", "18 km/h", 0,
     "Step 1: Downstream speed = 30/2 = 15 km/h. Step 2: Downstream = still water + stream, so still "
     "water = 15 - 3. Step 3: 12 km/h. (Upstream speed would then be 12 - 3 = 9 km/h.)",
     "Boats and streams", "30/2 - 3"),
    ("AR", "A father is four times as old as his son. After 10 years he will be twice as old as his "
     "son. The son's present age is",
     "5 years", "10 years", "8 years", "6 years", 0,
     "Step 1: Let the son be x and the father 4x. Step 2: After 10 years, 4x + 10 = 2(x + 10), so 4x + "
     "10 = 2x + 20. Step 3: 2x = 10, x = 5 years. Check: father 20, after 10 years 30 = 2 x 15.",
     "Ages", "10/(4-2)"),
    ("AR", "The angle between the hands of a clock at 4:20 is",
     "10 degrees", "0 degrees", "20 degrees", "30 degrees", 0,
     "Step 1: Hour hand = 4 x 30 + 20 x 0.5 = 120 + 10 = 130 deg. Step 2: Minute hand = 20 x 6 = 120 "
     "deg. Step 3: Difference = 10 degrees.", "Clocks", "abs(20*6 - (4*30 + 20*0.5))"),
    ("AR", "If 1 January 2027 is a Friday, then 1 February 2027 is a",
     "Monday", "Sunday", "Tuesday", "Saturday", 0,
     "Step 1: January has 31 days, and 31 = 4 x 7 + 3. Step 2: So 1 February is 3 days after Friday. "
     "Step 3: Friday + 3 = Monday.", "Calendar", "fact:Monday"),
    ("AR", "The area of a square whose perimeter is 48 m is",
     "144 sq m", "576 sq m", "196 sq m", "121 sq m", 0,
     "Step 1: Side = perimeter/4 = 48/4 = 12 m. Step 2: Area = side x side = 12 x 12. Step 3: 144 sq "
     "m. (576 sq m is the trap - that is the square of the perimeter.)", "Area", "(48/4)**2"),
    ("AR", "The length of the diagonal of a rectangle of sides 15 cm and 8 cm is",
     "17 cm", "23 cm", "16 cm", "19 cm", 0,
     "Step 1: The diagonal forms a right triangle with the two sides. Step 2: d = sqrt(15^2 + 8^2) = "
     "sqrt(225 + 64) = sqrt(289). Step 3: d = 17 cm (the 8-15-17 triple).", "Area",
     "math.hypot(15, 8)"),
    ("AR", "How many of the numbers 4563, 1234, 5678 and 2345 are divisible by 9?",
     "1", "2", "3", "0", 0,
     "Step 1: A number is divisible by 9 only if its digit sum is divisible by 9. Step 2: The digit "
     "sums are 4+5+6+3 = 18 (divisible), 1+2+3+4 = 10, 5+6+7+8 = 26 and 2+3+4+5 = 14. Step 3: Only "
     "4563 qualifies (4563/9 = 507), so exactly 1 of the four numbers is divisible by 9.",
     "Divisibility",
     "sum(1 for n in (4563, 1234, 5678, 2345) if n % 9 == 0)"),
    ("AR", "Simplify: (0.6^3 + 0.4^3) / (0.6^2 - 0.6 x 0.4 + 0.4^2)",
     "1", "0.2", "10", "0.1", 0,
     "Step 1: Use the identity a^3 + b^3 = (a + b)(a^2 - ab + b^2). Step 2: The denominator is exactly "
     "(a^2 - ab + b^2), so the expression reduces to a + b. Step 3: 0.6 + 0.4 = 1.",
     "Simplification", "(0.6**3 + 0.4**3)/(0.6**2 - 0.6*0.4 + 0.4**2)"),
    ("AR", "A invests Rs 4,000 for 12 months and B invests Rs 6,000 for 8 months. In a profit of "
     "Rs 2,400, A's share is",
     "Rs 1,200", "Rs 1,400", "Rs 1,000", "Rs 1,600", 0,
     "Step 1: Capital x time: A = 4000 x 12 = 48,000; B = 6000 x 8 = 48,000. Step 2: Ratio = 1 : 1. "
     "Step 3: A's share = 2400 x 1/2 = Rs 1,200.", "Partnership",
     "2400*4000*12/(4000*12+6000*8)"),
    ("AR", "A 60-litre mixture contains milk and water in the ratio 2 : 1. If 12 litres of water is "
     "added, the new ratio of milk to water is",
     "5 : 4", "2 : 1", "5 : 3", "4 : 3", 0,
     "Step 1: Milk = 2/3 x 60 = 40 L; water = 1/3 x 60 = 20 L. Step 2: Water becomes 20 + 12 = 32 L "
     "while milk stays 40 L. Step 3: Ratio = 40 : 32 = 5 : 4.", "Mixture", "40/32"),
    ("AR", "15% of 20% of 500 is",
     "15", "75", "30", "20", 0,
     "Step 1: 20% of 500 = 100. Step 2: 15% of 100 = 15. Step 3: Answer 15. (Multiplying 15 x 20 = "
     "300 and taking 300/100 of 500 gives the same: 15.)", "Percentage", "0.15*0.20*500"),
    ("AR", "The average of the first 15 odd numbers is",
     "15", "8", "30", "7.5", 0,
     "Step 1: The first n odd numbers are 1, 3, 5, ..., (2n - 1). Step 2: Their sum is n^2 = 225 for n "
     "= 15. Step 3: Average = 225/15 = 15, and in general the average of the first n odd numbers is n.",
     "Average", "sum(range(1, 30, 2))/15"),
    ("AR", "The difference between the compound interest and the simple interest on Rs 1,000 at 10% "
     "per annum for 2 years is",
     "Rs 10", "Rs 20", "Rs 5", "Rs 15", 0,
     "Step 1: SI = 1000 x 10 x 2/100 = Rs 200. Step 2: CI = 1000 x (1.1)^2 - 1000 = 1210 - 1000 = Rs "
     "210. Step 3: Difference = 10. Shortcut for 2 years: difference = P x (r/100)^2 = 1000 x 0.01 = "
     "Rs 10.", "Compound interest", "1000*1.1**2 - 1000 - 1000*10*2/100"),
    ("AR", "What fraction of a day is 4 hours 48 minutes?",
     "1/5", "1/4", "1/6", "2/9", 0,
     "Step 1: 4 h 48 min = 4 x 60 + 48 = 288 minutes. Step 2: One day = 24 x 60 = 1,440 minutes. Step "
     "3: 288/1440 = 1/5.", "Fractions", "288/1440"),
    ("AR", "The smallest number that must be added to 1,234 to make it divisible by 9 is",
     "8", "7", "6", "5", 0,
     "Step 1: Digit sum of 1234 = 1 + 2 + 3 + 4 = 10. Step 2: The next multiple of 9 after 10 is 18. "
     "Step 3: 18 - 10 = 8, so 1234 + 8 = 1242 and 1242/9 = 138.", "Divisibility", "9 - 1234%9"),
    ("AR", "The ratio of the areas of two squares whose sides are 3 cm and 5 cm is",
     "9 : 25", "3 : 5", "9 : 16", "9 : 20", 0,
     "Step 1: Area of a square = side^2, so the areas are 9 and 25 sq cm. Step 2: Ratio = 9 : 25. Step "
     "3: Note that the ratio of areas is the square of the ratio of sides (3 : 5), not the ratio "
     "itself.", "Area", "9/25"),
]

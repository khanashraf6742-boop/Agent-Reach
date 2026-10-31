# -*- coding: utf-8 -*-
"""General Studies datasets for the eight Part-I papers.

Each dataset is a table of facts. A question is generated from a row and the three
distractors come from the same column of the same table, so the key is never typed twice:
the paper and the validator both read the table. That is what makes the answer checkable
against an independent representation rather than against itself.
"""

ARTICLES = """
Article 14|equality before law
Article 15|prohibition of discrimination on grounds of religion, race, caste, sex or place of birth
Article 16|equality of opportunity in public employment
Article 17|abolition of untouchability
Article 18|abolition of titles
Article 19|protection of six freedoms including speech and expression
Article 20|protection in respect of conviction for offences
Article 21|protection of life and personal liberty
Article 21A|right to education for children between six and fourteen years
Article 22|protection against arrest and detention
Article 23|prohibition of traffic in human beings and forced labour
Article 24|prohibition of employment of children below fourteen years
Article 25|freedom of conscience and free profession of religion
Article 26|freedom to manage religious affairs
Article 27|freedom from taxation for the promotion of any religion
Article 28|freedom from religious instruction in certain institutions
Article 29|protection of the interests of minorities
Article 30|right of minorities to establish and administer educational institutions
Article 32|right to constitutional remedies for the enforcement of fundamental rights
Article 40|organisation of village panchayats
Article 44|uniform civil code
Article 48A|protection and improvement of the environment
Article 51A|fundamental duties of citizens
Article 72|pardoning power of the President
Article 74|Council of Ministers to aid and advise the President
Article 76|Attorney General of India
Article 110|definition of a Money Bill
Article 112|annual financial statement or budget
Article 123|ordinance-making power of the President
Article 143|advisory jurisdiction of the Supreme Court
Article 148|Comptroller and Auditor General of India
Article 155|appointment of the Governor
Article 161|pardoning power of the Governor
Article 163|Council of Ministers to aid and advise the Governor
Article 165|Advocate General of a State
Article 226|writ jurisdiction of the High Courts
Article 243|constitution of panchayats
Article 280|Finance Commission
Article 300A|right to property as a legal right
Article 312|All India Services
Article 324|Election Commission of India
Article 356|imposition of President's rule in a State
Article 368|procedure for amendment of the Constitution
Article 370|special provisions for Jammu and Kashmir
"""

OFFICES = """
Who administers the oath of office to the President of India?|Chief Justice of India|Vice-President of India,Speaker of the Lok Sabha,Attorney General of India|Article 60 requires the Chief Justice of India to administer the oath to the President.
Who administers the oath of office to a Governor?|Chief Justice of the High Court|Chief Justice of India,President of India,Speaker of the State Assembly|The Chief Justice of the High Court of the State administers the oath to the Governor.
The Vice-President of India is elected by|the members of both Houses of Parliament|the members of the Lok Sabha only,the State Legislative Assemblies,the Council of Ministers|Article 66 provides an electoral college of the elected and nominated members of both Houses of Parliament.
Who is the ex-officio Chairman of the Rajya Sabha?|Vice-President of India|President of India,Speaker of the Lok Sabha,Deputy Chairman of the Rajya Sabha|Article 64 makes the Vice-President the ex-officio Chairman of the Rajya Sabha.
The Speaker of the Lok Sabha is elected by|the members of the Lok Sabha|the members of both Houses,the President,the Council of Ministers|Article 93: the Lok Sabha chooses its Speaker from among its own members.
What is the maximum strength of the Lok Sabha provided by the Constitution?|552|545,500,600|Article 81 caps the House at 552: up to 530 from the States, 20 from Union Territories and 2 nominated Anglo-Indians.
The term of office of a member of the Rajya Sabha is|six years|five years,four years,three years|Article 83 fixes six years, with one third of the House retiring every two years.
The normal term of the Lok Sabha is|five years|four years,six years,seven years|Article 83 fixes five years from the first sitting, unless the House is dissolved earlier.
The minimum age to become President of India is|35 years|30 years,25 years,40 years|Article 58 requires 35 years of age, besides eligibility for election to the Lok Sabha.
The minimum age to become a member of the Lok Sabha is|25 years|21 years,30 years,35 years|Article 84 sets 25 years as the minimum age for the Lok Sabha.
The minimum age to become a member of the Rajya Sabha is|30 years|25 years,21 years,35 years|Article 84 sets 30 years as the minimum age for the Rajya Sabha.
Who appoints the Chief Election Commissioner of India?|President of India|Prime Minister,Chief Justice of India,Parliament|Article 324: the Chief Election Commissioner is appointed by the President.
The Finance Commission is constituted|every five years|every year,every ten years,only once|Article 280 requires a Finance Commission to be constituted every five years.
Which Schedule of the Constitution deals with anti-defection?|Tenth Schedule|Ninth Schedule,Eighth Schedule,Eleventh Schedule|The Tenth Schedule, inserted in 1985, disqualifies members who defect from their party.
Which Schedule of the Constitution lists the recognised languages?|Eighth Schedule|Seventh Schedule,Ninth Schedule,Tenth Schedule|The Eighth Schedule lists the recognised languages; it began with 14 and now contains 22.
How many fundamental duties are listed in the Constitution?|eleven|ten,eight,twelve|Article 51A lists eleven duties; the eleventh was added by the 86th Amendment in 2002.
The Directive Principles of State Policy are contained in|Part IV|Part III,Part V,Part II|Articles 36 to 51 in Part IV contain the Directive Principles of State Policy.
The Fundamental Rights are contained in|Part III|Part IV,Part II,Part V|Articles 12 to 35 in Part III contain the Fundamental Rights.
Which body is called the guardian of the Constitution?|the Supreme Court|the President,the Parliament,the Election Commission|The Supreme Court guards the Constitution and can strike down action that violates it.
The writ of habeas corpus requires the authorities to|produce the detained person before a court|stay a lower court's order,forbid an act of a public body,transfer a case to another court|Habeas corpus means 'to have the body'; the court orders that the detained person be produced before it.
A Money Bill can be introduced only in|the Lok Sabha|the Rajya Sabha,either House,a joint sitting|Article 110 requires a Money Bill to originate in the Lok Sabha, on the President's recommendation.
Who presides over a joint sitting of both Houses of Parliament?|the Speaker of the Lok Sabha|the Vice-President,the President,the senior-most member|Article 108: the Speaker of the Lok Sabha presides over a joint sitting of the two Houses.
The Constitution of India was adopted on|26 November 1949|26 January 1950,15 August 1947,26 January 1949|The Constituent Assembly adopted the Constitution on 26 November 1949, now observed as Constitution Day.
The Constitution of India came into force on|26 January 1950|26 November 1949,15 August 1947,1 January 1950|It came into force on 26 January 1950, a date chosen to honour the Lahore resolution of 1930.
Who appoints the Governor of a State?|President of India|Chief Minister,Prime Minister,Chief Justice of India|Article 155: the Governor is appointed by the President and is not elected.
The Governor holds office|during the pleasure of the President|for a fixed term of six years,for five years and cannot be removed,at the pleasure of the Chief Minister|Article 156: the Governor holds office during the pleasure of the President.
"""

CAPITALS = """
Andhra Pradesh|Amaravati
Arunachal Pradesh|Itanagar
Assam|Dispur
Bihar|Patna
Chhattisgarh|Raipur
Goa|Panaji
Gujarat|Gandhinagar
Haryana|Chandigarh
Himachal Pradesh|Shimla
Jharkhand|Ranchi
Karnataka|Bengaluru
Kerala|Thiruvananthapuram
Madhya Pradesh|Bhopal
Maharashtra|Mumbai
Manipur|Imphal
Meghalaya|Shillong
Mizoram|Aizawl
Nagaland|Kohima
Odisha|Bhubaneswar
Rajasthan|Jaipur
Sikkim|Gangtok
Tamil Nadu|Chennai
Telangana|Hyderabad
Tripura|Agartala
Uttar Pradesh|Lucknow
West Bengal|Kolkata
"""

RIVERS = """
Ganga|the Gangotri glacier in Uttarakhand
Yamuna|the Yamunotri glacier in Uttarakhand
Brahmaputra|the Chemayungdung glacier near Lake Mansarovar
Indus|the Tibetan plateau near Lake Mansarovar
Godavari|Trimbakeshwar in the Nashik district of Maharashtra
Krishna|Mahabaleshwar in the Satara district of Maharashtra
Narmada|Amarkantak in Madhya Pradesh
Tapti|Multai in Madhya Pradesh
Mahanadi|Sihawa in Chhattisgarh
Kaveri|Talakaveri in Karnataka
Damodar|the Chota Nagpur plateau in Jharkhand
Teesta|the Tso Lhamo lake in Sikkim
Son|Amarkantak in Madhya Pradesh
Beas|Beas Kund in Himachal Pradesh
Ravi|the Chamba district of Himachal Pradesh
Sutlej|Rakas Tal on the Tibetan plateau
Chenab|the Bara Lacha La pass in Himachal Pradesh
Jhelum|Verinag in the Kashmir valley
Ghaghara|the Mapchachungo glacier in Nepal
Gandak|the Nepal Himalaya
"""

PARKS = """
Kaziranga|Assam
Manas|Assam
Sundarbans|West Bengal
Buxa|West Bengal
Namdapha|Arunachal Pradesh
Keibul Lamjao|Manipur
Gir|Gujarat
Kanha|Madhya Pradesh
Bandhavgarh|Madhya Pradesh
Pench|Madhya Pradesh
Ranthambore|Rajasthan
Sariska|Rajasthan
Corbett|Uttarakhand
Valley of Flowers|Uttarakhand
Bandipur|Karnataka
Nagarhole|Karnataka
Periyar|Kerala
Eravikulam|Kerala
Simlipal|Odisha
Desert National Park|Rajasthan
"""

YEARS = """
1757|the Battle of Plassey
1764|the Battle of Buxar
1857|the Revolt of 1857
1885|the founding of the Indian National Congress
1905|the first Partition of Bengal
1911|the annulment of the Partition of Bengal
1913|the award of the Nobel Prize in Literature to Rabindranath Tagore
1919|the Jallianwala Bagh massacre
1920|the launch of the Non-Cooperation Movement
1922|the Chauri Chaura incident
1927|the appointment of the Simon Commission
1929|the Lahore session of the Congress and the Purna Swaraj resolution
1930|the Dandi March
1931|the Gandhi-Irwin Pact
1932|the Poona Pact
1935|the Government of India Act
1942|the Quit India Movement
1943|the Bengal famine
1946|the Cabinet Mission
1947|India's independence and Partition
1950|the coming into force of the Constitution
1951|the launching of the First Five Year Plan
1956|the States Reorganisation Act
1961|the liberation of Goa
1962|the Sino-Indian war
1965|the Indo-Pak war
1971|the Indo-Pak war that led to the creation of Bangladesh
1974|the Pokhran-I nuclear test
1975|the declaration of the Emergency
1983|India's first Cricket World Cup win
1984|the assassination of Indira Gandhi
1991|the beginning of economic liberalisation
1998|the Pokhran-II nuclear tests
2008|the launch of Chandrayaan-1
2011|the Census of India
2014|the formation of Telangana
2016|the demonetisation of high-value currency notes
2017|the introduction of the Goods and Services Tax
2019|the abrogation of Article 370
2023|the soft landing of Chandrayaan-3
2024|the Summer Olympics in Paris
"""

PERSONALITIES = """
Who founded the Indian National Congress in 1885?|A. O. Hume|Bal Gangadhar Tilak,Gopal Krishna Gokhale,Dadabhai Naoroji|A. O. Hume, a retired civil servant, founded the Congress in 1885; W. C. Bonnerjee was its first president.
Who gave the slogan 'Give me blood and I will give you freedom'?|Subhas Chandra Bose|Bhagat Singh,Jawaharlal Nehru,Lala Lajpat Rai|Subhas Chandra Bose gave the slogan in 1944 while leading the Indian National Army.
Who is known as the 'Father of the Indian Constitution'?|B. R. Ambedkar|Jawaharlal Nehru,Rajendra Prasad,Sardar Patel|B. R. Ambedkar chaired the Drafting Committee of the Constituent Assembly.
Who led the Bardoli Satyagraha of 1928?|Vallabhbhai Patel|Mahatma Gandhi,Rajendra Prasad,C. Rajagopalachari|Vallabhbhai Patel led the Bardoli satyagraha of 1928 and earned the title Sardar.
Who founded the Brahmo Samaj?|Raja Ram Mohan Roy|Swami Vivekananda,Ishwar Chandra Vidyasagar,Sri Aurobindo|Raja Ram Mohan Roy founded the Brahmo Sabha in 1828, which became the Brahmo Samaj.
Who founded the Arya Samaj?|Swami Dayananda Saraswati|Raja Ram Mohan Roy,Keshab Chandra Sen,Debendranath Tagore|Swami Dayananda Saraswati founded the Arya Samaj in 1875 and called for a return to the Vedas.
Who wrote 'Gitanjali'?|Rabindranath Tagore|Bankim Chandra Chatterjee,Sarat Chandra Chattopadhyay,Kazi Nazrul Islam|Rabindranath Tagore wrote Gitanjali, which won him the Nobel Prize in Literature in 1913.
Who wrote the novel 'Anandamath'?|Bankim Chandra Chatterjee|Rabindranath Tagore,Sarat Chandra Chattopadhyay,Michael Madhusudan Dutt|Bankim Chandra Chatterjee wrote Anandamath in 1882; it contains the song Vande Mataram.
Who is called the 'Father of the Indian Renaissance'?|Raja Ram Mohan Roy|Swami Vivekananda,Rabindranath Tagore,Ishwar Chandra Vidyasagar|Raja Ram Mohan Roy is called the father of the Indian Renaissance for his social and religious reforms.
Who founded the Ramakrishna Mission?|Swami Vivekananda|Ramakrishna Paramahamsa,Dayananda Saraswati,Sri Aurobindo|Swami Vivekananda founded the Ramakrishna Mission in 1897.
Who led the Salt Satyagraha at Dandi?|Mahatma Gandhi|Sardar Patel,Jawaharlal Nehru,Rajendra Prasad|Mahatma Gandhi led the Dandi march in 1930 to break the government's salt monopoly.
Who was the first Prime Minister of India?|Jawaharlal Nehru|Sardar Patel,Rajendra Prasad,Lal Bahadur Shastri|Jawaharlal Nehru was Prime Minister from 1947 until 1964.
Who was the first President of India?|Rajendra Prasad|Jawaharlal Nehru,S. Radhakrishnan,Zakir Husain|Rajendra Prasad was President of India from 1950 to 1962.
Who was the first woman Chief Minister of West Bengal?|Mamata Banerjee|Sucheta Kripalani,Pratibha Singh,Arati Saha|Mamata Banerjee became the first woman Chief Minister of West Bengal in 2011.
Who founded the Servants of India Society?|Gopal Krishna Gokhale|Bal Gangadhar Tilak,Lala Lajpat Rai,Bipin Chandra Pal|Gopal Krishna Gokhale founded the Servants of India Society in 1905.
Who is known as 'Punjab Kesari'?|Lala Lajpat Rai|Bal Gangadhar Tilak,Bipin Chandra Pal,Subhas Chandra Bose|Lala Lajpat Rai was called Punjab Kesari; he died in 1928 after a police lathi charge.
Who is known as 'Lokmanya'?|Bal Gangadhar Tilak|Gopal Krishna Gokhale,Lala Lajpat Rai,Mahatma Gandhi|Bal Gangadhar Tilak was called Lokmanya; he gave the slogan 'Swaraj is my birthright'.
Who founded the Indian Association in 1876?|Surendranath Banerjee|A. O. Hume,Anand Mohan Bose,W. C. Bonnerjee|Surendranath Banerjee founded the Indian Association in 1876, a forerunner of the Congress.
Who was the first woman President of the Indian National Congress?|Annie Besant|Sarojini Naidu,Vijaya Lakshmi Pandit,Kasturba Gandhi|Annie Besant was the first woman president of the Congress, in 1917.
Who wrote 'Gora'?|Rabindranath Tagore|Bankim Chandra Chatterjee,Sarat Chandra Chattopadhyay,Manik Bandopadhyay|Rabindranath Tagore wrote the novel Gora, published in 1910.
Who is known as the 'Iron Man of India'?|Vallabhbhai Patel|Jawaharlal Nehru,B. R. Ambedkar,Rajendra Prasad|Vallabhbhai Patel integrated the princely states and is called the Iron Man of India.
Who founded the Indian National Army?|Subhas Chandra Bose|Bhagat Singh,Chandrashekhar Azad,Rash Behari Bose|Subhas Chandra Bose reorganised the Indian National Army in 1943.
Who was the first Governor-General of independent India?|Lord Mountbatten|C. Rajagopalachari,Lord Wavell,Rajendra Prasad|Lord Mountbatten was the first Governor-General of independent India, serving from 1947 to 1948.
Who coined the term 'Satyagraha'?|Mahatma Gandhi|Rabindranath Tagore,Gopal Krishna Gokhale,Jawaharlal Nehru|Mahatma Gandhi coined satyagraha, meaning holding fast to truth, during the South African struggle.
"""

UNITS = """
length|metre
mass|kilogram
time|second
electric current|ampere
thermodynamic temperature|kelvin
amount of substance|mole
luminous intensity|candela
force|newton
energy|joule
power|watt
pressure|pascal
frequency|hertz
electric charge|coulomb
potential difference|volt
electrical resistance|ohm
magnetic flux|weber
sound level|decibel
radioactivity|becquerel
"""

VITAMINS = """
vitamin A|night blindness
vitamin B1|beriberi
vitamin B2|inflammation of the tongue
vitamin B3|pellagra
vitamin B12|pernicious anaemia
vitamin C|scurvy
vitamin D|rickets
vitamin K|delayed clotting of blood
iron|anaemia
iodine|goitre
calcium|weak bones and teeth
protein|kwashiorkor
"""

SCIENCE_QA = """
What is the chemical formula of common salt?|NaCl|KCl,CaCO3,NaHCO3|Common salt is sodium chloride, whose formula is NaCl.
Which gas is most abundant in the earth's atmosphere?|nitrogen|oxygen,carbon dioxide,argon|Nitrogen makes up about 78 per cent of the atmosphere; oxygen about 21 per cent.
Which gas do plants absorb during photosynthesis?|carbon dioxide|oxygen,nitrogen,hydrogen|Plants take in carbon dioxide and release oxygen during photosynthesis.
What is the hardest naturally occurring substance?|diamond|quartz,granite,iron|Diamond, a crystalline form of carbon, is the hardest natural substance on Mohs scale 10.
Which instrument is used to measure blood pressure?|sphygmomanometer|barometer,thermometer,hygrometer|Blood pressure is measured with a sphygmomanometer; a barometer measures atmospheric pressure.
What is the approximate speed of light in vacuum?|3 x 10^8 metre per second|3 x 10^6 metre per second,3 x 10^10 metre per second,3 x 10^5 metre per second|Light travels at about 3 x 10^8 metre per second in vacuum.
What is the pH of pure water at 25 degrees Celsius?|seven|zero,fourteen,one|Pure water is neutral, with a pH of 7 at 25 degrees Celsius.
Which is the largest gland in the human body?|liver|pancreas,thyroid,spleen|The liver is the largest gland; it secretes bile and detoxifies the blood.
How many bones are there in the adult human body?|206|300,256,186|An adult human skeleton has 206 bones; a newborn has about 300.
Who discovered the human blood groups?|Karl Landsteiner|Louis Pasteur,Robert Koch,William Harvey|Karl Landsteiner discovered the ABO blood groups in 1900 and won the Nobel Prize for it.
Who is regarded as the founder of modern nursing?|Florence Nightingale|Marie Curie,Clara Barton,Mary Seacole|Florence Nightingale organised nursing during the Crimean War and founded modern nursing.
Who developed the first effective polio vaccine?|Jonas Salk|Edward Jenner,Louis Pasteur,Alexander Fleming|Jonas Salk developed the first injectable polio vaccine, introduced in 1955.
Who developed the smallpox vaccine?|Edward Jenner|Jonas Salk,Louis Pasteur,Robert Koch|Edward Jenner used cowpox material in 1796 to protect against smallpox.
Who discovered penicillin?|Alexander Fleming|Louis Pasteur,Robert Koch,Joseph Lister|Alexander Fleming noticed the antibacterial effect of Penicillium mould in 1928.
Who invented dynamite?|Alfred Nobel|Michael Faraday,James Watt,Thomas Edison|Alfred Nobel invented dynamite in 1867; his fortune funds the Nobel Prizes.
Who invented the telephone?|Alexander Graham Bell|Thomas Edison,Guglielmo Marconi,Nikola Tesla|Alexander Graham Bell patented the telephone in 1876.
Who propounded the theory of relativity?|Albert Einstein|Isaac Newton,Niels Bohr,Max Planck|Albert Einstein published the special theory in 1905 and the general theory in 1915.
Who gave the three laws of motion?|Isaac Newton|Galileo Galilei,Albert Einstein,Johannes Kepler|Isaac Newton set out the three laws of motion in Principia Mathematica in 1687.
Who explained the circulation of blood?|William Harvey|Karl Landsteiner,Louis Pasteur,Claude Bernard|William Harvey described the circulation of the blood in 1628.
Who is known as the father of genetics?|Gregor Mendel|Charles Darwin,Louis Pasteur,Robert Hooke|Gregor Mendel worked out the laws of inheritance from experiments on pea plants.
Which is the smallest bird?|hummingbird|sparrow,kingfisher,sunbird|The bee hummingbird is the smallest bird, about five centimetres long.
Which is the largest mammal?|blue whale|elephant,giraffe,hippopotamus|The blue whale is the largest mammal, reaching about thirty metres.
Which is the fastest land animal?|cheetah|lion,horse,antelope|The cheetah is the fastest land animal, reaching about 100 km per hour in short bursts.
Which is the national bird of India?|Indian peafowl|house sparrow,parrot,peacock|The Indian peafowl is the national bird of India.
Which is the national animal of India?|Royal Bengal tiger|lion,elephant,leopard|The Royal Bengal tiger is the national animal of India.
Which is the national flower of India?|lotus|rose,sunflower,marigold|The lotus is the national flower of India.
Which is the national fruit of India?|mango|banana,apple,guava|The mango is the national fruit of India.
What is the chemical symbol of gold?|Au|Ag,Fe,Cu|The symbol Au for gold comes from the Latin word aurum.
Which is the most abundant metal in the earth's crust?|aluminium|iron,copper,zinc|Aluminium is the most abundant metal, and the third most abundant element, in the crust.
Which is the lightest gas?|hydrogen|helium,nitrogen,oxygen|Hydrogen is the lightest gas, with an atomic mass of about one.
Which gas is commonly used in balloons?|helium|hydrogen,oxygen,carbon dioxide|Helium is light and non-flammable, so it is used to fill balloons.
Which element has atomic number one?|hydrogen|helium,carbon,oxygen|Hydrogen has a single proton, so its atomic number is one.
What is the chemical name of table salt?|sodium chloride|calcium carbonate,potassium nitrate,sodium bicarbonate|Table salt is the compound sodium chloride.
Which instrument records earthquakes?|seismograph|barometer,hygrometer,anemometer|A seismograph records the waves produced by an earthquake.
Which instrument measures rainfall?|rain gauge|barometer,hygrometer,thermometer|A rain gauge measures rainfall, usually in millimetres.
Which instrument measures humidity?|hygrometer|barometer,rain gauge,anemometer|A hygrometer measures the moisture content of the air.
In which medium does sound travel fastest?|solids|gases,liquids,vacuum|Sound travels fastest in solids because the particles are closest together.
Through which medium can sound not travel?|vacuum|water,steel,air|Sound needs a material medium, so it cannot travel through a vacuum.
What kind of image is formed by a plane mirror?|virtual and erect|real and inverted,virtual and inverted,real and erect|A plane mirror forms a virtual and erect image of the same size, as far behind it as the object is in front.
Which lens is used to correct myopia?|concave lens|convex lens,cylindrical lens,bifocal lens|Myopia, or short sight, is corrected with a concave diverging lens.
Which lens is used to correct hypermetropia?|convex lens|concave lens,cylindrical lens,plano-concave lens|Hypermetropia, or long sight, is corrected with a convex converging lens.
Why does the sky appear blue?|scattering of light by air molecules|reflection of light by the sea,refraction by water vapour,absorption of blue light by ozone|Air molecules scatter the shorter blue wavelengths more than the longer red ones.
"""

ECON_TERMS = """
gross domestic product|the value of all final goods and services produced within a country in a year
inflation|a sustained rise in the general level of prices
deflation|a sustained fall in the general level of prices
recession|a fall in GDP for two consecutive quarters
fiscal deficit|the excess of total expenditure over total receipts excluding borrowings
revenue deficit|the excess of revenue expenditure over revenue receipts
repo rate|the rate at which the RBI lends short-term funds to banks against securities
reverse repo rate|the rate at which the RBI borrows short-term funds from banks
cash reserve ratio|the share of deposits that banks must keep with the RBI
statutory liquidity ratio|the share of deposits that banks must hold in government securities and gold
bank rate|the long-term lending rate of the RBI
devaluation|an official lowering of the value of a currency against other currencies
balance of trade|the difference between the value of exports and imports of goods
balance of payments|the record of all economic transactions with the rest of the world
subsidy|a government payment that lowers the price of a good or service
direct tax|a tax paid directly by the person on whom it is imposed
indirect tax|a tax collected on goods and services and passed on to the consumer
disinvestment|the sale of government equity in public sector undertakings
national income|the total income earned by the residents of a country in a year
per capita income|national income divided by the population
public debt|the total borrowings of the government
budget|the annual statement of the government's receipts and expenditure
"""

INSTITUTIONS = """
Reserve Bank of India|Mumbai
Securities and Exchange Board of India|Mumbai
State Bank of India|Mumbai
Life Insurance Corporation of India|Mumbai
National Stock Exchange|Mumbai
Supreme Court of India|New Delhi
Election Commission of India|New Delhi
NITI Aayog|New Delhi
Union Public Service Commission|New Delhi
World Bank|Washington DC
International Monetary Fund|Washington DC
United Nations|New York
World Health Organization|Geneva
World Trade Organization|Geneva
International Labour Organization|Geneva
UNESCO|Paris
Food and Agriculture Organization|Rome
UNICEF|New York
International Court of Justice|The Hague
"""

WB_PLACES = """
Digha|Purba Medinipur
Haldia|Purba Medinipur
Shantiniketan|Birbhum
Tarapith|Birbhum
Bishnupur|Bankura
Krishnanagar|Nadia
Barrackpore|North 24 Parganas
Durgapur|Paschim Bardhaman
Asansol|Paschim Bardhaman
Bakreswar|Birbhum
Baharampur|Murshidabad
Chandannagar|Hooghly
Bolpur|Birbhum
Kharagpur|Paschim Medinipur
Raiganj|Uttar Dinajpur
Balurghat|Dakshin Dinajpur
Suri|Birbhum
Chinsurah|Hooghly
Nabadwip|Nadia
Basirhat|North 24 Parganas
Canning|South 24 Parganas
Arambagh|Hooghly
Rampurhat|Birbhum
Bongaon|North 24 Parganas
Diamond Harbour|South 24 Parganas
Mathabhanga|Cooch Behar
Kalna|Purba Bardhaman
Katwa|Purba Bardhaman
Manbazar|Purulia
Uluberia|Howrah
Tarakeswar|Hooghly
Garbeta|Paschim Medinipur
"""

WB_QA = """
Which city is the capital of West Bengal?|Kolkata|Howrah,Siliguri,Durgapur|Kolkata has been the capital of West Bengal since the province was partitioned in 1947.
How many districts are there in West Bengal?|twenty-three|nineteen,twenty-five,twenty-one|West Bengal has 23 districts since Paschim Bardhaman, Jhargram and Kalimpong were created.
On which river does Kolkata stand?|Hooghly|Damodar,Teesta,Mahanadi|Kolkata stands on the Hooghly, a distributary of the Ganga.
How many Indian states share a border with West Bengal?|five|three,four,six|West Bengal borders Odisha, Jharkhand, Bihar, Sikkim and Assam, five States in all.
Which is the highest peak in West Bengal?|Sandakphu|Falut,Tiger Hill,Senchal|Sandakphu, about 3,636 metres high in the Darjeeling district, is the highest point in the State.
Which is the state animal of West Bengal?|fishing cat|Royal Bengal tiger,elephant,leopard|The fishing cat is the state animal of West Bengal.
Which is the state bird of West Bengal?|white-throated kingfisher|house sparrow,peacock,parrot|The white-throated kingfisher is the state bird of West Bengal.
Which is the state flower of West Bengal?|night-flowering jasmine|lotus,rose,hibiscus|The night-flowering jasmine, known in Bengali as shiuli, is the state flower.
The Sundarbans is best known for|mangrove forests and the Royal Bengal tiger|tea gardens,snow peaks,desert dunes|The Sundarbans is the largest mangrove forest in the world and a tiger reserve.
Darjeeling is famous for|tea|coffee,rubber,sugarcane|Darjeeling tea is famous for its flavour and carries a geographical indication.
The Victoria Memorial is situated in|Kolkata|Howrah,Darjeeling,Siliguri|The Victoria Memorial stands on the Maidan in Kolkata.
The Howrah Bridge crosses the river|Hooghly|Damodar,Teesta,Barakar|The Howrah Bridge spans the Hooghly between Howrah and Kolkata.
Who was the first Chief Minister of West Bengal?|Prafulla Chandra Ghosh|Bidhan Chandra Roy,Jyoti Basu,Siddhartha Shankar Ray|Prafulla Chandra Ghosh was Chief Minister of West Bengal in 1947 and 1948.
Bishnupur is famous for|terracotta temples and Baluchari silk|tea,cashew,iron ore|Bishnupur in Bankura is known for its terracotta temples and Baluchari sarees.
The Kanyashree scheme of West Bengal supports|girl students|farmers,fishermen,weavers|Kanyashree Prakalpa, launched in 2013, gives scholarships to girl students to keep them in school.
Gangasagar Mela is held at|Sagar Island|Digha,Bakkhali,Shantiniketan|The Gangasagar Mela is held on Sagar Island at the mouth of the Hooghly.
The West Bengal Legislative Assembly has how many seats?|294|250,300,280|The West Bengal Legislative Assembly has 294 elected seats.
Poila Boishakh, the Bengali New Year, falls in|April|January,October,July|Poila Boishakh, the first day of the Bengali year, falls in mid-April.
"""

CURRENT = """
Which country won the ICC Men's T20 World Cup 2026?|India|Australia,New Zealand,England|India beat New Zealand by 96 runs in the final at Ahmedabad on 8 March 2026.
Which country won the FIFA World Cup 2026?|Spain|Argentina,France,Brazil|Spain beat Argentina 1-0 after extra time at MetLife Stadium on 19 July 2026.
Which city hosted the 2026 Winter Olympics?|Milano-Cortina|Beijing,Pyeongchang,Salt Lake City|The 2026 Winter Olympics were held in Milan and Cortina d'Ampezzo from 6 to 22 February 2026.
Which country won the most gold medals at the 2026 Winter Olympics?|Norway|United States,Germany,Italy|Norway topped the medal table at the 2026 Winter Olympics with 18 gold medals.
Which city hosted the 2026 Commonwealth Games?|Glasgow|Birmingham,Delhi,Melbourne|Glasgow hosted the 2026 Commonwealth Games, which closed on 2 August 2026.
Which country is hosting the 2026 Asian Games?|Japan|China,South Korea,India|The 2026 Asian Games are being held in Aichi and Nagoya in Japan.
Which city will host the 2028 Summer Olympics?|Los Angeles|Brisbane,Paris,Rome|Los Angeles will host the 2028 Summer Olympics.
Who is the Chief Minister of West Bengal in 2026?|Suvendu Adhikari|Mamata Banerjee,Dilip Ghosh,Abani Roy|Suvendu Adhikari took office as Chief Minister of West Bengal on 9 May 2026.
Who is the President of India in 2026?|Droupadi Murmu|Ram Nath Kovind,Pranab Mukherjee,Venkaiah Naidu|Droupadi Murmu is the President of India.
Who is the Vice-President of India in 2026?|C. P. Radhakrishnan|Venkaiah Naidu,Jagdeep Dhankhar,M. Venkaiah Naidu|C. P. Radhakrishnan is the Vice-President of India.
Who is the Chief Justice of India in 2026?|Surya Kant|D. Y. Chandrachud,N. V. Ramana,U. U. Lalit|Justice Surya Kant is the Chief Justice of India.
Who is the Governor of the Reserve Bank of India in 2026?|Sanjay Malhotra|Shaktikanta Das,Urjit Patel,Raghuram Rajan|Sanjay Malhotra is the Governor of the Reserve Bank of India.
Who is the Chief Election Commissioner of India in 2026?|Gyanesh Kumar|Sushil Chandra,Rajiv Kumar,Sunil Arora|Gyanesh Kumar is the Chief Election Commissioner of India.
Who is the Chairman of ISRO in 2026?|V. Narayanan|K. Sivan,S. Somanath,A. S. Kiran Kumar|V. Narayanan is the Chairman of ISRO.
Who is the Union Finance Minister of India in 2026?|Nirmala Sitharaman|Piyush Goyal,Nitin Gadkari,Amit Shah|Nirmala Sitharaman is the Union Finance Minister.
Which was India's first uncrewed Gaganyaan mission, planned for 2026?|G1|G2,H1,TV-D2|G1 is the first uncrewed Gaganyaan mission, planned for the second half of 2026.
Which country won the ICC Champions Trophy 2025?|India|Pakistan,New Zealand,Australia|India beat New Zealand to win the ICC Champions Trophy in 2025.
Which city hosted the 2024 Summer Olympics?|Paris|Tokyo,Rio de Janeiro,Los Angeles|Paris hosted the 2024 Summer Olympics.
On which date did Chandrayaan-3 land on the Moon?|23 August 2023|15 August 2023,23 August 2024,5 September 2023|Chandrayaan-3's Vikram lander touched down near the lunar south pole on 23 August 2023.
"""


def rows(blob, n):
    out = []
    for line in blob.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != n:
            raise ValueError(f"expected {n} fields: {line}")
        if n == 4:                       # question | answer | d1,d2,d3 | explanation
            parts = [parts[0], parts[1], [d.strip() for d in parts[2].split(",")], parts[3]]
        elif n == 3:                     # question | answer | d1,d2,d3
            parts = [parts[0], parts[1], [d.strip() for d in parts[2].split(",")]]
        out.append(tuple(parts))
    return out


ART = rows(ARTICLES, 2)
OFF = rows(OFFICES, 4)
CAP = rows(CAPITALS, 2)
RIV = rows(RIVERS, 2)
PRK = rows(PARKS, 2)
YRS = rows(YEARS, 2)
PER = rows(PERSONALITIES, 4)
UNT = rows(UNITS, 2)
VIT = rows(VITAMINS, 2)
SCI = rows(SCIENCE_QA, 4)
ECO = rows(ECON_TERMS, 2)
HQ = rows(INSTITUTIONS, 2)
WBP = rows(WB_PLACES, 2)
WBQ = rows(WB_QA, 4)
CA = rows(CURRENT, 4)

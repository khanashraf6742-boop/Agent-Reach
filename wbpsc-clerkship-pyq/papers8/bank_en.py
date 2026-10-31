# -*- coding: utf-8 -*-
"""English bank for the eight Part-I papers.

Line format:  prompt | answer | d1,d2,d3 | explanation
Every line is a single source of truth. The validator re-reads these datasets and
re-derives the key independently of the assembled paper, so a typo in an answer field
cannot survive by agreeing with itself.
"""

SYNONYMS = """
ABANDON|forsake|retain,cherish,pursue|Forsake means to give up completely; retain and cherish mean to keep, and pursue means to follow.
ABUNDANT|plentiful|scarce,meagre,sparse|Plentiful means more than enough; the other three all mean short in supply.
AUDACIOUS|daring|timid,cautious,gentle|Audacious means boldly reckless; timid and cautious are its opposites.
BENEVOLENT|kind|cruel,hostile,selfish|Benevolent means wishing good to others, hence kind.
CANDID|frank|evasive,secretive,sly|Candid means open and straightforward; the others describe concealment.
DILIGENT|industrious|lazy,careless,idle|Diligent means hard-working; lazy and idle mean the opposite.
ELOQUENT|fluent|tongue-tied,halting,coarse|Eloquent means speaking with ease and grace; halting speech is its opposite.
FRUGAL|thrifty|wasteful,lavish,prodigal|Frugal means sparing in expenditure; the others mean spending freely.
GREGARIOUS|sociable|solitary,reclusive,aloof|Gregarious means fond of company; the others describe withdrawal.
HOSTILE|unfriendly|cordial,amiable,friendly|Hostile means showing enmity; the other three are warm.
IMPARTIAL|unbiased|prejudiced,partial,one-sided|Impartial means not favouring a side; the others mean favouring one.
JUBILANT|elated|dejected,gloomy,sorrowful|Jubilant means filled with joy; the others mean low in spirits.
LUCID|clear|obscure,vague,murky|Lucid means easily understood; the others mean hard to grasp.
MENDACIOUS|untruthful|honest,truthful,sincere|Mendacious means given to lying; the others mean truthful.
NOVICE|beginner|expert,veteran,master|A novice is new to a field; the others mean experienced.
OBSTINATE|stubborn|flexible,docile,yielding|Obstinate means refusing to change; the others mean willing to bend.
PRUDENT|wise|reckless,rash,foolish|Prudent means showing care for the future; the others mean careless.
QUAINT|odd|ordinary,common,familiar|Quaint means pleasingly unusual; the others mean usual.
RELUCTANT|unwilling|eager,willing,keen|Reluctant means disinclined; the others mean keen.
TENACIOUS|persistent|irresolute,fickle,wavering|Tenacious means holding on firmly; the others mean changing easily.
URGENT|pressing|trivial,minor,leisurely|Urgent means demanding immediate action; the others mean unimportant or unhurried.
VIVID|bright|dull,faded,dim|Vivid means strong and clear in colour or impression.
WARY|cautious|reckless,careless,bold|Wary means on guard against danger; the others mean without caution.
ZEALOUS|enthusiastic|indifferent,apathetic,listless|Zealous means full of energy for a cause; the others mean without interest.
ABSTRUSE|obscure|simple,plain,obvious|Abstruse means hard to understand; the others mean easy.
BREVITY|conciseness|verbosity,prolixity,length|Brevity means shortness of expression; the others mean long-windedness.
COMPLY|obey|defy,resist,oppose|Comply means to act in accordance with an order.
DEFER|postpone|hasten,advance,hurry|Defer means to put off to a later time.
EMINENT|distinguished|unknown,obscure,ordinary|Eminent means standing above others in a field.
FEEBLE|weak|strong,sturdy,robust|Feeble means lacking strength; the other three mean strength.
GAUDY|showy|subdued,plain,tasteful|Gaudy means crudely bright; the others mean restrained.
HAMPER|hinder|assist,help,facilitate|Hamper means to make progress difficult.
IMPETUOUS|rash|careful,deliberate,prudent|Impetuous means acting on impulse without thought.
JEOPARDY|danger|safety,security,protection|Jeopardy means exposure to harm; the others mean shelter from it.
LAMENT|mourn|rejoice,celebrate,cheer|Lament means to express grief; the others mean to express joy.
MALICE|spite|goodwill,kindness,benevolence|Malice means a desire to harm others.
NEGLIGIBLE|insignificant|substantial,considerable,large|Negligible means too small to matter.
OBSCURE|unclear|obvious,plain,lucid|Obscure means not easily understood or seen.
PLACATE|pacify|provoke,anger,irritate|Placate means to calm an angry person.
QUERY|question|answer,reply,response|A query is a question or enquiry.
REMOTE|distant|near,close,adjacent|Remote means far away in space or time.
SALIENT|prominent|minor,trivial,hidden|Salient means standing out as important.
TEDIOUS|boring|interesting,lively,exciting|Tedious means long and dull.
UPHOLD|support|oppose,reject,overturn|Uphold means to confirm or give support to.
VACANT|empty|occupied,full,filled|Vacant means not occupied.
WITHDRAW|retreat|advance,proceed,attack|Withdraw means to move back or take out.
YEARN|long|detest,loathe,spurn|Yearn means to feel a strong desire for something.
ABOLISH|repeal|enforce,establish,institute|Abolish means to put an end to a law or practice.
BANISH|exile|recall,welcome,admit|Banish means to send away by authority.
COERCE|compel|persuade,coax,request|Coerce means to force by threat; the others mean to ask or urge.
DEARTH|scarcity|abundance,plenty,surplus|Dearth means an inadequate supply.
ENIGMA|mystery|clarity,certainty,explanation|An enigma is something puzzling and unexplained.
FOSTER|encourage|suppress,hinder,discourage|Foster means to help something grow.
GRIEF|sorrow|joy,delight,pleasure|Grief is deep sadness, especially at a loss.
HAZARDOUS|dangerous|safe,secure,harmless|Hazardous means involving risk.
IMMENSE|huge|tiny,minute,small|Immense means extremely large.
JOVIAL|cheerful|gloomy,morose,sullen|Jovial means good-humoured and merry.
KEEN|eager|reluctant,indifferent,apathetic|Keen means very interested; the others mean without interest.
LURE|entice|repel,deter,dissuade|Lure means to attract by temptation.
MITIGATE|lessen|aggravate,worsen,intensify|Mitigate means to make less severe.
OBSOLETE|outdated|modern,current,recent|Obsolete means no longer in use.
PERIL|danger|safety,security,shelter|Peril means serious and immediate risk.
QUELL|suppress|incite,provoke,foment|Quell means to put down a disturbance.
RECTIFY|correct|worsen,spoil,corrupt|Rectify means to put right.
SOLEMN|serious|frivolous,trivial,playful|Solemn means formal and grave.
TRANQUIL|calm|turbulent,restless,agitated|Tranquil means free from disturbance.
VIGILANT|watchful|negligent,careless,inattentive|Vigilant means keeping careful watch.
WHIMSICAL|fanciful|practical,serious,sober|Whimsical means playfully odd in imagination.
ALLEVIATE|relieve|aggravate,intensify,worsen|Alleviate means to make pain or difficulty less.
CORDIAL|friendly|hostile,bitter,cold|Cordial means warm and courteous.
DEBILITATE|weaken|strengthen,fortify,invigorate|Debilitate means to make weak.
EXEMPLARY|model|inferior,defective,faulty|Exemplary means fit to be copied as a model.
FUTILE|useless|fruitful,effective,profitable|Futile means producing no result.
"""

ANTONYMS = """
ABSURD|sensible|foolish,ridiculous,silly|Absurd means wildly unreasonable, so its opposite is sensible.
ADVERSE|favourable|hostile,unfavourable,harmful|Adverse means unfavourable or opposing.
AFFLUENT|poor|rich,wealthy,prosperous|Affluent means wealthy; the other three are synonyms of it.
AMBIGUOUS|clear|vague,unclear,doubtful|Ambiguous means open to more than one meaning.
ANCIENT|modern|old,antique,aged|Ancient means belonging to the distant past.
ARROGANT|humble|proud,haughty,conceited|Arrogant means overbearingly proud.
BENEVOLENT|cruel|kind,generous,charitable|Benevolent means kindly, so its opposite is cruel.
BRAVE|cowardly|bold,fearless,valiant|Brave means facing danger without fear.
CANDID|evasive|frank,honest,open|Candid means straightforward; evasive means avoiding a straight answer.
CHEERFUL|gloomy|happy,joyful,merry|Cheerful means in good spirits.
CONCEAL|reveal|hide,cover,mask|Conceal means to keep from sight.
CONDEMN|praise|blame,criticise,censure|Condemn means to express strong disapproval.
CRUEL|kind|brutal,harsh,savage|Cruel means causing pain deliberately.
DEFICIT|surplus|shortage,loss,debt|A deficit is a shortfall; a surplus is an excess.
DELIBERATE|accidental|intentional,planned,wilful|Deliberate means done on purpose.
DIMINISH|increase|reduce,lessen,decrease|Diminish means to become smaller.
ENEMY|friend|foe,rival,opponent|An enemy is one who opposes; a friend supports.
EXPAND|contract|enlarge,widen,spread|Expand means to grow larger.
FAMINE|plenty|hunger,scarcity,starvation|Famine is an extreme scarcity of food.
FERTILE|barren|productive,rich,fruitful|Fertile means able to produce crops.
FIERCE|gentle|savage,wild,ferocious|Fierce means violent in temper or action.
FLEXIBLE|rigid|pliable,supple,elastic|Flexible means able to bend.
FORBID|permit|prohibit,ban,bar|Forbid means to order not to do something.
GENEROUS|mean|liberal,kind,lavish|Generous means free in giving.
GUILTY|innocent|culpable,blameworthy,sinful|Guilty means having committed a wrong.
HASTY|deliberate|quick,hurried,rash|Hasty means done too quickly, without care.
HUMBLE|proud|modest,meek,lowly|Humble means not thinking highly of oneself.
IDLE|busy|lazy,inactive,indolent|Idle means not working or not in use.
INNOCENT|guilty|blameless,pure,faultless|Innocent means free from wrong.
JOY|sorrow|delight,happiness,pleasure|Joy is great happiness.
LIBERTY|bondage|freedom,independence,licence|Liberty means freedom from restraint.
LOYAL|treacherous|faithful,devoted,steadfast|Loyal means firm in allegiance.
MEAGRE|ample|scanty,sparse,insufficient|Meagre means small in quantity.
MERCY|cruelty|kindness,pity,compassion|Mercy means forbearance shown to an offender.
OBEDIENT|defiant|dutiful,submissive,compliant|Obedient means willing to obey.
OPTIMIST|pessimist|hopeful,positive,cheerful|An optimist expects the best; a pessimist expects the worst.
PERMANENT|temporary|lasting,enduring,stable|Permanent means lasting indefinitely.
PROSPERITY|adversity|wealth,success,fortune|Prosperity means success and good fortune.
RARE|common|scarce,unusual,infrequent|Rare means seldom found or occurring.
RIGID|flexible|stiff,firm,unbending|Rigid means not able to bend.
SACRED|profane|holy,divine,pious|Sacred means set apart as holy.
SCATTER|gather|disperse,spread,strew|Scatter means to throw in all directions.
SHALLOW|deep|superficial,hollow,slight|Shallow means of little depth.
STRICT|lenient|severe,stern,rigid|Strict means enforcing rules firmly.
SUPERIOR|inferior|higher,better,greater|Superior means above another in rank or quality.
TRANSPARENT|opaque|clear,lucid,obvious|Transparent means allowing light through.
UNITY|discord|union,harmony,accord|Unity means being joined as one.
VICTORY|defeat|triumph,success,win|Victory means winning; defeat means losing.
VIRTUE|vice|goodness,merit,morality|Virtue is moral excellence.
WISDOM|folly|prudence,sagacity,insight|Wisdom is sound judgement; folly is foolishness.
ZEAL|apathy|enthusiasm,ardour,passion|Zeal is great energy for a cause.
ACQUIT|convict|absolve,pardon,exonerate|To acquit is to declare not guilty.
"""

IDIOMS = """
to bite the dust|to fail or be defeated|to eat greedily,to speak rudely,to sleep deeply|'To bite the dust' means to be defeated or to come to nothing.
a bolt from the blue|a sudden shock|a loud noise,a welcome gift,a long journey|The image is lightning from a clear sky, that is, something wholly unexpected.
to burn the midnight oil|to work late into the night|to waste money,to sleep early,to light a fire|The oil is lamp oil burnt while working after dark.
to bury the hatchet|to end a quarrel|to hide a weapon,to dig a grave,to start a fight|The hatchet is buried as a sign that hostility is over.
by hook or by crook|by any means|by fair means only,by chance,by legal process|The phrase means by one method or another, fair or foul.
to call a spade a spade|to speak plainly|to dig a garden,to insult someone,to tell a lie|It means to name a thing honestly instead of euphemising.
a cat's paw|a person used by another|a small animal,a lucky charm,a gentle person|The cat's paw is the instrument through which another does a risky act.
to cry wolf|to raise a false alarm|to hunt animals,to weep loudly,to call for help|From the fable of the boy who called 'wolf' when there was none.
to cut the Gordian knot|to solve a problem boldly|to tie a rope,to divide wealth,to avoid trouble|Alexander cut the knot that no one could untie.
a dark horse|an unexpected winner|a black animal,a wicked person,a night worker|The term comes from racing, for a horse about which little is known.
to die in harness|to die while still working|to die in battle,to retire early,to work hard|The harness is the working gear of a horse.
to eat one's words|to take back a statement|to speak softly,to enjoy a meal,to be hungry|It means to admit that what one said was wrong.
an eye for an eye|retaliation in kind|a medical treatment,a fair judgement,a gift|It describes exact retaliation, not a cure or a reward.
to face the music|to bear the consequences|to enjoy a concert,to dance well,to sing loudly|It means to confront the unpleasant result of one's action.
a far cry|a great distance|a loud shout,a small effort,a short walk|'A far cry from' means very different or very distant.
to fish in troubled waters|to take advantage of trouble|to catch fish,to clean a pond,to sail a boat|It means to profit from disorder.
to get cold feet|to lose courage|to feel chilly,to be ill,to walk barefoot|It describes a sudden loss of nerve before an act.
to give a wide berth|to keep away|to offer a seat,to sail a ship,to greet warmly|A berth is room enough for a ship to pass safely.
a hard nut to crack|a difficult problem|a tasty fruit,a strong person,an easy task|The nut resists the cracker, as the problem resists solution.
to hit the nail on the head|to say exactly the right thing|to hurt someone,to work with tools,to fail badly|The image is a blow that lands exactly where intended.
in hot water|in trouble|in a bath,in good health,in a hurry|It means in difficulty or disgrace.
to keep one's fingers crossed|to hope for good luck|to pray loudly,to refuse help,to fold hands|The gesture is a silent wish for a good outcome.
to let the cat out of the bag|to reveal a secret|to free an animal,to make a mistake,to start a rumour|The secret escapes, like a cat from a sack.
to make ends meet|to live within one's means|to join two ropes,to earn a lot,to finish a task|It means to manage on the money one has.
a mare's nest|a discovery that is not real|a bird's home,a comfortable place,a strange dream|The phrase describes an imagined discovery or a muddle.
to move heaven and earth|to make every possible effort|to travel far,to change the weather,to pray only|It means to use every means available.
once in a blue moon|very rarely|every night,very often,at dawn|A blue moon is a rare second full moon in a month.
to pay through the nose|to pay too much|to pay in instalments,to pay nothing,to borrow money|It means to pay an exorbitant price.
to play second fiddle|to take a subordinate role|to sing badly,to cheat someone,to act in a play|The second fiddle supports the first in an orchestra.
to pull one's leg|to tease someone|to hurt someone,to help someone,to run fast|It is a joke at someone's expense, not an injury.
to put one's foot down|to act firmly|to dance well,to walk slowly,to fall down|It means to refuse to yield.
a red letter day|an important day|a holiday,a sad day,a rainy day|Important days were once marked in red on calendars.
to see eye to eye|to agree completely|to stare,to look sideways,to meet accidentally|It means to share the same view.
to smell a rat|to suspect something wrong|to find food,to keep a pet,to clean a house|The smell suggests something is not as it should be.
to spill the beans|to reveal information|to cook food,to drop a vessel,to waste grain|It means to let out what was hidden.
to steal a march|to gain an advantage secretly|to walk quietly,to rob a house,to march fast|It means to get ahead of another unawares.
a storm in a teacup|a great fuss over a small matter|a heavy rain,a hot drink,a real danger|The storm is imaginary and the teacup tiny.
to take the bull by the horns|to face danger boldly|to catch an animal,to run away,to argue|It means to tackle a difficulty directly.
to throw cold water on|to discourage a plan|to wash something,to cool a room,to help gladly|Cold water extinguishes enthusiasm.
to turn a deaf ear|to refuse to listen|to hear clearly,to be ill,to speak softly|The ear is turned away so as not to hear.
to turn a blind eye|to ignore deliberately|to become blind,to look carefully,to wink|It means to pretend not to see.
under the weather|feeling unwell|in the rain,in a good mood,out of doors|It means slightly ill or low.
to wear one's heart on one's sleeve|to show one's feelings openly|to dress nicely,to be brave,to hide emotions|The heart, once worn on the sleeve, is visible to all.
a wet blanket|a person who spoils others' fun|a rainy day,a warm quilt,a helpful friend|A wet blanket smothers a fire, as such a person smothers cheer.
at the eleventh hour|at the last moment|at eleven o'clock,in the morning,too early|From the parable of the labourers hired at the eleventh hour.
to bear the brunt|to suffer the main force|to carry a load,to attack first,to pay a debt|The brunt is the heaviest part of a blow.
to blow one's own trumpet|to praise oneself|to play music,to be honest,to shout loudly|It means to boast of one's own deeds.
to burn one's fingers|to suffer from one's own action|to cook food,to feel cold,to work fast|It means to get hurt by meddling.
to have an axe to grind|to have a selfish motive|to cut wood,to quarrel,to do hard work|The phrase implies a private purpose behind a show of goodwill.
to put the cart before the horse|to reverse the proper order|to load a wagon,to travel fast,to harness an animal|The cart must follow the horse, as effect follows cause.
"""

ONE_WORD = """
one who talks too much|garrulous|taciturn,reserved,succinct|Garrulous means excessively talkative.
one who eats too much|glutton|miser,spendthrift,gourmet|A glutton is one given to excessive eating.
one who is hard to please|fastidious|careless,generous,punctual|Fastidious means very particular about details.
a place where money is coined|mint|treasury,bank,vault|Coins are struck at a mint.
a place where birds are kept|aviary|apiary,aquarium,granary|An aviary houses birds.
a place where bees are kept|apiary|aviary,coop,zoo|An apiary houses beehives.
a place where fishes are kept|aquarium|aviary,apiary,reservoir|An aquarium is a tank for live fish.
a medicine that counteracts poison|antidote|antibiotic,antiseptic,vaccine|An antidote neutralises a poison.
a speech made without preparation|extempore|oration,prologue,lecture|Extempore means spoken without previous preparation.
one who does not believe in God|atheist|theist,agnostic,pagan|An atheist denies the existence of God.
one who is present everywhere|omnipresent|omnipotent,omniscient,absent|Omnipresent means present in all places.
one who knows everything|omniscient|omnipotent,omnipresent,ignorant|Omniscient means knowing all things.
one who is all-powerful|omnipotent|omniscient,weak,mortal|Omnipotent means having unlimited power.
a government by the people|democracy|monarchy,oligarchy,autocracy|Democracy is rule by the people.
a government by a king|monarchy|democracy,republic,anarchy|Monarchy is rule by a single hereditary sovereign.
a government by officials|bureaucracy|aristocracy,plutocracy,theocracy|Bureaucracy is rule by officials.
a government by the rich|plutocracy|democracy,monarchy,anarchy|Plutocracy is rule by the wealthy.
a word of the same meaning|synonym|antonym,homonym,acronym|A synonym has the same meaning as another word.
a word of opposite meaning|antonym|synonym,homonym,pseudonym|An antonym has the opposite meaning.
a word no longer in use|obsolete|current,modern,frequent|Obsolete means out of use.
the study of birds|ornithology|entomology,botany,zoology|Ornithology is the study of birds.
the study of insects|entomology|ornithology,etymology,anthropology|Entomology is the study of insects.
the study of the origin of words|etymology|entomology,ornithology,astronomy|Etymology traces the history of words.
the study of the human body|anatomy|astronomy,geology,botany|Anatomy is the study of body structure.
the study of stars|astronomy|astrology,anatomy,geology|Astronomy is the science of heavenly bodies.
the study of rocks|geology|anatomy,astronomy,geometry|Geology is the study of the earth's crust.
a person who walks on foot|pedestrian|motorist,cyclist,sailor|A pedestrian travels on foot.
a person who loves mankind|philanthropist|misanthrope,philosopher,patriot|A philanthropist loves and helps humanity.
one who hates mankind|misanthrope|philanthropist,optimist,hermit|A misanthrope dislikes human society.
a person who lives alone|recluse|socialite,host,traveler|A recluse lives apart from others.
that which cannot be avoided|inevitable|avoidable,uncertain,unlikely|Inevitable means certain to happen.
that which cannot be read|illegible|legible,eligible,audible|Illegible writing cannot be read.
that which cannot be heard|inaudible|audible,invisible,illegible|Inaudible means not able to be heard.
that which cannot be seen|invisible|visible,inaudible,illegible|Invisible means not able to be seen.
one who cannot read or write|illiterate|literate,ignorant,educated|Illiterate means unable to read or write.
fit to be eaten|edible|audible,visible,incredible|Edible means fit for eating.
fit to be believed|credible|incredible,credulous,creditable|Credible means believable.
a person of a hundred years|centenarian|septuagenarian,octogenarian,nonagenarian|A centenarian is a hundred years old.
a dead body|corpse|cargo,coffin,statue|A corpse is a dead human body.
a word written in another's name|pseudonym|synonym,antonym,acronym|A pseudonym is an assumed name.
a hater of women|misogynist|misanthrope,feminist,philanthropist|A misogynist hates women.
a doctor of animals|veterinarian|physician,dentist,gardener|A veterinarian treats animals.
one who can use both hands equally well|ambidextrous|left-handed,clumsy,amateur|Ambidextrous means using either hand with equal skill.
"""

SPELLINGS = """
accommodation|acomodation,accomodation,accomodetion|The word has two c's and two m's: ac-com-mo-da-tion.
bureaucracy|bureacracy,burocracy,bureaucrecy|After 'bureau' comes 'cracy': bureau-cracy.
privilege|priviledge,privelege,privilage|There is no d in privilege: priv-i-lege.
recommendation|recomendation,reccommendation,recomendetion|One c, two m's: re-com-men-da-tion.
occurrence|occurence,ocurrence,occurrance|Two c's, two r's, and 'ence' at the end.
embarrassment|embarassment,embarrasment,embarresment|Two r's and two s's: em-bar-rass-ment.
committee|commitee,committe,comittee|Two m's, two t's, two e's: com-mit-tee.
receipt|reciept,receit,recipt|The rule 'i before e except after c' gives re-ceipt.
maintenance|maintainance,maintenence,maintainence|The base is 'maintain', but the noun is main-te-nance.
separate|seperate,seperete,seperat|There is 'a rat' in sep-a-rate.
definitely|definately,definitly,definetly|From 'finite': de-fin-ite-ly.
calendar|calender,calandar,calendir|A calendar marks dates; a calender presses cloth.
government|goverment,govenment,governmant|The n of 'govern' is kept: govern-ment.
necessary|neccessary,necesary,necessery|One c, two s's: ne-ces-sa-ry.
parliament|parliment,parliamant,parlement|Parliament has 'ia': par-lia-ment.
questionnaire|questionaire,questionnair,questionnere|Two n's and 'aire' at the end.
schedule|shedule,schedual,scheddule|Begins with 'sch', not 'sh'.
vaccinate|vacinate,vaccinete,vasccinate|Two c's, one n: vac-ci-nate.
mischievous|mischevious,mischieveous,mischeivous|Three syllables: mis-chie-vous, with no extra i.
liaison|liason,liaision,laison|Two i's around 'ais': li-ai-son.
sergeant|sergent,sergant,seargant|Sergeant has 'ea': ser-geant.
consensus|concensus,consenssus,consensous|From 'consent': con-sen-sus, one c and one s in the middle.
arduous|ardous,arrduous,ardoues|Ar-du-ous, with a u after the d.
employee|employe,emploee,employy|Ends in 'ee' for the person employed.
correspondence|correspondance,corresponence,corespondence|Two r's, two s's, and 'ence'.
acquaintance|acquaintence,acquiantance,akquaintance|'Acquaint' plus 'ance'.
"""

USAGE = """
She is very good ____ mathematics.|at|in,on,for|The collocation is 'good at' a subject or skill.
The clerk was accused ____ accepting a bribe.|of|for,with,about|Accuse takes 'of': accuse someone of something.
She is married ____ a doctor.|to|with,for,by|One is married to a person.
He died ____ cholera.|of|from,by,with|Death by disease takes 'of': died of cholera.
I am senior ____ him by five years.|to|than,from,of|Senior, junior, superior and inferior take 'to', not 'than'.
He insisted ____ paying the bill.|on|at,for,to|Insist takes 'on' before a gerund.
She is afraid ____ spiders.|of|from,with,at|Afraid of something.
The train arrived ____ time.|on|in,at,by|'On time' means punctually; 'in time' means before it is too late.
He is addicted ____ gambling.|to|with,for,of|Addicted to a habit.
She complied ____ the rules.|with|to,by,for|Comply takes 'with'.
He was angry ____ me for being late.|with|on,at,to|Anger at a person takes 'with'; anger at a thing takes 'at'.
The book consists ____ ten chapters.|of|in,from,with|Consist of means to be made up of.
He was deprived ____ his rights.|of|from,with,to|Deprive takes 'of'.
He is capable ____ doing it alone.|of|to,for,in|Capable takes 'of' plus a gerund.
Nothing came ____ his efforts.|of|from,in,with|'Come of' means to result from.
She is junior ____ me.|to|than,from,of|Junior takes 'to'.
He was charged ____ murder.|with|of,for,by|Charge takes 'with'; accuse takes 'of'.
The teacher was pleased ____ the result.|with|on,at,for|Pleased with a thing or a person.
"""


def _rows(blob):
    out = []
    for line in blob.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split("|")
        if len(parts) == 3:          # spelling rows: word | misspellings | note
            prompt, answer, distractors, expl = parts[0], parts[0], parts[1], parts[2]
        elif len(parts) == 4:
            prompt, answer, distractors, expl = parts
        else:
            raise ValueError("bad line: " + line)
        ds = [d.strip() for d in distractors.split(",")]
        if "remove" in expl.lower():
            raise ValueError("draft row left in bank: " + line)
        out.append((prompt.strip(), answer.strip(), ds, expl.strip()))
    return out


SYN = _rows(SYNONYMS)
ANT = _rows(ANTONYMS)
IDIOM = _rows(IDIOMS)
ONEWORD = _rows(ONE_WORD)
SPELL = _rows(SPELLINGS)
USE = _rows(USAGE)

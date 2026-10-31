# -*- coding: utf-8 -*-
"""Addenda that top each sheet up to the foot of its page.

Kept apart from the main sheets so the extra material can be read and checked
on its own.  Numbers that appear inside a worked check are computed here.
"""

# --- arithmetic checks used below -------------------------------------------
_cp, _sp = 480, 552
_profit = (_sp - _cp) / _cp * 100
_mp, _d1 = 800, 20
_sp_disc = _mp * (1 - _d1 / 100)
_p, _r, _t = 2500, 4, 3
_si = _p * _r * _t / 100
_ci = _p * (1 + _r / 100) ** _t - _p
_x, _y = 12, 18
_work = _x * _y / (_x + _y)

EXTRA = {
"geography": {
"left": """
## Passes, lakes, minerals
- Passes :: Karakoram (Ladakh), Zoji La (Srinagar to Kargil), Nathu La (Sikkim to Tibet), Bomdi La (Arunachal).
- Lakes :: Wular the largest freshwater lake, Chilika the largest brackish lagoon, Sambhar the salt lake of Rajasthan.
- Minerals :: iron ore in Odisha and Jharkhand, coal in Jharkhand and Odisha, bauxite in Odisha, mica in Jharkhand.
""",
"right": """
## States at a glance
- Twenty-eight States and eight Union Territories. Sikkim joined in 1975, Goa became a State in 1987, Telangana in 2014.
- The seven sisters :: Assam, Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Tripura.
- Largest by area :: Rajasthan. Smallest :: Goa. Most populous :: Uttar Pradesh.
- Mountains :: Himalaya, Aravalli (the oldest fold range), Vindhya, Satpura, Western and Eastern Ghats. Plateaus :: Deccan, Chota Nagpur, Malwa.
- Northern plains :: Bhabar, Terai, Bhangar and Khadar.
""",
},
"history": {
"left": """
## Texts, religions and reform
- Four Vedas :: Rig, Sama, Yajur, Atharva. Buddhism :: Four Noble Truths, Eightfold Path. Jainism :: Mahavira, the twenty-fourth Tirthankara.
- Sati abolished 1829, Bentinck. Widow remarriage 1856, Vidyasagar. Aligarh 1875, Sir Syed Ahmed Khan.
- Newspapers :: Kesari (Tilak), Bengalee (Banerjee), Amrita Bazar Patrika, Bande Mataram (Aurobindo), Young India and Harijan (Gandhi).
""",
"right": """
## Viceroys and sessions
- Cornwallis :: the Permanent Settlement. Wellesley :: the Subsidiary Alliance. Dalhousie :: the Doctrine of Lapse. Curzon :: the Partition of Bengal.
- 1885 Bombay :: the first session. 1906 Calcutta :: the split. 1916 Lucknow :: the Congress-League pact.
- 1929 Lahore :: Purna Swaraj. 1931 Karachi :: fundamental rights. 1939 Tripuri :: Bose against the working committee.
""",
},
"science": {
"left": """
## The body, and the names of the sciences
- Bones 206 in an adult, adult teeth 32, heart about 72 beats a minute, red cells live about 120 days.
- Study of :: birds ornithology, insects entomology, fossils palaeontology, fungi mycology, viruses virology, cells cytology.
- Laws :: Ohm's law V equals I times R; Boyle's law on pressure and volume; Charles's law on volume and temperature; Archimedes on upthrust.
""",
"right": """
## Indian science and everyday science
- Raman effect :: C. V. Raman, Nobel 1930. Bhabha the nuclear programme, Sarabhai space, Kalam missiles, Swaminathan the green revolution, Kurien the white revolution.
- Sky is blue :: scattering. Stick looks bent in water :: refraction. Diamond sparkles :: total internal reflection.
- Lightning before thunder :: light travels faster than sound. Ice floats :: it is less dense than water. Pressure cooker :: pressure raises the boiling point.
""",
},
"economy": {
"left": """
## Banking history
- RBI :: founded 1935, nationalised 1949. Imperial Bank became the State Bank of India in 1955.
- Fourteen banks nationalised in 1969; six more in 1980.
- Cheque, demand draft, NEFT, RTGS and UPI are the payment instruments worth knowing by name.
- NPA :: a non-performing asset, a loan that has stopped paying. Basel norms :: capital adequacy rules.
""",
"right": """
## Measures and committees
- Poverty :: the Tendulkar committee line; the Census of 2011 is the reference count.
- Unemployment :: frictional, structural, cyclical and disguised.
- HDI :: the UNDP index with three dimensions, health, education and income.
- CPI :: retail prices. WPI :: wholesale prices. IIP :: industrial production.
- Committees worth a name :: Narasimham on banking reform, Kelkar on taxation, Rangarajan on poverty.
""",
},
"westbengal": {
"left": """
## Numbers
- Area :: 88,752 sq km. Districts :: 23. Lok Sabha seats :: 42. Rajya Sabha seats :: 16. Assembly seats :: 294.
- Borders :: five States, plus Bangladesh, Nepal and Bhutan. Coastline :: about 158 km.
- Physiographic regions :: the Darjeeling hills, the Terai and the Dooars, the Rarh, the Gangetic plains and the Sundarbans.
- Crops :: rice, jute, tea and potato, with Darjeeling tea carrying a geographical indication.
- Physiography :: the Darjeeling hills, the Terai and the Dooars, the Rarh, the Gangetic plains and the Sundarbans.
- Neighbours :: five States, and the international borders with Bangladesh, Nepal and Bhutan.
- Climate :: tropical monsoon; the northern hills are temperate, the Sundarbans humid and saline.
""",
"right": """
## Culture and institutions
- Kolkata :: the Asiatic Society 1784, the Indian Museum 1814, Calcutta University 1857, the Indian Statistical Institute 1931.
- First IIT :: Kharagpur, 1951. First metro :: Kolkata, 1984.
- Clubs :: Mohun Bagan 1889, East Bengal 1920. Eden Gardens is the State's great ground.
- Festivals :: Durga Puja, Kali Puja, Rath Yatra at Mahesh, Gangasagar Mela, Poila Boishakh, Basanta Utsav at Shantiniketan.
- Names :: Tagore, Bankim Chandra, Vidyasagar, Vivekananda, Sarat Chandra, Kazi Nazrul Islam, Satyajit Ray.
""",
},
"current": {
"left": """
## Venues and firsts worth knowing
- Narendra Modi Stadium, Ahmedabad :: the largest cricket ground in the world and the venue of the T20 World Cup 2026 final on 8 March 2026.
- Chandrayaan-3 :: the lander Vikram and the rover Pragyan; the landing site is called Shiv Shakti point.
- Aditya-L1 :: parked at the L1 point, about 1.5 million km from the earth.
- INS Vikrant :: the first aircraft carrier built in India, commissioned 2022.
""",
"right": """
## Countries and capitals that sit beside current affairs
- Bangladesh :: Dhaka. Nepal :: Kathmandu. Bhutan :: Thimphu. Myanmar :: Naypyidaw. Sri Lanka :: Sri Jayawardenepura Kotte (Colombo is the commercial capital).
- China :: Beijing. Pakistan :: Islamabad. Afghanistan :: Kabul. Maldives :: Male.
- Currencies :: taka, rupee, ngultrum, kyat, yuan, afghani, rufiyaa.

## The calendar of the year
- 26 January :: Republic Day. 15 August :: Independence Day. 2 October :: Gandhi Jayanti.
- 5 September :: Teachers' Day. 14 November :: Children's Day. 8 March :: International Women's Day.
- 14 April :: Poila Boishakh. 23 August :: the Chandrayaan-3 landing anniversary.
- An appointment question is usually one year old at most; a sports question is about the last season; a scheme question is about the last budget.
""",
},
"profit": {
"right": """
## A check you can do in ten seconds
- If CP is Rs 480 and SP is Rs 552, the profit is Rs 72 and the profit per cent is 15.
- Multiply the CP by 1.15 to get the SP back. If the multiplication does not return the SP, the answer is wrong.
- The same test works for a loss: multiply by (1 - loss/100).
""",
},
"discount": {
"right": """
## The two-step check
- Marked Rs 800, discount 20 per cent, so SP is Rs 640. Divide back by 0.8 and the marked price returns.
- A discount of 25 per cent is a factor of 3/4; a mark-up of 25 per cent is 5/4. They are not inverses.
- When the question gives a profit after a discount, first find SP from MP, then compare with CP.
""",
},
"si": {
"right": """
## A check you can do in ten seconds
- Rs 2,500 at 4 per cent for 3 years gives Rs 300 of simple interest, so the amount is Rs 2,800.
- Interest per year is P x R/100; multiply by the years and you are done.
- If the question gives the amount, subtract the principal before dividing by the rate.
""",
},
"ci": {
"right": """
## A check you can do in ten seconds
- Rs 2,500 at 4 per cent for 3 years gives about Rs 312 of compound interest, against Rs 300 of simple interest.
- The extra 12 rupees is the interest on interest; it grows with the square of the rate.
- For two years, compute the simple interest and add P(R/100)^2; it is faster than the full power.
""",
},
"ratio": {
"right": """
## Checks
- If 12 men do a job in 18 days, the work is 216 man-days. Any other combination must multiply to 216.
- Convert every ratio to parts of the same whole before comparing two ratios.
- In a proportion a : b = c : d, cross-multiply to check; if ad is not equal to bc, the proportion is wrong.
""",
},
"work": {
"right": """
## Checks
- A in 12 days and B in 18 days together take 7.2 days, which is less than either alone and more than half the faster time.
- If your answer is longer than the faster worker's time, the arithmetic is wrong.
- Convert the final answer back into days and fractions of a day; 7.2 days is 7 days and about 5 hours.
""",
},
"ages": {
"right": """
## Checks
- Every age you compute must be positive and the older person must stay older.
- Substitute the answer back into the sentence, in the year the sentence describes.
- If the ages come out fractional, re-read the sentence; these questions are built to give whole numbers.
""",
},
"series": {
"right": """
## Checks
- Two independent routes to the same answer is the standard: differences and the pattern.
- If the numbers are all perfect squares, test the square roots as a series of their own.
- If the answer choices are far apart, an approximate rule is enough; if they are close, compute exactly.
""",
},
"mixture": {
"right": """
## Checks
- The mean price must lie between the two prices; if it does not, the question is misread.
- After replacement, the quantity of the original liquid must fall but never reach zero.
- The total volume in the vessel is unchanged by a replacement, which is the assumption the formula rests on.
""",
},
"analogy": {
"right": """
## Checks
- Say the relation aloud before choosing, then say it again with your answer in place.
- If the sentence sounds wrong with the answer, the answer is wrong, however familiar the words look.
- For number analogies, compute both sides; a rule that works on one side only is not a rule.
""",
},
"oddone": {
"right": """
## Checks
- Name the shared property of three of the four before you choose; if you cannot name it, look again.
- Squares to 30 squared :: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900.
- Cubes to 12 :: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728.
""",
},
}

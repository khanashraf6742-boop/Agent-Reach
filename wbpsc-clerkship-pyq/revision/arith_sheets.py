# -*- coding: utf-8 -*-
"""Twenty-three formula sheets, one page per topic, in the order of the book.

Worked examples are computed here (Python arithmetic) rather than typed, so a
printed number cannot disagree with its own formula.  formula_tests.py then
re-derives each formula from independent textbook inputs.
"""


def n(x):
    """Format a number the way a solution sheet would write it."""
    if abs(x - round(x)) < 1e-9:
        return f"{int(round(x))}"
    s = f"{x:.4f}".rstrip("0").rstrip(".")
    return s


def money(x):
    return f"Rs {n(x)}"


TOPICS = []


def add(**kw):
    TOPICS.append(kw)


# 1 -------------------------------------------------------------------------
P, R, T = 1200, 6, 2
si = P * R * T / 100
add(key="percentage", tag="Percentage", kicker="Formula sheet 1 of 23",
    title="Percentage",
    sub="The base question behind profit, discount, interest and every data question",
    left=f"""
## The formulas
= x per cent of N = (x / 100) x N
= a as a percentage of b = (a / b) x 100
= Percentage change = ((new - old) / old) x 100 | the base is always the old value
= Successive change of a per cent then b per cent = a + b + (a x b)/100 | the sign matters: a fall is negative
= Price rises by r per cent; consumption must fall by = (100r) / (100 + r) per cent | to keep the spend the same
= Price falls by r per cent; consumption may rise by = (100r) / (100 - r) per cent
= If A is x per cent more than B, then B is = (100x) / (100 + x) per cent less than A

## Fractions worth knowing cold
- 1/2 = 50 per cent. 1/3 = 33.33. 1/4 = 25. 1/5 = 20. 1/6 = 16.67. 1/7 = 14.28. 1/8 = 12.5. 1/9 = 11.11. 1/10 = 10.
- 1/12 = 8.33. 1/15 = 6.67. 1/16 = 6.25. 1/20 = 5. 1/25 = 4. 1/40 = 2.5.
- 2/3 = 66.67. 3/4 = 75. 2/5 = 40. 3/5 = 60. 5/8 = 62.5. 7/8 = 87.5.

## The four types in the paper
- Find the part :: what is 15 per cent of 240. Multiply and divide by 100.
- Find the whole :: 45 is 15 per cent of what. Divide by the percentage.
- Find the rate :: 45 is what per cent of 300.
- Two changes in a row :: a rise then a fall; use the successive formula, never add.
""",
    right=f"""
## Worked example
- A number is increased by 20 per cent and then decreased by 20 per cent. What is the net change?
= Net = 20 + (-20) + (20 x -20)/100 = -4 | a fall of 4 per cent
- The trap :: most candidates answer "no change". The two percentages are taken on different bases, so the fall is on a bigger number.

## Second worked example
- The price of rice rises by 25 per cent. By what per cent must a family cut consumption to keep its bill unchanged?
= 100 x 25 / (100 + 25) = 20 per cent
- Check :: 100 kg at Rs 4 costs Rs 400. New price Rs 5. To spend Rs 400 buy 80 kg, which is 20 per cent less.

## Shortcuts
- To increase by 12.5 per cent, multiply by 9/8. To decrease by 12.5, multiply by 7/8.
- To increase by 16.67 per cent, multiply by 7/6. By 14.28 per cent, multiply by 8/7.
- A rise of a per cent then b per cent multiplies by (1 + a/100)(1 + b/100). Chain the fractions instead of adding.
- "X per cent more than" and "X per cent less than" run on different bases; convert to fractions before you compare.

## Traps
* Adding two successive percentages. 20 then 20 is not 40, it is 44 for two rises and minus 4 for a rise and a fall.
* Taking the percentage on the new value when the question fixed the old one.
* Confusing "per cent of" with "per cent more than": 25 per cent of 80 is 20; 25 per cent more than 80 is 100.
* In a fraction table, writing 1/6 as 16.6 and then rounding at every step.

## Where it is hidden
- Profit and loss, discount, simple and compound interest, mixture, data interpretation and even time and work all begin as a percentage of a base. If a question feels ambiguous, ask "percentage of what".
""",
)

# 2 -------------------------------------------------------------------------
cp, sp = 900, 945
add(key="profit", tag="Profit and loss", kicker="Formula sheet 2 of 23",
    title="Profit and loss",
    sub="Everything is measured on the cost price unless the question says otherwise",
    left=f"""
## The formulas
= Profit = SP - CP. Loss = CP - SP
= Profit per cent = (Profit / CP) x 100. Loss per cent = (Loss / CP) x 100 | the base is CP, never SP
= SP = CP x (100 + p)/100. CP = SP x 100/(100 + p) | with a loss, use (100 - l)
= If an article is sold at a gain of p per cent, the gain on the selling price is = 100p/(100 + p) per cent
= Two articles sold at the same price, one at a gain of x per cent and one at a loss of x per cent, give a net = loss of x squared / 100 per cent | always a loss, never a gain
= Dishonest dealer using a false weight :: gain per cent = (true weight - false weight) / false weight x 100
= Marked price and discount :: SP = MP x (100 - d)/100; then profit per cent is measured on CP

## The four types
- Cost to selling :: given CP and the profit per cent, find SP.
- Selling to cost :: given SP and the profit or loss per cent, find CP. Divide, do not multiply.
- Find the rate :: given CP and SP.
- Two-part questions :: a shopkeeper marks up by x per cent and then allows a discount of y per cent; multiply the two factors.
""",
    right=f"""
## Worked example
- A shopkeeper buys an article for Rs 900 and sells it for Rs 945. Find his profit per cent.
= Profit = 945 - 900 = Rs 45
= Profit per cent = (45 / 900) x 100 = 5 per cent
- The trap :: dividing by the selling price gives 4.76 per cent, which is the gain on SP, not the answer.

## Second worked example
- By selling a chair for Rs 720 a carpenter loses 10 per cent. What did it cost him?
= CP = 720 x 100/90 = Rs 800
- Check :: a loss of 10 per cent on 800 is 80, and 800 - 80 = 720.

## Shortcuts
- Successive mark-up and discount :: multiply (100 + m)/100 by (100 - d)/100 to get SP/CP in one line.
- If the profit per cent equals the loss per cent on two articles sold at the same price, the seller always loses. The loss is x squared/100 per cent of the total cost.
- Keep everything in fractions. A profit of 25 per cent is a factor of 5/4; a loss of 20 per cent is 4/5.
- When the answer choices are close, compute the CP from the SP rather than the other way round; division is where the error hides.

## Traps
* Measuring profit on the selling price. Only the gain "on SP" questions do that, and they say so.
* Forgetting that discount is on the marked price while profit is on the cost price.
* Two articles at the same selling price giving "no profit no loss" when the percentages are equal.
* Writing "Rs 45 profit" when the question asked for the percentage, or the reverse.
""",
)

# 3 -------------------------------------------------------------------------
add(key="discount", tag="Discount", kicker="Formula sheet 3 of 23",
    title="Discount",
    sub="Discount lives on the marked price; profit lives on the cost price",
    left="""
## The formulas
= Discount = MP - SP. Discount per cent = (Discount / MP) x 100
= SP = MP x (100 - d)/100. MP = SP x 100/(100 - d)
= Two successive discounts of a and b per cent are equivalent to a single discount of = a + b - (a x b)/100 per cent
= Three successive discounts :: multiply the three factors (100 - a)(100 - b)(100 - c) / 100^3
= SP after a discount of d per cent and then a further discount of e per cent on the reduced price = MP x (1 - d/100)(1 - e/100)
= Successive discounts never add :: 20 and 10 give 28, not 30 | the second is taken on the already reduced price

## The four types
- Single discount :: MP and rate given, find SP.
- Find the rate :: MP and SP given.
- Two successive discounts :: the standard question; use the combined formula.
- Discount then profit :: mark-up first, discount second, profit on CP last.

## Why the single-discount formula works
- Take MP 100. A discount of a per cent leaves 100 - a. A further b per cent leaves (100 - a)(100 - b)/100.
- The single equivalent discount is 100 minus that, which simplifies to a + b - ab/100.
""",
    right="""
## Worked example
- Two successive discounts of 15 per cent and 20 per cent are equivalent to a single discount of what?
= Single = 15 + 20 - (15 x 20)/100 = 35 - 3 = 32 per cent
- Check on MP 100 :: 15 per cent leaves 85; 20 per cent of 85 is 17, leaving 68. A discount of 32 per cent on 100 also leaves 68.

## Second worked example
- A shirt marked Rs 1,200 is sold after two discounts of 10 per cent and 5 per cent. Find the selling price.
= SP = 1200 x 0.90 x 0.95 = Rs 1,026
- Check :: the single equivalent discount is 10 + 5 - 0.5 = 14.5 per cent, and 1200 x 0.855 = 1,026.

## Shortcuts
- Chain the factors: 0.9 x 0.95 = 0.855. One multiplication beats two subtractions.
- A discount of 50 per cent followed by 50 per cent is a discount of 75 per cent, not 100.
- To undo a discount, divide by the factor; to apply one, multiply.
- In questions with a mark-up, do the mark-up on CP and the discount on MP, then compare SP with CP.

## Traps
* Adding successive discounts, which overstates the reduction by ab/100.
* Taking the second discount on the original marked price instead of the reduced price.
* Mixing the bases: a 20 per cent mark-up and a 20 per cent discount leave a loss of 4 per cent, not a wash.
* Reading "a discount of 20 per cent on the marked price" as a profit of 20 per cent on cost.
""",
)

# 4 -------------------------------------------------------------------------
add(key="si", tag="Simple interest", kicker="Formula sheet 4 of 23",
    title="Simple interest",
    sub="Interest on the original principal only, never on the interest",
    left=f"""
## The formulas
= SI = (P x R x T) / 100 | P principal, R rate per cent per year, T time in years
= Amount A = P + SI = P (1 + RT/100)
= P = (100 x SI) / (R x T). R = (100 x SI) / (P x T). T = (100 x SI) / (P x R)
= Money doubles itself at simple interest in = 100/R years | at 8 per cent, 12.5 years
= Money becomes k times in = 100(k - 1)/R years
= If a sum becomes A1 in T1 years and A2 in T2 years, then = P = (A2 x T1 - A1 x T2) / (T1 - T2) and R follows from SI
= Equal instalments under simple interest :: each instalment reduces the principal, so the interest is charged only on the balance

## The four types
- Find the interest :: P, R, T given.
- Find the rate or the time :: SI, P and one of R or T given.
- Doubling and trebling :: use the 100/R rule and its multiples.
- Two amounts at two times :: the difference of the amounts is the interest for the difference of the times.

## Why the formula is linear
- Each year adds the same interest, P x R/100, because the principal never changes.
- That is the whole difference from compound interest, where each year's interest joins the principal.
""",
    right=f"""
## Worked example
- Find the simple interest on Rs 1,200 at 6 per cent per annum for 2 years.
= SI = (1200 x 6 x 2)/100 = Rs {n(si)}
= Amount = 1200 + {n(si)} = Rs {n(1200 + si)}
- The trap :: multiplying by the number of months instead of the fraction of a year.

## Second worked example
- A sum amounts to Rs 1,344 in 2 years and Rs 1,416 in 3 years at simple interest. Find the principal.
= Interest for one year = 1416 - 1344 = Rs 72
= Interest for two years = Rs 144
= Principal = 1344 - 144 = Rs 1,200
- Check :: 72 x 100/(1200 x 1) = 6 per cent per annum.

## Shortcuts
- Convert the time to years first: 8 months is 8/12, 15 months is 5/4.
- If time is given in days, use 365 unless the question says ordinary or commercial year.
- Doubling at simple interest is exactly 100/R years; trebling is 200/R. No logarithms needed.
- For "what rate gives the same interest on half the sum in twice the time", set the products PRT equal.

## Traps
* Mixing years and months without converting.
* Using the amount in place of the principal in the formula.
* Expecting simple interest to double in fewer years at a lower rate.
* Adding the interest to the principal at the end of each year, which is a compound interest question wearing a simple interest label.
""",
)

# 5 -------------------------------------------------------------------------
p5, r5, t5 = 1000, 10, 2
ci5 = p5 * (1 + r5 / 100) ** t5 - p5
si5 = p5 * r5 * t5 / 100
add(key="ci", tag="Compound interest", kicker="Formula sheet 5 of 23",
    title="Compound interest",
    sub="Interest that joins the principal, and the two-year gap that is always asked",
    left=f"""
## The formulas
= A = P (1 + R/100)^T. CI = A - P
= Half-yearly :: rate R/2 and time 2T. Quarterly :: rate R/4 and time 4T
= Difference between CI and SI for two years = P (R/100)^2
= Difference for three years = P (R/100)^2 x (3 + R/100)
= CI for two years = P [(1 + R/100)^2 - 1] = P (2R/100 + R^2/10000)
= If a sum becomes k times in T years, it becomes k^2 times in 2T years and k^3 in 3T | powers, not multiples
= Rule of 72 :: money doubles in about 72/R years at compound interest, a useful check, not an answer

## The four types
- Find the amount :: P, R, T given.
- Find the difference :: CI minus SI over two or three years.
- Compounding more often :: half-yearly, quarterly, sometimes monthly.
- Growth and decay :: population, depreciation, bacteria; depreciation uses (1 - R/100).
""",
    right=f"""
## Worked example
- Find the compound interest on Rs 1,000 at 10 per cent for 2 years, and the difference from simple interest.
= A = 1000 x (1.1)^2 = Rs 1,210, so CI = Rs {n(ci5)}
= SI = (1000 x 10 x 2)/100 = Rs {n(si5)}
= Difference = {n(ci5)} - {n(si5)} = Rs {n(ci5 - si5)}
= Check by the formula :: 1000 x (10/100)^2 = Rs 10. Correct.

## Second worked example
- Find the amount on Rs 8,000 at 10 per cent for 1 year compounded half-yearly.
= Rate becomes 5 per cent and time 2 half-years
= A = 8000 x (1.05)^2 = 8000 x 1.1025 = Rs 8,820

## Shortcuts
- For two years, the second year's interest is charged on the first year's interest as well; that extra is exactly P(R/100)^2.
- Successive percentage change and compound interest are the same formula; R per cent for T years is (1 + R/100) applied T times.
- Depreciation, population decline, and a machine losing value all use the same bracket with a minus sign.
- For three years at small rates, the difference is roughly three times the two-year difference.

## Traps
* Applying the simple interest formula for a period longer than one year when interest is compounded.
* Halving the time as well as the rate for half-yearly compounding, instead of doubling the periods.
* Treating "becomes 3 times in 4 years" as "becomes 6 times in 8 years"; it is 9 times.
* Subtracting CI and SI the wrong way round when the question asks for the difference.
""",
)

# 6 -------------------------------------------------------------------------
add(key="ratio", tag="Ratio", kicker="Formula sheet 6 of 23",
    title="Ratio and proportion",
    sub="The quietest topic in the paper and the one that unlocks the most others",
    left="""
## The formulas
= a : b = c : d means a x d = b x c | the product of the extremes equals the product of the means
= Compound ratio of a : b and c : d = ac : bd. Duplicate ratio of a : b = a^2 : b^2. Triplicate = a^3 : b^3
= Sub-duplicate = the square roots; inverse ratio of a : b = b : a
= Third proportional to a and b = b^2/a. Fourth proportional to a, b and c = bc/a
= Mean proportional between a and b = the square root of (a x b)
= Dividing a sum S in the ratio a : b : c gives = S x a/(a + b + c), and so on
= Partnership :: profit shares are in the ratio of capital x time
= If a : b = 2 : 3 and b : c = 4 : 5, then a : b : c = 8 : 12 : 15 | make the common term equal

## The four types
- Simplify or combine :: two ratios sharing a term.
- Divide a quantity :: in a given ratio.
- Find a missing term :: fourth, third or mean proportional.
- Proportion word problems :: mixture, partnership, ages and map scales.
""",
    right="""
## Worked example
- Two numbers are in the ratio 3 : 5 and their sum is 96. Find them.
= Total parts = 3 + 5 = 8, and one part = 96/8 = 12
= The numbers are 36 and 60
- Check :: 36 : 60 = 3 : 5 and 36 + 60 = 96.

## Second worked example
- A and B invest Rs 5,000 and Rs 8,000. A leaves after 6 months, B stays the year. Divide a profit of Rs 3,600.
= Ratio = 5000 x 6 : 8000 x 12 = 30,000 : 96,000 = 5 : 16
= A's share = 3600 x 5/21 = Rs 857.14, B's = Rs 2,742.86

## Shortcuts
- To combine a : b and b : c, multiply the first ratio by the b of the second and the second by the b of the first.
- If a : b = 2 : 3, write the numbers as 2x and 3x and let the equation do the work.
- In a partnership, the ratio is capital times months; never capital alone unless the times are equal.
- When a ratio is increased by adding the same number to both terms, the ratio moves towards 1.

## Traps
* Adding the same amount to both terms and expecting the ratio to stay the same.
* Using the ratio as if it were the actual value; 3 : 5 means 3x and 5x, not 3 and 5.
* Ignoring time in partnership questions.
* Reversing the order when the question asks for b : a.
""",
)

# 7 -------------------------------------------------------------------------
add(key="average", tag="Average", kicker="Formula sheet 7 of 23",
    title="Average",
    sub="A total divided by a count, and the small changes that decide the answer",
    left="""
## The formulas
= Average = sum of the terms / number of terms. Sum = average x number
= If one term is replaced by another, the average changes by = (new - old) / number of terms
= Average of the first n natural numbers = (n + 1)/2. Of the first n odd numbers = n. Of the first n even numbers = n + 1
= Average of consecutive numbers = the middle one. Of an odd count, the middle term; of an even count, the mean of the two middles
= Weighted average = (sum of value x weight) / (sum of weights)
= Average speed for equal distances = 2xy/(x + y) | not (x + y)/2
= If a person travels a distance at x and returns at y, the average speed for the whole journey = 2xy/(x + y)
= New member joins :: new average = (old total + new value)/(n + 1)

## The four types
- Plain average :: sum and count given.
- Change by replacement :: one value leaves and another arrives.
- Average of series :: consecutive numbers, squares, odd and even runs.
- Average speed and weighted average :: two or more groups merged.
""",
    right="""
## Worked example
- The average age of 20 students is 15 years. A teacher joins and the average becomes 15.5. Find the teacher's age.
= Old total = 20 x 15 = 300
= New total = 21 x 15.5 = 325.5
= Teacher = 325.5 - 300 = 25.5 years
- Check :: 325.5/21 = 15.5. Correct.

## Second worked example
- A man goes to a town at 30 km per hour and returns at 20 km per hour. Find his average speed.
= Average = 2 x 30 x 20/(30 + 20) = 1200/50 = 24 km per hour
- The trap :: the arithmetic mean of 30 and 20 is 25, and it is wrong, because he spends longer at the slower speed.

## Shortcuts
- For an even run of consecutive numbers, the average is the mean of the first and last.
- If every term is increased by 5, the average rises by exactly 5.
- For average speed on equal distances, the harmonic mean; on equal times, the simple mean.
- To find a missing term from an average, subtract the known total from the required total instead of writing an equation.

## Traps
* Using the arithmetic mean for average speed.
* Dividing by the wrong count after a member leaves or joins.
* Forgetting that the average of a set of consecutive numbers is its middle, which wastes a minute of working.
* Treating a weighted average as if all the groups had the same size.
""",
)

# 8 -------------------------------------------------------------------------
add(key="work", tag="Time and work", kicker="Formula sheet 8 of 23",
    title="Time and work",
    sub="Turn every time into a rate, add the rates, and the answer follows",
    left="""
## The formulas
= If A finishes in a days, A's one day's work = 1/a
= A and B together :: 1/a + 1/b = 1/t, so t = ab/(a + b)
= A alone, given A and B together and B alone :: 1/a = 1/t - 1/b
= Work done in n days = n x (rate). Work left = 1 - that
= Efficiency is inversely proportional to time :: if A is twice as fast as B, A takes half the time
= Men, days, hours, work :: (M1 D1 H1)/W1 = (M2 D2 H2)/W2
= Wages are shared in the ratio of work done, which for the same job is the ratio of the rates, 1/a : 1/b
= Pipes and cisterns :: an inlet fills at +1/a, an outlet empties at -1/b; add them with signs

## The four types
- Together :: two or three workers, find the time.
- One alone :: the pair's time and one worker's time given.
- Work left :: how much remains after n days, and who finishes it.
- Pipes :: filling and emptying at the same time; a leak; a pipe closed partway.

## The one idea
- Time is the enemy; rate is the friend. Convert every "in x days" to "1/x per day" before touching the arithmetic.
""",
    right="""
## Worked example
- A can do a job in 12 days and B in 18 days. How long will they take together?
= Rates 1/12 and 1/18; common denominator 36
= Together = 3/36 + 2/36 = 5/36 per day
= Time = 36/5 = 7.2 days
- Check :: in 7.2 days A does 7.2/12 = 0.6 and B does 0.4; total 1.

## Second worked example
- A and B together finish in 6 days, A alone in 10 days. How long for B alone?
= 1/b = 1/6 - 1/10 = (5 - 3)/30 = 2/30
= b = 15 days

## Shortcuts
- Use the LCM trick: take the total work as the LCM of the times (36 here), so A does 3 units a day and B 2; together 5, and 36/5 follows instantly.
- For three workers, the same trick with three rates.
- If a pipe fills in 6 hours and a leak empties in 9, the net rate is 1/6 - 1/9 = 1/18, so 18 hours.
- If A is x times as efficient as B and together they take t days, then B alone takes t(x + 1) days.

## Traps
* Adding times instead of rates. 12 and 18 together is never 30.
* Forgetting to convert the answer back to days when the rate is per day.
* Losing the sign when an outlet pipe empties the tank.
* Paying wages by time when the question says work; wages follow the rates, so the slower worker gets less per day.
""",
)

# 9 -------------------------------------------------------------------------
add(key="tsd", tag="Time and distance", kicker="Formula sheet 9 of 23",
    title="Time and distance",
    sub="One relation, three rearrangements, and the 5/18 that saves a minute",
    left="""
## The formulas
= Speed = distance/time. Distance = speed x time. Time = distance/speed
= km per hour to metre per second :: multiply by 5/18. The other way :: multiply by 18/5
= Relative speed :: opposite directions, add; same direction, subtract
= Average speed = total distance / total time | never the mean of the speeds unless the times are equal
= Equal distances at x and y :: average = 2xy/(x + y)
= If a man covers a distance at x and returns at y, the average speed for the whole journey = 2xy/(x + y)
= Late and early :: if by going at x he is late by t1 and at y early by t2, then = distance = xy(t1 + t2)/(y - x), with the times in the same unit
= A journey with a halt :: total time = running time + halt

## The four types
- One leg :: a single speed, find time or distance.
- Two legs :: different speeds, find the average.
- Two objects :: relative speed, meeting point, catching up.
- Late and early :: the same distance at two speeds with a clock condition.
""",
    right="""
## Worked example
- A train covers 240 km in 4 hours. Find its speed in metre per second.
= Speed = 240/4 = 60 km per hour
= 60 x 5/18 = 16.67 metre per second
- Check :: 60 km in an hour is 60000 m in 3600 s, which is 16.67 m/s.

## Second worked example
- A man walks to office at 5 km per hour and is 10 minutes late; at 6 km per hour he is 5 minutes early. Find the distance.
= Difference of time = 15 minutes = 1/4 hour
= d/5 - d/6 = 1/4, so d/30 = 1/4 and d = 7.5 km
- Check :: 7.5/5 = 1.5 hours and 7.5/6 = 1.25, a difference of 15 minutes.

## Shortcuts
- 36 km per hour is 10 m/s; 54 is 15; 72 is 20; 90 is 25. Learn the family.
- For "same distance, two speeds", go straight to 2xy/(x + y).
- Draw a line with the meeting point marked; relative speed and a timeline solve most two-object questions in one line.
- In late-and-early questions, the difference of the two times equals the difference of lateness plus earliness.

## Traps
* Averaging 40 and 60 to get 50 when the distances are equal; the answer is 48.
* Mixing km per hour with metres per second inside one calculation.
* Adding speeds when the objects move in the same direction.
* Forgetting to convert minutes to hours before multiplying by a speed.
""",
)

# 10 ------------------------------------------------------------------------
add(key="trains", tag="Trains", kicker="Formula sheet 10 of 23",
    title="Trains",
    sub="A moving length crossing a fixed or moving length",
    left="""
## The formulas
= Time to cross a pole or a standing man = length of the train / speed of the train
= Time to cross a platform or a bridge = (length of train + length of platform) / speed
= Two trains in opposite directions :: time = (L1 + L2)/(v1 + v2)
= Two trains in the same direction :: time = (L1 + L2)/(v1 - v2) | the faster one overtakes
= A train crossing another train is always a length question, never a distance-between-cities question
= If a train of length L crosses a platform of length P in t seconds, its speed = (L + P)/t
= Passengers in a moving train :: a man in one train crosses a second train of length L at the relative speed, because his own train's length does not count

## The four types
- Pole, man, signal :: only the train's own length.
- Platform or bridge :: both lengths.
- Two trains, opposite directions :: add the speeds.
- Two trains, same direction :: subtract the speeds, and check which is faster.
""",
    right="""
## Worked example
- A train 120 m long crosses a platform 180 m long in 20 seconds. Find its speed.
= Total length = 120 + 180 = 300 m
= Speed = 300/20 = 15 metre per second
= In km per hour :: 15 x 18/5 = 54 km per hour

## Second worked example
- Two trains of 150 m and 250 m run in opposite directions at 40 and 50 km per hour. How long do they take to cross?
= Relative speed = 90 km per hour = 90 x 5/18 = 25 metre per second
= Total length = 400 m
= Time = 400/25 = 16 seconds

## Shortcuts
- Convert every speed to metre per second before dividing by a length in metres. One conversion at the start beats three at the end.
- For a train crossing a man walking along the track, the relative speed depends on the direction of the walk.
- If two trains of equal length cross each other in t seconds, the time to cross a pole is half the time when the speeds are equal.
- When a train passes two bridges of different lengths, the difference of the times gives the speed: speed = difference of lengths / difference of times.

## Traps
* Using only the train's length for a platform question.
* Adding the speeds for trains going the same way, or subtracting when they are opposite.
* Converting the length to kilometres but the speed to metres per second.
* Forgetting that a man sitting in one train travels with it, so his own length is not added.
""",
)

# 11 ------------------------------------------------------------------------
add(key="boats", tag="Boats and streams", kicker="Formula sheet 11 of 23",
    title="Boats and streams",
    sub="Downstream adds the current, upstream takes it away",
    left="""
## The formulas
= Downstream speed = speed of boat in still water + speed of stream = b + s
= Upstream speed = b - s
= Speed in still water = (downstream + upstream)/2. Speed of stream = (downstream - upstream)/2
= Time downstream = D/(b + s). Time upstream = D/(b - s)
= For the same distance, time downstream : time upstream = (b - s) : (b + s)
= Round trip :: total time = D/(b + s) + D/(b - s) = 2Db/(b^2 - s^2)
= If a boat takes t1 hours downstream and t2 hours upstream for the same distance, then = b/s = (t2 + t1)/(t2 - t1)
= A boat with no current :: s = 0 and both speeds are equal

## The four types
- Speeds from the two directions :: the standard pair.
- Time for one direction :: a distance and the speeds.
- Round trip :: the total time for going and returning.
- Two boats or a floating object :: a raft moves at the speed of the stream.
""",
    right="""
## Worked example
- A boat travels 20 km downstream in 2 hours. If the stream runs at 2 km per hour, find the boat's speed in still water.
= Downstream speed = 20/2 = 10 km per hour
= Still water = 10 - 2 = 8 km per hour
- Check :: upstream would be 8 - 2 = 6, and 20 km upstream would take 3 hours 20 minutes.

## Second worked example
- A boat goes 12 km downstream and returns in 3 hours 12 minutes. If the stream is 2 km per hour, find the boat's speed in still water.
= Total time = 3.2 hours
= 12/(b + 2) + 12/(b - 2) = 3.2
= 24b = 3.2 (b^2 - 4), so 3.2b^2 - 24b - 12.8 = 0, giving b = 8 km per hour
- Check :: 12/10 + 12/6 = 1.2 + 2 = 3.2 hours.

## Shortcuts
- Always compute the two speeds first, downstream and upstream; almost every question is then a one-step division.
- For a round trip, the harmonic form 2Db/(b^2 - s^2) saves a quadratic.
- A raft or a floating log travels at exactly the speed of the stream; a question that mentions one is telling you s.
- If the time ratio is 3 : 5, the speed ratio is 5 : 3, and the speeds follow from the sum and difference formulas.

## Traps
* Adding the stream speed when the boat goes upstream.
* Using the still-water speed as the downstream speed.
* Forgetting that the round trip has two different times, so the average speed is not b.
* Treating a raft as a boat with a motor.
""",
)

# 12 ------------------------------------------------------------------------
add(key="mixture", tag="Mixture", kicker="Formula sheet 12 of 23",
    title="Mixture and alligation",
    sub="The see-saw rule, and the replacement formula that follows from it",
    left="""
## The formulas
= Alligation :: the ratio of the cheaper to the dearer = (price of dearer - mean) : (mean - price of cheaper)
= Mean price = (quantity1 x price1 + quantity2 x price2) / (quantity1 + quantity2)
= Repeated replacement :: if a vessel of V litres holds pure liquid and k litres are drawn and replaced by water, n times, the pure liquid left = V (1 - k/V)^n
= For a mixture of two components, the ratio after one replacement = (V - k) : k, if k is replaced by the other component
= Mixing two solutions of the same substance :: the concentration of the mixture is the weighted mean of the concentrations
= Milk and water :: work in parts; if the ratio is a : b, the fraction of milk is a/(a + b)

## The four types
- Two ingredients, find the ratio :: the alligation cross.
- Find the mean price :: a weighted average.
- Repeated replacement :: the (1 - k/V)^n formula, the one everyone forgets.
- Removing and replacing with the same liquid :: concentration falls geometrically.
""",
    right="""
## Worked example
- In what ratio must rice at Rs 40 a kg be mixed with rice at Rs 55 a kg so that the mixture costs Rs 46 a kg?
= Cheaper : dearer = (55 - 46) : (46 - 40) = 9 : 6 = 3 : 2
- Check :: 3 kg at 40 and 2 kg at 55 cost 120 + 110 = 230 for 5 kg, which is Rs 46.

## Second worked example
- A vessel holds 40 litres of milk. 8 litres are drawn out and replaced by water, twice over. How much milk remains?
= Milk left = 40 (1 - 8/40)^2 = 40 x (0.8)^2 = 40 x 0.64 = 25.6 litres
- Check :: after the first replacement 32 litres of milk remain; after the second, 80 per cent of that, 25.6.

## Shortcuts
- Draw the cross: write the two prices, the mean in the middle, and subtract diagonally. The two differences are the ratio, cheaper first.
- For replacement questions, the fraction left after one operation is (1 - k/V); raise it to the number of operations.
- If a mixture is sold at cost price but diluted, the profit is the value of the water added.
- In alligation with three ingredients, do it in two pairs.

## Traps
* Subtracting in the wrong order and getting the ratio upside down; the cheaper quantity always pairs with the larger difference.
* Using simple interest thinking for replacement, subtracting k/V each time instead of multiplying.
* Forgetting that the vessel's total volume stays the same after replacement.
* Mixing percentages of different bases, such as 40 per cent of 30 litres with 60 per cent of 20 litres.
""",
)

# 13 ------------------------------------------------------------------------
add(key="ages", tag="Problems on ages", kicker="Formula sheet 13 of 23",
    title="Problems on ages",
    sub="One variable, one equation, and a translation you must get right",
    left="""
## The method
= Let the present ages be x and y. Every statement is about a different time, and the difference never changes
= "A is t years older than B" :: x - y = t, at every point in time
= "Five years ago" :: x - 5 and y - 5. "Five years hence" :: x + 5 and y + 5
= "A is twice as old as B" :: x = 2y now; five years ago it was x - 5 = 2(y - 5), a different equation
= Ratio now a : b :: write the ages as ax and bx
= If the ratio of ages is a : b now and c : d after t years, then (ax + t)/(bx + t) = c/d
= The sum of ages changes by n x (number of people) every year

## The four types
- Present ages from a ratio and a difference.
- Ages t years ago or hence.
- Two people, two times :: the ratio method.
- Father and son, mother and daughter :: the standard pair, always one older by a fixed number.
""",
    right="""
## Worked example
- A father is three times as old as his son. Ten years hence he will be twice as old. Find their present ages.
= Now :: f = 3s. In ten years :: f + 10 = 2(s + 10)
= Substituting :: 3s + 10 = 2s + 20, so s = 10 and f = 30
- Check :: in ten years the son is 20 and the father 40, which is twice.

## Second worked example
- The ages of A and B are in the ratio 5 : 7. Four years ago the ratio was 3 : 5. Find their ages.
= (5x - 4)/(7x - 4) = 3/5 gives 25x - 20 = 21x - 12, so 4x = 8 and x = 2
= A is 10 and B is 14
- Check :: four years ago they were 6 and 10, a ratio of 3 : 5.

## Shortcuts
- Take the ratio as ax and bx, not as a and b. One unknown beats two.
- Write "ago" as a minus on both ages, and check the equation against the sentence before solving.
- If the question gives a sum and a difference, solve by adding and subtracting, not by substitution.
- Test the answer choices when the equation looks messy; ages are small integers, and a choice is often quicker than the algebra.

## Traps
* Applying "twice as old" to the present age when the question describes a past or future year.
* Forgetting to subtract from both people when the question says "five years ago".
* Assuming the ratio of ages stays constant; it changes every year.
* Mixing up who is older when the answer choices are close.
""",
)

# 14 ------------------------------------------------------------------------
add(key="series", tag="Number series", kicker="Formula sheet 14 of 23",
    title="Number series",
    sub="Find the rule by taking differences before you guess",
    left="""
## The tools
= Arithmetic progression :: a, a + d, a + 2d. The nth term = a + (n - 1)d. The sum = (n/2)(2a + (n - 1)d)
= Geometric progression :: a, ar, ar^2. The nth term = a r^(n - 1)
= First differences constant :: linear rule. Second differences constant :: a square rule, n^2 with a coefficient
= Alternating series :: two interleaved series, one in the odd places and one in the even
= Squares and cubes :: 1, 4, 9, 16, 25 and 1, 8, 27, 64, 125 are the skeletons of half the series in the paper
= Products :: 1x2, 2x3, 3x4 appears as 2, 6, 12, 20; the rule is n(n + 1)
= Primes :: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31
= Fibonacci-like :: each term the sum of the two before it

## The four types
- Difference series :: add a constant, or add a changing difference.
- Multiplication series :: x2, x3, then plus or minus a small number.
- Square and cube series :: n^2 + 1, n^3 - 1, and their cousins.
- Two-tier series :: odd places and even places obey different rules.
""",
    right="""
## Worked example
- Find the next term: 8, 15, 22, 29, 36, ?
= First differences :: 7, 7, 7, 7, so the rule is "add 7"
= Next term = 36 + 7 = 43

## Second worked example
- Find the next term: 2, 6, 12, 20, 30, ?
= The terms are 1x2, 2x3, 3x4, 4x5, 5x6
= Next is 6x7 = 42
- Check with differences :: 4, 6, 8, 10, then 12, which gives 42. Two routes, one answer.

## The method that works
- Write the series, then write the first differences underneath, then the second differences.
- If the first differences are constant, it is arithmetic. If the second are constant, it is quadratic.
- If the numbers grow fast, test multiplication and division before addition.
- If the series jumps around, split it into odd and even positions.
- Check the answer against the choices; a wrong rule rarely produces a listed option.

## Traps
* Guessing a rule from two terms. Two terms fit a thousand rules; take differences first.
* Assuming a square series when the differences are merely increasing.
* Forgetting that a series can multiply and then add, in the same step.
* Ignoring the odd-even split in a series that alternates up and down.
""",
)


# 15 ------------------------------------------------------------------------
add(key="coding", tag="Coding and decoding", kicker="", title="Coding and decoding",
    sub="The alphabet is a number line from 1 to 26; every code is a move on it",
    left="""
## The alphabet as numbers
- A 1, B 2, C 3, D 4, E 5, F 6, G 7, H 8, I 9, J 10, K 11, L 12, M 13.
- N 14, O 15, P 16, Q 17, R 18, S 19, T 20, U 21, V 22, W 23, X 24, Y 25, Z 26.
- EJOTY :: E is 5, J is 10, O is 15, T is 20, Y is 25. Five anchors beat twenty-six memorised numbers.
- Opposite letters :: A-Z, B-Y, C-X, and in general two letters whose positions sum to 27.
- Reverse alphabet :: A is 26 and Z is 1. The reverse position = 27 minus the forward position.

## The types
- Letter shift :: each letter moved by a fixed number of places, forward or backward. CAT to DBU is plus one.
- Reversal :: the word written backwards, or each letter replaced by its opposite.
- Position arithmetic :: the code number is the sum, product or difference of the letter positions.
- Substitution :: a fixed table maps each letter to a symbol or another letter; read two examples together.
- Conditional :: the rule changes with the position of the letter in the word, for example odd places shifted by one and even by two.
- Word to word :: two coded words share letters, and the overlap gives the mapping.

## The method
- Write the word, write the code beneath it, and write the positions of both rows.
- Compare positions column by column and state the move in words: "plus one", "minus three", "opposite".
- Test the rule on a third letter before applying it to the question word.
""",
    right="""
## Worked example
- If CAT is coded as DBU, how is DOG coded?
= C to D is plus one, A to B is plus one, T to U is plus one
= D to E, O to P, G to H
= DOG is coded EPH

## Second worked example
- If each letter is replaced by the letter opposite it in the alphabet, how is CAT coded?
= C is 3, so its opposite is 27 - 3 = 24, which is X
= A becomes Z; T is 20 and becomes 7, which is G
= CAT is coded XZG

## Third worked example
- If A is 1, B is 2 and so on, and the code of a word is the sum of its letter positions, what is the code of CAB?
= C is 3, A is 1, B is 2
= Sum = 6

## Shortcuts
- Learn the five anchors and count from the nearest one; nobody counts from A to T.
- Opposite letters always sum to 27, so the opposite of 17 is 10, which is J.
- When the code is a number, check whether it is a sum or a product; products explode quickly, sums grow slowly.
- In substitution questions, find a letter that appears in both coded words and fix its meaning first.

## Traps
* Shifting the wrong way, forward when the example moved backward.
* Forgetting that Z plus one wraps to A.
* Mixing the forward position with the reverse position inside one question.
* Assuming the rule for the first letter applies to all of them when the question is conditional.
""",
)

# 16 ------------------------------------------------------------------------
add(key="alphabet", tag="Alphabet test", kicker="", title="Alphabet test",
    sub="Counting from the left, from the right, and the middle of a word",
    left="""
## The formulas
= Position from the left is the position; position from the right = 27 - position
= A letter that is p-th from the left is (27 - p) from the right
= The number of letters between two positions = the difference of the positions minus one
= In a word, the middle letter is at the position (length + 1)/2 when the length is odd
= Alphabetical order :: compare the first letters, then the second, and so on
= Letter pairs in a word :: a pair is in alphabetical order if the first letter comes before the second

## The types
- Position questions :: find the letter at a place from the left or the right.
- Left of and right of :: combine two moves, as in "fourth to the left of the tenth from the right".
- Word formation :: which of these words cannot be made from the letters of the given word.
- Alphabet series :: a run with gaps, or alternate letters.
- Dictionary order :: arrange given words as they would appear in a dictionary.
- Letter pairs :: count the pairs in a word that have as many letters between them as in the alphabet.

## The method
- Convert every "from the right" into "from the left" at once: 27 minus the number.
- Then move left by subtracting and right by adding.
- For dictionary order, do not read the whole word; compare until the words differ.
""",
    right="""
## Worked example
- Which letter is fourth to the left of the tenth letter from the right of the alphabet?
= Tenth from the right = 27 - 10 = 17, which is Q
= Four to the left of Q = 17 - 4 = 13, which is M
= The answer is M

## Second worked example
- How many letters are there between the letter that is seventh from the left and the letter that is fourth from the right?
= Seventh from the left is G, fourth from the right is 27 - 4 = 23, which is W
= Between them = 23 - 7 - 1 = 15 letters

## Third worked example
- In the word EDUCATION, which letter is exactly in the middle?
= Nine letters, so the middle is the fifth
= E D U C A T I O N gives A

## Shortcuts
- 27 minus the position turns any right-hand count into a left-hand one; do it in your head in a second.
- For "middle of the word", count the letters first; if the count is even there is no single middle letter, and the question will not ask.
- In word-formation questions, count the letters of the source word against the target; a letter used twice in the target needs two in the source.
- In series questions, write the positions under the letters; the pattern is usually in the positions, not in the shapes.

## Traps
* Counting the letter itself as "between" the two positions.
* Forgetting to add one when the question asks for the number of letters including the ends.
* Reversing left and right when the question says "to the left of the letter that is fourth from the right".
* Treating a repeated letter as available twice when the source word has it once.
""",
)

# 17 ------------------------------------------------------------------------
add(key="ranking", tag="Ranking", kicker="", title="Ranking and position",
    sub="One row, two counts from the two ends, and a formula that never fails",
    left="""
## The formulas
= Total in the row = position from the left + position from the right - 1
= Position from the right = total - position from the left + 1
= Number of people between two persons = total - (left position of the first + right position of the second)
= If two people interchange places, the change in one rank gives the number between them
= In a class, rank from the top and rank from the bottom behave exactly like left and right in a row
= If the ranks of the same person from both ends are given, the total follows from the first formula

## The types
- One person, both ranks :: find the total.
- Two persons, one rank each :: find how many are between them.
- Interchange :: after swapping, the new rank of one is given; find the total.
- Percentage rank :: "he is 40th from the top in a class of 100", convert to the rank from the bottom.
- Ordering :: arrange by height, marks or age and answer a position question.

## The method
- Draw the row as a line, mark the two positions, and shadow the unknown stretch.
- Put the formula down before the arithmetic; the errors in this topic are almost all subtraction slips.
- For interchange questions, the person who moves from rank a to rank b has (b - a) people between the old and new places.
""",
    right="""
## Worked example
- In a class of 50 students, A is 18th from the top. What is his rank from the bottom?
= Rank from the bottom = 50 - 18 + 1 = 33
- Check :: 17 students above him and 32 below him, and 17 + 1 + 32 = 50.

## Second worked example
- In a row of 40, A is 12th from the left and B is 15th from the right. How many people are between them?
= People between = 40 - (12 + 15) = 13
- Check :: A at 12, B at 40 - 15 + 1 = 26, and 26 - 12 - 1 = 13.

## Third worked example
- In a row, A is 9th from the left and 14th from the right. How many are in the row?
= Total = 9 + 14 - 1 = 22

## Shortcuts
- Do the "minus one" immediately; the plus and minus are where marks are lost.
- If the two positions overlap (their sum is more than the total), the question is about people counted twice; subtract the overlap.
- For a class rank, the same formula works with top and bottom.
- When the answer choices are consecutive numbers, recheck the arithmetic rather than the logic.

## Traps
* Forgetting the minus one when the same person is counted from both ends.
* Using the total as the answer when the question asked for the rank.
* Mixing up left and right when the row is described from one side only.
* Assuming the total is known when the question gives only two ranks of different people.
""",
)

# 18 ------------------------------------------------------------------------
add(key="blood", tag="Blood relations", kicker="", title="Blood relations",
    sub="Draw the tree, mark the sexes, and never guess a gender",
    left="""
## The vocabulary
- Father's or mother's brother :: uncle. Their children :: cousins. Father's or mother's sister :: aunt.
- Brother's or sister's son :: nephew. Their daughter :: niece. Husband's or wife's brother :: brother-in-law.
- Father's father :: grandfather. Mother's mother :: grandmother. Son's son :: grandson.
- Wife of the son :: daughter-in-law. Husband of the daughter :: son-in-law.
- Maternal :: on the mother's side (maternal uncle is the mother's brother). Paternal :: on the father's side.
- A "only son" or "only daughter" in the question is a clue that removes every sibling from the tree.

## The types
- Pointing to a photograph :: a sentence about "my father's only son" and so on.
- Coded relations :: symbols such as A + B, A - B, A x B with a key for each.
- Family tree from statements :: several sentences, and a question about one person.
- Gender and generation :: "how is X related to Y", where the answer is a relationship word.

## The method
- Draw a tree: generations as rows, marriages as horizontal lines, siblings as a bracket.
- Put a small M or F beside every person as soon as the sex is known.
- Read the sentence backwards from the person named last to the person named first.
- If two relationships are possible, the question is testing the missing clue; look for "only", "eldest" or "wife of".
""",
    right="""
## Worked example
- Pointing to a photograph, a man says, "She is the daughter of my grandfather's only son." How is she related to him?
= Grandfather's only son = the speaker's father
= The daughter of his father = his sister
= The answer is sister

## Second worked example
- A is the father of B. B is the sister of C. C is the son of D. How is A related to D?
= A and D are the parents of B and C
= A is the husband of D, or D is the wife of A
= If the question asks for A's relation to D, the answer is husband

## Third worked example
- P is the brother of Q. Q is the mother of R. R is the sister of S. How is P related to S?
= Q is the mother of R and of S, so R and S are siblings
= P is the brother of Q, so P is S's maternal uncle
= The answer is maternal uncle

## Shortcuts
- Draw before you read the choices; the choices are designed to confuse the undecided.
- Sexes are the whole difficulty: a "sister of" tells you the sex, a "child of" tells you nothing.
- In coded questions, translate each symbol into a word first, then build the tree.
- Check the generation gap: a grandparent is two rows away, an uncle one row up and one across.

## Traps
* Assuming a child is a son.
* Treating a cousin as a sibling.
* Reading "my father's son" as the speaker himself when he has a brother.
* Ignoring "only" in "my grandfather's only son".
""",
)

# 19 ------------------------------------------------------------------------
add(key="direction", tag="Direction sense", kicker="", title="Direction sense",
    sub="Walk the route on paper, then close the triangle with Pythagoras",
    left="""
## The frame
- Four cardinal directions :: north, east, south, west. Four diagonals :: north-east, north-west, south-east, south-west.
- A right turn from north is east; a right turn from east is south; from south, west; from west, north.
- A left turn is the mirror: from north it is west, and so on round the compass.
- Clockwise :: N, E, S, W. Anti-clockwise :: N, W, S, E.
- Displacement :: the straight line from the start to the finish, found by Pythagoras when the two legs are at right angles.
- Distance = the square root of (the east-west distance squared + the north-south distance squared).
- The direction of the finish from the start follows the signs: east positive, west negative, north positive, south negative.

## The types
- Final direction :: follow the turns and name the direction faced.
- Distance from the start :: two legs at right angles, then Pythagoras.
- Shadow questions :: the sun rises in the east, so a shadow in the morning falls to the west, and in the evening to the east.
- Clock-face directions :: 3 o'clock is east, 9 o'clock is west, 12 is north, 6 is south.
- Two people starting from one point :: draw both routes and compare the endpoints.
""",
    right="""
## Worked example
- A man walks 9 km north, turns right and walks 12 km. How far is he from his starting point?
= North 9, then east 12; the legs are at right angles
= Distance = the square root of (9 squared + 12 squared) = the square root of (81 + 144) = the square root of 225 = 15 km
= He is 15 km north-east of the start

## Second worked example
- A man walks 5 km east, turns left and walks 3 km, turns left again and walks 5 km. Where is he?
= East 5, north 3, then west 5
= The two east-west legs cancel and he is 3 km north of the start

## Third worked example
- At sunrise a man faces a pole and his shadow falls to his right. Which direction is he facing?
= In the morning the shadow falls to the west
= If west is on his right, he faces south

## Shortcuts
- Draw the route on the answer sheet, one centimetre to a kilometre. It takes ten seconds and removes the whole class of error.
- Opposite legs cancel; only the difference matters for distance.
- For shadow questions, remember the sun: east in the morning, west in the evening, and the shadow is always opposite the sun.
- 3-4-5, 5-12-13, 8-15-17 and 9-12-15 are the triangles the paper prefers.

## Traps
* Turning right from south and walking east instead of west.
* Adding the legs instead of using Pythagoras.
* Naming the distance when the question asked for the direction.
* Forgetting that the shadow falls opposite the sun, not towards it.
""",
)

# 20 ------------------------------------------------------------------------
add(key="clock", tag="Clock", kicker="", title="Clock",
    sub="Two hands, five and a half degrees a minute, and a formula for the angle",
    left="""
## The formulas
= The minute hand moves 6 degrees a minute; the hour hand moves 0.5 degrees a minute
= Their relative speed = 5.5 degrees a minute
= Angle between the hands at H hours and M minutes = the modulus of (30H - 5.5M), taken as the smaller angle, 360 minus it if it exceeds 180
= The hands coincide every 65 and 5/11 minutes; there are 11 coincidences in 12 hours and 22 in a day
= Right angles :: 44 in a day, 22 in twelve hours
= Opposite directions :: 22 in a day, 11 in twelve hours
= At H o'clock the hour hand is at 30H degrees, which is the head start the minute hand must cover
= Time to coincide after H o'clock = (30H) / 5.5 minutes = 60H/11 minutes
= Mirror image :: the mirror time of a 12-hour clock reading is 11:60 minus the time

## The types
- Angle at a given time :: the formula, and take the smaller angle.
- When do the hands coincide :: the head-start division.
- When are they opposite or at right angles :: the same division with 180 or 90 added to the head start.
- Faulty clocks :: a clock that gains or loses a fixed number of minutes a day.
- Mirror image :: the reading in a mirror.
""",
    right="""
## Worked example
- Find the angle between the hands of a clock at 3:30.
= 30H = 90 and 5.5M = 165
= The modulus of (90 - 165) is 75 degrees, which is less than 180
= The angle is 75 degrees

## Second worked example
- At what time between 4 and 5 o'clock do the hands coincide?
= At 4 o'clock the hour hand is at 120 degrees
= Time = 120 / 5.5 = 240/11 minutes = 21 and 9/11 minutes
= The hands coincide at 4:21 and 9/11 minutes, that is about 4:21:49

## Third worked example
- What is the mirror image of 3:30?
= Mirror time = 11:60 - 3:30 = 8:30
= The answer is 8:30

## Shortcuts
- 30H - 5.5M, then take the smaller angle. One line, every time.
- For a head start, divide by 5.5: the hands meet after 60H/11 minutes past H.
- For right angles, the minute hand must close the head start and then be 90 degrees ahead or behind; two answers, usually.
- In faulty-clock questions, compare the clock's time with the true time over the same interval, then scale.

## Traps
* Forgetting to take the smaller angle; 300 degrees is really 60.
* Using 6 degrees a minute for the hour hand.
* Dividing by 6 instead of 5.5 when finding a meeting time.
* Treating the mirror image as 12:00 minus the time; it is 11:60 minus the time.
""",
)

# 21 ------------------------------------------------------------------------
add(key="calendar", tag="Calendar", kicker="", title="Calendar",
    sub="Odd days, century codes, and the one date that anchors the year",
    left="""
## The formulas
= An ordinary year has 365 days, that is 52 weeks and 1 odd day. A leap year has 2 odd days
= A century of 100 years has 5 odd days; 200 years has 3; 300 years has 1; 400 years has 0
= Leap year :: divisible by 4, and a century year must be divisible by 400. 1900 is not a leap year; 2000 is
= To find the day of a date :: total odd days = odd days of the completed years + odd days of the months before the date + the date itself
= Day codes for the months of an ordinary year, from January :: 3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3 | January is 31 days, so 3 odd days
= Month codes for a leap year :: January 3, February 1, and the rest as above
= The days run :: Sunday 0, Monday 1, Tuesday 2, Wednesday 3, Thursday 4, Friday 5, Saturday 6

## The types
- The day of a given date :: the standard odd-days calculation.
- The day on which a year begins :: one odd day after the previous year, two after a leap year.
- Calendar repetition :: a calendar repeats when the total odd days over the gap is a multiple of 7.
- Odd days between two dates :: count the years and the days.
- Leap-year counting :: how many leap years in a range.
""",
    right="""
## Worked example
- What day of the week is 15 August 2026, given that 1 January 2026 is a Thursday?
= Days from 1 January to 15 August :: 31 + 28 + 31 + 30 + 31 + 30 + 31 + 15 = 227, and the day number is 227
= Odd days after 1 January = (227 - 1) mod 7 = 226 mod 7 = 2
= Thursday plus 2 = Saturday
= 15 August 2026 is a Saturday

## Second worked example
- Which years between 2000 and 2010 are leap years?
= Divisible by 4 :: 2000, 2004, 2008
= 2000 is a century year and divisible by 400, so it counts
= The leap years are 2000, 2004 and 2008

## Third worked example
- If 1 January 2025 is a Wednesday, what is 1 January 2026?
= 2025 is an ordinary year, so it adds one odd day
= Wednesday plus one = Thursday

## Shortcuts
- Learn one anchor date for the current year and count from it; the whole topic collapses into one subtraction.
- An ordinary year shifts the next year's first day by one, a leap year by two.
- Century codes are 5, 3, 1, 0 for 100, 200, 300, 400 years; they cycle.
- When two calendars repeat, the gap is 6, 11 or 28 years, and 28 always works for an ordinary stretch.

## Traps
* Treating 1900 as a leap year; it is not, because it is not divisible by 400.
* Forgetting February's extra day when the date is after February in a leap year.
* Counting the starting day twice when measuring a gap.
* Using month codes for a leap year from March onwards, when they are the same as an ordinary year after February.
""",
)

# 22 ------------------------------------------------------------------------
add(key="analogy", tag="Analogy", kicker="", title="Analogy",
    sub="Say the relation in a sentence, then make the second pair say the same thing",
    left="""
## The relations that are used
- Synonym :: big : large. Antonym :: hot : cold.
- Part and whole :: wheel : car. Whole and part :: tree : branch.
- Cause and effect :: rain : flood. Effect and cause :: death : poison.
- Worker and workplace :: doctor : hospital. Worker and tool :: carpenter : saw.
- Worker and product :: farmer : crop. Animal and young :: cow : calf. Animal and sound :: dog : bark.
- Category and member :: fruit : mango. Member and category :: rose : flower.
- Degree :: warm : hot. Function :: knife : cut.
- Number analogy :: 4 : 16, a square relation; 3 : 9 : : 5 : 25.
- Letter analogy :: ACE : BDF, each letter one ahead; GIK : HJL.
- Word and its unit :: distance : kilometre.

## The method
- Write the first pair as a sentence: "a wheel is part of a car".
- Apply the same sentence to the third word: "a branch is part of a tree".
- Keep the order. If the first pair goes from part to whole, the answer must also go from part to whole.
- Reject any option that fits a different relation, even if the words seem related.
""",
    right="""
## Worked example
- Doctor : Hospital : : Teacher : ?
= The relation is worker to workplace
= The teacher's workplace is a school
= The answer is school

## Second worked example
- 4 : 16 : : 7 : ?
= The relation is the square
= 7 squared is 49
= The answer is 49

## Third worked example
- ACE : BDF : : GIK : ?
= Each letter moves one place forward
= G to H, I to J, K to L
= The answer is HJL

## Fourth worked example
- Cow : Calf : : Horse : ?
= The relation is animal to its young
= The young of a horse is a foal or a colt
= The answer is foal

## Shortcuts
- Name the relation before you look at the options; otherwise the options choose the relation for you.
- If two options fit, the question has a second relation in it; look for the order, the sex or the degree.
- For number analogies, test square, cube, prime, multiple and digit sum, in that order.
- For letter analogies, write the positions under the letters and compare the two rows.

## Traps
* Reversing the order of the relation.
* Accepting a merely associated word, such as "hospital" for "nurse" when the relation is worker to workplace.
* Missing the difference between animal and young and animal and sound.
* For number analogies, using a rule that fits only one side.
""",
)

# 23 ------------------------------------------------------------------------
add(key="oddone", tag="Odd one out", kicker="", title="Odd one out",
    sub="Find the property the majority shares, and the one that breaks it",
    left="""
## The properties to test, in order
- Perfect squares and cubes :: 121, 144, 169 are squares; 125, 216, 343 are cubes.
- Primes :: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.
- Multiples and divisibility :: by 3 (digit sum), by 4 (last two digits), by 9 (digit sum), by 11 (alternating sum).
- Parity :: odd and even. 1 is neither prime nor composite.
- Digit properties :: the sum of digits, the product, the number of digits.
- Letter series :: vowels and consonants, or positions in a fixed pattern.
- Word classes :: all fruits but one, all capital cities but one, all metals but one.
- Spelling :: one word with a doubled letter, one with a silent letter.

## The method
- Test the simplest property first, which is usually the square or the prime.
- State the shared property in words before choosing; "all but one are squares" is an answer, "this one looks different" is not.
- If two options break different properties, the question is testing the property that three of the four share.
- For word questions, look for the category before the spelling.
""",
    right="""
## Worked example
- Which is the odd one out: 121, 144, 169, 180?
= 121 is 11 squared, 144 is 12 squared, 169 is 13 squared
= 180 is not a perfect square
= The answer is 180

## Second worked example
- Which is the odd one out: 17, 19, 23, 27?
= 17, 19 and 23 are prime
= 27 is 3 cubed and is divisible by 3 and 9
= The answer is 27

## Third worked example
- Which is the odd one out: apple, mango, banana, potato?
= Apple, mango and banana are fruits
= Potato is a vegetable, and botanically a tuber
= The answer is potato

## Shortcuts
- Squares up to 30 squared and cubes up to 12 cubed cover almost every number question in this topic.
- Test divisibility by 3 with the digit sum; 27 gives 9, so it is a multiple of 3.
- In letter series, write the positions; the odd one usually breaks the gap pattern by one.
- In word lists, name the category of three of them out loud before you choose.

## Traps
* Reading "which is different" as "which is rare"; the odd one breaks a stated property, not a hunch.
* Forgetting that 2 is prime and 1 is not.
* Missing that 91 is not prime, since it is 7 times 13.
* Choosing a word for its meaning when the list is testing spelling.
""",
)
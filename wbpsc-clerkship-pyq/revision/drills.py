# -*- coding: utf-8 -*-
"""Three drills per arithmetic sheet.  Numeric answers are computed here."""


def n(x):
    if abs(x - round(x)) < 1e-9:
        return f"{int(round(x))}"
    return f"{x:.4f}".rstrip("0").rstrip(".")


D = {
"percentage": [
    ("15 per cent of 240?", n(0.15 * 240)),
    ("45 is what per cent of 300?", n(45 / 300 * 100) + " per cent"),
    ("A price rises 25 per cent, then falls 20 per cent. Net change?", "no change"),
],
"profit": [
    ("CP 480, SP 552. Profit per cent?", n((552 - 480) / 480 * 100) + " per cent"),
    ("SP 720 at a loss of 10 per cent. CP?", "Rs " + n(720 / 0.9)),
    ("CP 250, profit 20 per cent. SP?", "Rs " + n(250 * 1.2)),
],
"discount": [
    ("MP 800, discount 20 per cent. SP?", "Rs " + n(800 * 0.8)),
    ("Successive discounts of 25 and 20 per cent?", n(25 + 20 - 25 * 20 / 100) + " per cent"),
    ("MP 1,200, SP 1,026. Discount per cent?", n((1200 - 1026) / 1200 * 100) + " per cent"),
],
"si": [
    ("SI on Rs 1,500 at 8 per cent for 4 years?", "Rs " + n(1500 * 8 * 4 / 100)),
    ("A sum doubles at simple interest at what rate in 8 years?", n(100 / 8) + " per cent"),
    ("SI on Rs 2,500 at 4 per cent is Rs 300. For how many years?", n(300 * 100 / (2500 * 4)) + " years"),
],
"ci": [
    ("CI on Rs 2,000 at 5 per cent for 2 years?", "Rs " + n(2000 * 1.05 ** 2 - 2000)),
    ("CI minus SI on Rs 1,000 at 20 per cent for 2 years?", "Rs " + n(1000 * (0.2) ** 2)),
    ("Amount on Rs 4,000 at 10 per cent for 1 year, half-yearly?", "Rs " + n(4000 * 1.05 ** 2)),
],
"ratio": [
    ("Divide 120 in the ratio 2 : 3.", "48 and 72"),
    ("3 : 5 = 24 : ?", "40"),
    ("Mean proportional between 9 and 16?", "12"),
],
"average": [
    ("Average of 12, 18 and 24?", "18"),
    ("Five numbers average 20. One is removed and the average falls to 18. The removed number?", "28"),
    ("Average speed going at 40 and returning at 60 over equal distances?", n(2 * 40 * 60 / 100) + " km per hour"),
],
"work": [
    ("A in 10 days, B in 15. Together?", n(10 * 15 / 25) + " days"),
    ("A and B in 8 days, A alone in 12. B alone?", n(1 / (1 / 8 - 1 / 12)) + " days"),
    ("6 men take 12 days. How long for 9 men?", n(6 * 12 / 9) + " days"),
],
"tsd": [
    ("150 km in 2 hours 30 minutes. Speed?", "60 km per hour"),
    ("90 km per hour in metre per second?", "25"),
    ("5 km at 4 km per hour and back at 6. Average speed?", n(2 * 4 * 6 / 10) + " km per hour"),
],
"trains": [
    ("A 200 m train at 72 km per hour passes a pole in?", n(200 / (72 * 5 / 18)) + " seconds"),
    ("150 m and 250 m trains cross at 30 and 50 km per hour, opposite ways?", n(400 / (80 * 5 / 18)) + " seconds"),
    ("A 150 m train at 45 km per hour crosses a 300 m platform in?", n(450 / (45 * 5 / 18)) + " seconds"),
],
"boats": [
    ("Boat 10 km per hour, stream 3. Downstream and upstream?", "13 and 7 km per hour"),
    ("24 km downstream in 3 hours, stream 2 km per hour. Boat in still water?", "6 km per hour"),
    ("12 km upstream in 4 hours, boat 5 km per hour. Stream?", "2 km per hour"),
],
"mixture": [
    ("Mix Rs 30 and Rs 45 teas to sell at Rs 36. Ratio?", "3 : 2"),
    ("20 litres of milk, 4 drawn and replaced once. Milk left?", n(20 * 0.8) + " litres"),
    ("Equal quantities at Rs 40 and Rs 50. Mean price?", "Rs 45"),
],
"ages": [
    ("A is twice B and their ages add to 36.", "A 24, B 12"),
    ("A father is four times his son; in 6 years he will be three times.", "Father 48, son 12"),
    ("Five years ago a man was 30. How old is he now?", "35"),
],
"series": [
    ("3, 7, 11, 15, ?", "19"),
    ("2, 6, 18, 54, ?", "162"),
    ("1, 4, 9, 16, ?", "25"),
],
"coding": [
    ("If every letter moves two places forward, how is CAT written?", "ECV"),
    ("CAT with every letter replaced by its opposite?", "XZG"),
    ("If A is 1 and so on, what is the sum for BAD?", "7"),
],
"alphabet": [
    ("Which letter is fifth from the right?", "V"),
    ("Which letter is third to the left of the fifteenth from the left?", "L"),
    ("How many letters lie between C and G?", "3"),
],
"ranking": [
    ("A is 25th from the top in a class of 60. Rank from the bottom?", "36"),
    ("In a row of 30, A is 8th from the left and B 6th from the right. Between them?", "16"),
    ("A is 7th from the left and 9th from the right. How many in the row?", "15"),
],
"blood": [
    ("How is your mother's brother related to you?", "Maternal uncle"),
    ("How is your father's sister's son related to you?", "Cousin"),
    ("How is your son's wife related to you?", "Daughter-in-law"),
],
"direction": [
    ("6 km north, then 8 km east. Distance from the start?", "10 km, to the north-east"),
    ("4 km east, 3 km north, 4 km west. Where are you?", "3 km north of the start"),
    ("At sunset a man's shadow falls to his left. Which way is he facing?", "North"),
],
"clock": [
    ("Angle between the hands at 6 o'clock?", "180 degrees"),
    ("Angle between the hands at 9 o'clock?", "90 degrees"),
    ("When do the hands coincide after 2 o'clock?", "After 120/11 minutes, about 2:10:54"),
],
"calendar": [
    ("Odd days in a leap year?", "2"),
    ("Odd days in 200 years?", "3"),
    ("If 1 January 2026 is a Thursday, what is 1 January 2027?", "Friday"),
],
"analogy": [
    ("Doctor : Hospital : : Teacher : ?", "School"),
    ("5 : 25 : : 8 : ?", "64"),
    ("Pen : Write : : Knife : ?", "Cut"),
],
"oddone": [
    ("121, 144, 169, 180 - the odd one?", "180, not a perfect square"),
    ("17, 19, 23, 27 - the odd one?", "27, not prime"),
    ("Apple, mango, banana, potato - the odd one?", "Potato, a vegetable"),
],
}

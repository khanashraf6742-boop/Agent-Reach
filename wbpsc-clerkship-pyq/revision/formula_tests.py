# -*- coding: utf-8 -*-
"""Independent re-derivation of every formula printed on the sheets.

Each entry computes the quantity from the formula as printed and compares it
with the textbook answer, or with Python's own datetime where the subject is
the calendar.  The build refuses to run if any identity fails.
"""
import datetime

TESTS = []


def t(topic, what, got, want, tol=1e-9):
    TESTS.append((topic, what, got, want, tol))


# percentages -----------------------------------------------------------------
t("Percentage", "successive +20 then -20", 20 + (-20) + 20 * -20 / 100, -4)
t("Percentage", "successive +10 then +10", 10 + 10 + 100 / 100, 21)
t("Percentage", "price +25%, consumption cut", 100 * 25 / (100 + 25), 20)
t("Percentage", "price -20%, consumption may rise", 100 * 20 / (100 - 20), 25)
t("Percentage", "A 25% more than B means B is", 100 * 25 / (100 + 25), 20)

# profit and loss -------------------------------------------------------------
t("Profit and loss", "profit % on 900 to 945", (945 - 900) / 900 * 100, 5)
t("Profit and loss", "CP from SP 720 at 10% loss", 720 * 100 / 90, 800)
t("Profit and loss", "same SP, +x and -x loses x^2/100", 20 ** 2 / 100, 4)
t("Profit and loss", "false weight 900 g sold as 1 kg", (1000 - 900) / 900 * 100, 100 / 9)

# discount --------------------------------------------------------------------
t("Discount", "successive 15 and 20", 15 + 20 - 15 * 20 / 100, 32)
t("Discount", "successive 10 and 5", 10 + 5 - 10 * 5 / 100, 14.5)
t("Discount", "1200 less 10% less 5%", 1200 * 0.9 * 0.95, 1026)
t("Discount", "20% mark-up then 20% discount is a loss of", 100 - 120 * 0.8, 4)

# simple and compound interest ------------------------------------------------
t("Simple interest", "SI on 1200 at 6% for 2 years", 1200 * 6 * 2 / 100, 144)
t("Simple interest", "doubling time at 8%", 100 / 8, 12.5)
t("Simple interest", "amount 1344 in 2y, 1416 in 3y, principal", 1344 - (1416 - 1344) * 2, 1200)
t("Compound interest", "CI on 1000 at 10% for 2 years", 1000 * 1.1 ** 2 - 1000, 210)
t("Compound interest", "CI - SI for 2 years", (1000 * 1.1 ** 2 - 1000) - (1000 * 10 * 2 / 100), 10)
t("Compound interest", "P(R/100)^2", 1000 * (10 / 100) ** 2, 10)
t("Compound interest", "CI - SI for 3 years", (1000 * 1.1 ** 3 - 1000) - 300, 31)
t("Compound interest", "P(R/100)^2(3+R/100)", 1000 * 0.01 * 3.1, 31)
t("Compound interest", "8000 at 10% half-yearly for 1 year", 8000 * 1.05 ** 2, 8820)

# ratio -----------------------------------------------------------------------
t("Ratio", "combine 2:3 and 4:5 to 8:12:15", (2 * 4, 3 * 4, 3 * 5), (8, 12, 15))
t("Ratio", "fourth proportional to 2,3,4", 3 * 4 / 2, 6)
t("Ratio", "mean proportional of 4 and 9", (4 * 9) ** 0.5, 6)
t("Ratio", "third proportional to 4 and 6", 6 ** 2 / 4, 9)
t("Ratio", "partnership 5000x6 : 8000x12", (5000 * 6, 8000 * 12), (30000, 96000))
t("Ratio", "divide 96 in 3:5", (96 * 3 / 8, 96 * 5 / 8), (36, 60))

# average ---------------------------------------------------------------------
t("Average", "average speed 30 and 20 over equal distance", 2 * 30 * 20 / (30 + 20), 24)
t("Average", "teacher joins 20 at 15 to make 15.5", 21 * 15.5 - 20 * 15, 25.5)
t("Average", "first n naturals, n=10", (10 + 1) / 2, 5.5)
t("Average", "replacement changes average by (new-old)/n", (40 - 25) / 5, 3)

# time and work ---------------------------------------------------------------
t("Time and work", "12 and 18 days together", 12 * 18 / (12 + 18), 7.2)
t("Time and work", "A+B 6 days, A 10, then B", 1 / (1 / 6 - 1 / 10), 15)
t("Time and work", "3 workers 6, 8, 12 days", 1 / (1 / 6 + 1 / 8 + 1 / 12), 8 / 3)

# time and distance, trains, boats --------------------------------------------
t("Time and distance", "240 km in 4 h in m/s", 240 / 4 * 5 / 18, 50 / 3)
t("Time and distance", "late 10 min at 5, early 5 min at 6", 5 * 6 * (1 / 6 + 1 / 12) / (6 - 5), 7.5)
t("Trains", "120 m train, 180 m platform, 20 s", (120 + 180) / 20, 15)
t("Trains", "150 + 250 m at 90 km/h opposite", 400 / (90 * 5 / 18), 16)
t("Boats and streams", "20 km downstream in 2 h, stream 2", 20 / 2 - 2, 8)
t("Boats and streams", "round trip 12 km at b=8, s=2", 12 / 10 + 12 / 6, 3.2)
t("Boats and streams", "b from down and up", (10 + 6) / 2, 8)

# mixture ---------------------------------------------------------------------
t("Mixture", "40 and 55 to mean 46", (55 - 46, 46 - 40), (9, 6))
t("Mixture", "replacement 40 L, 8 L, twice", 40 * (1 - 8 / 40) ** 2, 25.6)

# ages ------------------------------------------------------------------------
t("Problems on ages", "f=3s, +10 years f=2s, son", (2 * 10 - 10) / (3 - 2), 10)
_x = 4 * (5 - 3) / (5 * 5 - 7 * 3)          # x = t(d-c)/(ad-bc) for (5x-4)/(7x-4) = 3/5
t("Problems on ages", "5:7 now, 3:5 four years ago, A", 5 * _x, 10)
t("Problems on ages", "5:7 now, 3:5 four years ago, B", 7 * _x, 14)

# series ----------------------------------------------------------------------
t("Number series", "8,15,22,29,36 next", 36 + 7, 43)
t("Number series", "n(n+1) at n=6", 6 * 7, 42)
t("Number series", "sum of AP 1..10", 10 / 2 * (2 * 1 + 9 * 1), 55)

# coding, alphabet, ranking ---------------------------------------------------
t("Coding and decoding", "CAT +1", "".join(chr(ord(c) + 1) for c in "CAT"), "DBU")
t("Coding and decoding", "opposite of CAT", "".join(chr(155 - ord(c)) for c in "CAT"), "XZG")
t("Coding and decoding", "CAB position sum", 3 + 1 + 2, 6)
t("Alphabet test", "10th from right is position", 27 - 10, 17)
t("Alphabet test", "four left of Q", 17 - 4, 13)
t("Alphabet test", "between 7th from left and 4th from right", (27 - 4) - 7 - 1, 15)
t("Ranking", "18th of 50 from the bottom", 50 - 18 + 1, 33)
t("Ranking", "between 12th from left and 15th from right, row 40", 40 - 12 - 15, 13)
t("Ranking", "9 + 14 - 1", 9 + 14 - 1, 22)

# direction -------------------------------------------------------------------
t("Direction sense", "9 north then 12 east", (9 ** 2 + 12 ** 2) ** 0.5, 15)
t("Direction sense", "5 east, 3 north, 5 west", abs(5 - 5) + 3, 3)

# clock -----------------------------------------------------------------------
t("Clock", "angle at 3:30", abs(30 * 3 - 5.5 * 30), 75)
t("Clock", "coincidence after 4 o'clock, minutes", 30 * 4 / 5.5, 240 / 11)
t("Clock", "mirror of 3:30", (11 * 60 + 60) - (3 * 60 + 30), 510)

# calendar, checked against Python's own calendar -----------------------------
d = datetime.date(2026, 8, 15)
t("Calendar", "15 Aug 2026 weekday (Mon=0)", d.weekday(), 5)     # Saturday
t("Calendar", "1 Jan 2026 weekday", datetime.date(2026, 1, 1).weekday(), 3)   # Thursday
t("Calendar", "1 Jan 2025 weekday", datetime.date(2025, 1, 1).weekday(), 2)   # Wednesday
t("Calendar", "day of year for 15 Aug 2026", d.timetuple().tm_yday, 227)
t("Calendar", "odd days from 1 Jan to 15 Aug 2026",
  (d.timetuple().tm_yday - 1) % 7, 2)
t("Calendar", "leap years 2000 to 2010",
  [y for y in range(2000, 2011) if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0],
  [2000, 2004, 2008])
t("Calendar", "1900 is not a leap year", (1900 % 4 == 0 and 1900 % 100 != 0) or 1900 % 400 == 0, False)

# analogy and odd one out ------------------------------------------------------
t("Analogy", "7 squared", 7 ** 2, 49)
t("Odd one out", "180 is a perfect square", int(180 ** 0.5) ** 2 == 180, False)
t("Odd one out", "27 is prime", all(27 % p for p in range(2, 6)), False)
t("Odd one out", "91 is divisible by 7", 91 % 7, 0)


def run():
    bad = []
    for topic, what, got, want, tol in TESTS:
        if isinstance(want, (int, float)) and isinstance(got, (int, float)):
            ok = abs(got - want) <= tol * max(1, abs(want))
        else:
            ok = got == want
        if not ok:
            bad.append((topic, what, got, want))
    return len(TESTS), bad


if __name__ == "__main__":
    total, bad = run()
    for row in bad:
        print("  FAIL", row)
    print(f"{total} formula identities, {len(bad)} failure(s)")

# -*- coding: utf-8 -*-
"""Arithmetic and reasoning generator.

Every item is produced from parameters and a formula, and keeps its `spec` so that the
validator can recompute the answer by a different route (forward substitution into the
defining equation) instead of trusting the text.

Distractors are perturbations of the true value, never the true value itself, and are
de-duplicated. Answers are exact: all arithmetic is done in integers or Fractions.
"""
import random
from fractions import Fraction

MONEY = "Rs "


def _num(x):
    if isinstance(x, Fraction):
        if x.denominator == 1:
            return str(x.numerator)
        return f"{float(x):.2f}"
    return str(x)


def _d(prefix, candidates):
    out = []
    for c in candidates:
        if c is None or c <= 0:
            continue
        t = prefix + _num(c)
        if t not in out:
            out.append(t)
    while len(out) < 3:
        out.append(prefix + str(97 + len(out)))
    return out[:3]


def _rupees(cands):
    return [MONEY + _num(c) for c in cands]


def pct_of(rng):
    p = rng.randrange(5, 91, 5)
    n = rng.randrange(120, 981, 20)
    ans = Fraction(p * n, 100)
    q = f"What is {p}% of {n}?"
    e = (f"{p}% of {n} = ({p}/100) x {n} = {_num(ans)}. "
         f"Short cut: 10% of {n} is {n // 10}, so {p}% is {p // 10} times that.")
    dl = _d("", [ans + p, ans - n // 10, ans + n // 20])
    return dict(q=q, a=_num(ans), d=dl, e=e, tag="Percentage",
                spec=("pct_of", (p, n)))


def profit_pct(rng):
    cp = rng.randrange(200, 3001, 100)
    p = rng.choice([5, 10, 12, 15, 20, 25, 30, 40])
    sp = cp + cp * p // 100
    q = f"A shopkeeper buys an article for {MONEY}{cp} and sells it for {MONEY}{sp}. His profit per cent is"
    e = (f"Profit = SP - CP = {sp} - {cp} = {sp - cp}. "
         f"Profit per cent = (profit / CP) x 100 = ({sp - cp}/{cp}) x 100 = {p}%. "
         f"The base is always the cost price, never the selling price.")
    dl = [f"{p + 5}%", f"{p - 5}%" if p > 5 else f"{p + 10}%", f"{p + 10}%"]
    return dict(q=q, a=f"{p}%", d=dl[:3], e=e, tag="Profit and loss",
                spec=("profit_pct", (cp, sp)))


def loss_pct(rng):
    cp = rng.randrange(200, 3001, 100)
    p = rng.choice([5, 10, 15, 20, 25])
    sp = cp - cp * p // 100
    q = f"A man buys a watch for {MONEY}{cp} and sells it for {MONEY}{sp}. His loss per cent is"
    e = (f"Loss = CP - SP = {cp} - {sp} = {cp - sp}. "
         f"Loss per cent = (loss / CP) x 100 = ({cp - sp}/{cp}) x 100 = {p}%.")
    dl = [f"{p + 5}%", f"{p - 5}%" if p > 5 else f"{p + 8}%", f"{p + 10}%"]
    return dict(q=q, a=f"{p}%", d=dl[:3], e=e, tag="Profit and loss",
                spec=("loss_pct", (cp, sp)))


def simple_interest(rng):
    P = rng.randrange(1000, 20001, 500)
    R = rng.choice([4, 5, 6, 7, 8, 9, 10, 11, 12])
    T = rng.choice([2, 3, 4, 5, 6])
    si = Fraction(P * R * T, 100)
    q = f"Find the simple interest on {MONEY}{P} at {R}% per annum for {T} years."
    e = (f"SI = (P x R x T) / 100 = ({P} x {R} x {T}) / 100 = {MONEY}{_num(si)}. "
         f"Simple interest is charged only on the principal, never on interest already earned.")
    dl = _rupees([si + P * R // 100, si - P * R // 100 if si > P * R // 100 else si + 200,
                  si + P * T // 100])
    return dict(q=q, a=MONEY + _num(si), d=dl, e=e, tag="Simple interest",
                spec=("si", (P, R, T)))


def compound_interest(rng):
    P = rng.choice([1000, 1200, 1600, 2000, 2400, 4000, 5000, 8000, 10000])
    R = rng.choice([10, 20, 25])
    T = 2
    amt = Fraction(P) * (1 + Fraction(R, 100)) ** T
    ci = amt - P
    q = (f"Find the compound interest on {MONEY}{P} at {R}% per annum for {T} years, "
         f"compounded annually.")
    e = (f"Amount = P(1 + R/100)^T = {P} x (1 + {R}/100)^2 = {_num(amt)}. "
         f"CI = Amount - P = {_num(amt)} - {P} = {MONEY}{_num(ci)}. "
         f"Compounding charges interest on the first year's interest as well.")
    dl = _rupees([ci + P * R // 100, ci - P * R // 200, ci + 100])
    return dict(q=q, a=MONEY + _num(ci), d=dl, e=e, tag="Compound interest",
                spec=("ci", (P, R, T)))


def ratio_share(rng):
    a, b = rng.choice([(2, 3), (3, 4), (4, 5), (5, 7), (3, 5), (2, 5), (5, 6), (7, 8), (4, 7)])
    total = (a + b) * rng.choice([100, 150, 200, 250, 300, 350, 400, 500, 600, 750])
    share = Fraction(total * a, a + b)
    q = (f"{MONEY}{total} is divided between A and B in the ratio {a}:{b}. "
         f"The share of A is")
    e = (f"Total parts = {a} + {b} = {a + b}. One part = {total}/{a + b} = {total // (a + b)}. "
         f"A's share = {a} x {total // (a + b)} = {MONEY}{_num(share)}.")
    dl = _rupees([Fraction(total * b, a + b), share + total // (a + b), share - total // (a + b)])
    return dict(q=q, a=MONEY + _num(share), d=dl, e=e, tag="Ratio",
                spec=("ratio", (total, a, b)))


def average_remove(rng):
    n = rng.choice([5, 6, 7, 8, 10])
    avg = rng.randrange(20, 61, 5)
    delta = rng.choice([-2, -1, 1, 2])
    rest = avg + delta                       # the new average, an exact integer
    x = n * avg - (n - 1) * rest             # the number removed
    q = (f"The average of {n} numbers is {avg}. If one of the numbers is {x}, "
         f"the average of the remaining numbers is")
    e = (f"Sum of all {n} numbers = {n} x {avg} = {n * avg}. "
         f"Sum of the rest = {n * avg} - {x} = {n * avg - x}. "
         f"Average of the remaining {n - 1} numbers = {n * avg - x}/{n - 1} = {rest}.")
    dl = _d("", [rest + 2, rest - 2, avg])
    return dict(q=q, a=_num(rest), d=dl, e=e, tag="Average",
                spec=("avg_remove", (n, avg, x)))


def work_together(rng):
    pairs = [(6, 12), (10, 15), (12, 24), (20, 30), (15, 30), (9, 18), (8, 24), (12, 6),
             (18, 9), (16, 48), (24, 8), (30, 20), (14, 35), (21, 42), (36, 12), (40, 10)]
    a, b = rng.choice(pairs)
    ans = Fraction(a * b, a + b)
    q = f"A can finish a piece of work in {a} days and B in {b} days. Working together, they will finish it in"
    e = (f"One day's work = 1/{a} + 1/{b} = {b}/{a * b} + {a}/{a * b} = "
         f"{(a + b)}/{a * b}. Time = {a * b}/{a + b} = {_num(ans)} days.")
    dl = [f"{_num(ans + 1)} days", f"{_num(ans - 1 if ans > 1 else ans + 2)} days",
          f"{_num(Fraction(a + b, 2))} days"]
    return dict(q=q + ":", a=f"{_num(ans)} days", d=dl, e=e, tag="Time and work",
                spec=("work", (a, b)))


def speed_time(rng):
    speed = rng.choice([30, 35, 40, 45, 50, 55, 60, 65, 70, 72, 75, 80, 90])
    t = rng.choice([2, 3, 4, 5, 6])
    d = speed * t
    q = f"A car covers {d} km in {t} hours. Its average speed is"
    e = (f"Speed = distance / time = {d}/{t} = {speed} km per hour. "
         f"To convert km per hour into metre per second, multiply by 5/18.")
    dl = [f"{speed + 5} km per hour", f"{speed - 5} km per hour", f"{speed + 10} km per hour"]
    return dict(q=q, a=f"{speed} km per hour", d=dl, e=e, tag="Time and distance",
                spec=("speed", (d, t)))


def train_pole(rng):
    v = rng.choice([36, 45, 54, 72, 90, 108])
    secs = rng.choice([6, 8, 10, 11, 12, 14, 15, 16, 18, 20])
    L = v * 5 * secs // 18
    q = f"A train {L} metres long is running at {v} km per hour. The time it takes to cross a pole is"
    e = (f"Speed in m/s = {v} x 5/18 = {_num(Fraction(v * 5, 18))} m/s. "
         f"Time = length / speed = {L} / ({v} x 5/18) = {secs} seconds. "
         f"A pole has no length, so only the train's own length is covered.")
    dl = [f"{secs + 2} seconds", f"{secs - 2 if secs > 4 else secs + 4} seconds",
          f"{secs + 5} seconds"]
    return dict(q=q, a=f"{secs} seconds", d=dl, e=e, tag="Trains",
                spec=("train", (L, v)))


def mixture(rng):
    a, b, c = rng.choice([(40, 25, 30), (60, 40, 45), (50, 30, 35), (80, 50, 60),
                          (45, 30, 36), (70, 40, 50), (54, 30, 42), (63, 35, 49),
                          (90, 60, 72), (48, 32, 40), (75, 45, 60), (96, 60, 72)])
    x, y = c - b, a - c
    from math import gcd
    g = gcd(x, y)
    x, y = x // g, y // g
    q = (f"In what ratio must rice at {MONEY}{a} per kg be mixed with rice at {MONEY}{b} per kg "
         f"so that the mixture costs {MONEY}{c} per kg?")
    e = (f"By the rule of alligation, ratio = (price of dearer - mean) : (mean - price of cheaper) "
         f"= ({a} - {c}) : ({c} - {b}) = {a - c}:{c - b} = {x}:{y}.")
    dl = [f"{y}:{x}", f"{x + 1}:{y}", f"{x}:{y + 1}"]
    return dict(q=q, a=f"{x}:{y}", d=dl, e=e, tag="Mixture",
                spec=("mixture", (a, b, c)))


def ages(rng):
    d = rng.randrange(3, 16)
    b = rng.choice([10, 11, 12, 14, 15, 16, 18, 20, 21, 24, 25])
    S = 2 * b + d
    a = b + d
    q = f"The sum of the ages of A and B is {S} years and A is {d} years older than B. The age of A is"
    e = (f"Let B's age be x. Then A's age is x + {d}, and x + (x + {d}) = {S}, "
         f"so 2x = {S - d} and x = {b}. A's age = {b} + {d} = {a} years.")
    dl = [f"{a + 2} years", f"{b} years", f"{a - 2} years"]
    return dict(q=q, a=f"{a} years", d=dl, e=e, tag="Problems on ages",
                spec=("ages", (S, d)))


def discount(rng):
    x = rng.choice([5, 10, 15, 20, 25, 30])
    y = rng.choice([5, 8, 10, 12, 15, 20, 25])
    single = Fraction(x + y) - Fraction(x * y, 100)
    q = f"Two successive discounts of {x}% and {y}% are equivalent to a single discount of"
    e = (f"Single discount = x + y - xy/100 = {x} + {y} - ({x} x {y})/100 "
         f"= {_num(single)}%. Successive discounts never add simply, because the second "
         f"discount is calculated on the reduced price.")
    dl = [f"{x + y}%", f"{_num(single + 1)}%", f"{_num(single - 1)}%"]
    return dict(q=q, a=f"{_num(single)}%", d=dl, e=e, tag="Discount",
                spec=("discount", (x, y)))


def net_change(rng):
    x = rng.choice([10, 15, 20, 25, 30, 40, 50])
    net = -Fraction(x * x, 100)
    q = (f"The price of an article is increased by {x}% and then decreased by {x}%. "
         f"The net change in price is")
    e = (f"Net change = +{x} - {x} - ({x} x {x})/100 = -{_num(abs(net))}%. "
         f"A rise and an equal fall never cancel, because the fall is taken on the raised price.")
    dl = [f"no change", f"{_num(abs(net))}% increase", f"{x}% decrease"]
    return dict(q=q, a=f"{_num(abs(net))}% decrease", d=dl, e=e, tag="Percentage",
                spec=("net_change", (x,)))


def boat(rng):
    u = rng.choice([8, 10, 12, 14, 15, 16, 18, 20])
    v = rng.choice([2, 3, 4, 5])
    d = (u + v) * rng.choice([2, 3, 4, 5, 6])
    t = d // (u + v)
    q = (f"A boat travels {d} km downstream in {t} hours. If the speed of the stream is "
         f"{v} km per hour, the speed of the boat in still water is")
    e = (f"Downstream speed = {d}/{t} = {u + v} km per hour. "
         f"Speed in still water = downstream speed - stream speed = {u + v} - {v} = {u} km per hour.")
    dl = [f"{u + v} km per hour", f"{u - v} km per hour", f"{u + 2 * v} km per hour"]
    return dict(q=q, a=f"{u} km per hour", d=dl, e=e, tag="Boats and streams",
                spec=("boat", (d, t, v)))



import re as _re


def _finalize(it):
    """Guarantee three distinct distractors, none equal to the answer."""
    a = it["a"]
    ds = list(it["d"])

    def key(x):
        return str(x).strip().lower()

    seen = {key(a)}
    out = []
    for x in ds:
        if key(x) in seen:
            continue
        seen.add(key(x))
        out.append(x)
    m = _re.search(r"-?\d+(?:\.\d+)?", a)
    if len(out) < 3 and m:
        num = float(m.group())
        prefix, suffix = a[:m.start()], a[m.end():]
        k = 1
        while len(out) < 3 and k < 40:
            for cand in (num + k, num - k):
                cand_s = _num(cand)
                if cand <= 0 or not cand_s:
                    continue
                cand_s = f"{prefix}{cand_s}{suffix}"
                if key(cand_s) not in seen:
                    seen.add(key(cand_s))
                    out.append(cand_s)
                    if len(out) == 3:
                        break
            k += 1
    if len(out) < 3:
        return None
    it["d"] = out[:3]
    return it


ARITH = [pct_of, profit_pct, loss_pct, simple_interest, compound_interest, ratio_share,
         average_remove, work_together, speed_time, train_pole, mixture, ages, discount,
         net_change, boat]


# ------------------------------------------------------------------ reasoning
def series_arith(rng):
    a = rng.randrange(2, 21)
    d = rng.randrange(2, 13)
    seq = [a + i * d for i in range(5)]
    ans = seq[-1] + d
    q = "Find the next number in the series: " + ", ".join(map(str, seq)) + ", ?"
    e = (f"The difference between successive terms is constant: {seq[1]} - {seq[0]} = {d}. "
         f"So the next term is {seq[-1]} + {d} = {ans}.")
    dl = [str(ans + d), str(ans - 1), str(ans + 2)]
    return dict(q=q, a=str(ans), d=dl, e=e, tag="Number series",
                spec=("series_ap", (a, d)))


def series_geo(rng):
    r = rng.choice([2, 3])
    a = rng.choice([1, 2, 3, 4, 5, 6])
    seq = [a * r ** i for i in range(4)]
    ans = seq[-1] * r
    q = "Find the next number in the series: " + ", ".join(map(str, seq)) + ", ?"
    e = (f"Each term is {r} times the term before it: {seq[1]}/{seq[0]} = {r}. "
         f"So the next term is {seq[-1]} x {r} = {ans}.")
    dl = [str(ans + r), str(ans // r), str(ans + 2)]
    return dict(q=q, a=str(ans), d=dl, e=e, tag="Number series",
                spec=("series_gp", (a, r)))


def series_square(rng):
    start = rng.randrange(1, 9)
    seq = [(start + i) ** 2 for i in range(4)]
    ans = (start + 4) ** 2
    q = "Find the next number in the series: " + ", ".join(map(str, seq)) + ", ?"
    e = (f"The terms are squares of consecutive numbers starting from {start}: "
         f"{start}^2, {start + 1}^2, {start + 2}^2, {start + 3}^2. "
         f"So the next is {start + 4}^2 = {ans}.")
    dl = [str(ans + 4), str(ans - 4), str(ans + 8)]
    return dict(q=q, a=str(ans), d=dl, e=e, tag="Number series",
                spec=("series_sq", (start,)))


def coding(rng):
    words = [("CAT", 1), ("DOG", 1), ("BAT", 2), ("PEN", 1), ("SUN", 2), ("MAP", 1),
             ("BOX", 2), ("CUP", 3), ("RAT", 2)]
    w, k = rng.choice(words)
    enc = "".join(chr(ord(c) + k) for c in w)
    q = (f"In a certain code language, if {w} is written as {enc}, how is "
         f"{w} written in that code?")
    # a self-referential trap is avoided by asking for a different word
    target, k2 = rng.choice([("FAN", k), ("TOP", k), ("BAG", k)])
    ans = "".join(chr(ord(c) + k2) for c in target)
    q = (f"In a certain code language, if {w} is written as {enc}, how is {target} written "
         f"in that code?")
    e = (f"Each letter moves {k} step{'s' if k > 1 else ''} forward in the alphabet: "
         f"{w[0]} becomes {enc[0]}, {w[1]} becomes {enc[1]}, {w[2]} becomes {enc[2]}. "
         f"Applying the same shift to {target} gives {ans}.")
    dl = ["".join(chr(ord(c) + k + 1) for c in target),
          "".join(chr(ord(c) + k - 1) for c in target),
          "".join(chr(ord(c) + k + 2) for c in target)]
    return dict(q=q, a=ans, d=dl, e=e, tag="Coding and decoding",
                spec=("coding", (w, k, target)))


BLOOD = [
    ("P is the mother of Q. Q is the brother of R. How is P related to R?", "mother",
     ["sister", "aunt", "grandmother"],
     "P is the mother of both Q and R, since Q and R are brother and sister."),
    ("A is the son of B. B is the daughter of C. How is A related to C?", "grandson",
     ["son", "nephew", "brother"],
     "B is C's daughter, so B's son A is C's grandson."),
    ("X is the brother of Y. Y is the daughter of Z. How is X related to Z?", "son",
     ["brother", "nephew", "grandson"],
     "X and Y are children of Z, and X is male, so X is Z's son."),
    ("A is the husband of B. B is the sister of C. How is A related to C?", "brother-in-law",
     ["son-in-law", "cousin", "uncle"],
     "A is married to C's sister, so A is C's brother-in-law."),
    ("R is the father of S. S is the sister of T. How is R related to T?", "father",
     ["uncle", "brother", "grandfather"],
     "S and T are siblings, and R is the father of S, so R is also T's father."),
    ("M is the daughter of N. N is the son of O. How is M related to O?", "granddaughter",
     ["daughter", "niece", "sister"],
     "N is O's son and M is N's daughter, so M is O's granddaughter."),
    ("K is the wife of L. L is the son of M. How is K related to M?", "daughter-in-law",
     ["sister-in-law", "niece", "cousin"],
     "K is married to M's son L, so K is M's daughter-in-law."),
    ("D is the brother of E. E is the mother of F. How is D related to F?", "uncle",
     ["father", "brother", "grandfather"],
     "D is the brother of F's mother E, so D is F's uncle."),
]


def blood(rng):
    q, a, dl, e = rng.choice(BLOOD)
    return dict(q=q, a=a, d=list(dl), e=e, tag="Blood relations", spec=("blood", (q,)))


def direction(rng):
    n, e_ = rng.choice([(3, 4), (6, 8), (5, 12), (9, 12), (8, 15)])
    q = (f"A man walks {n} km towards the north, then turns right and walks {e_} km. "
         f"How far is he from his starting point?")
    d = (n * n + e_ * e_) ** 0.5
    ans = f"{int(d) if d == int(d) else d:.0f} km".strip()
    ans = f"{int(d)} km" if abs(d - round(d)) < 1e-9 else f"{d:.2f} km"
    e = (f"The two walks are at right angles, so the distance is the hypotenuse: "
         f"sqrt({n}^2 + {e_}^2) = sqrt({n * n + e_ * e_}) = {ans}. "
         f"Turning right from north means walking east.")
    dl = [f"{n + e_} km", f"{abs(e_ - n)} km", f"{n * e_} km"]
    return dict(q=q, a=ans, d=dl, e=e, tag="Direction sense",
                spec=("direction", (n, e_)))


def odd_square(rng):
    base = rng.randrange(3, 11)
    squares = [(base + i) ** 2 for i in range(3)]
    odd = squares[1] + rng.choice([2, 3, 5])
    options = squares + [odd]
    rng.shuffle(options)
    q = "Which one of the following is not a perfect square: " + ", ".join(map(str, options)) + "?"
    e = (f"{squares[0]} = {int(squares[0] ** 0.5)}^2, {squares[1]} = {int(squares[1] ** 0.5)}^2 and "
         f"{squares[2]} = {int(squares[2] ** 0.5)}^2 are perfect squares. {odd} lies between "
         f"{int(odd ** 0.5)}^2 = {int(odd ** 0.5) ** 2} and {int(odd ** 0.5) + 1}^2 = "
         f"{(int(odd ** 0.5) + 1) ** 2}, so it is not a square.")
    return dict(q=q, a=str(odd), d=[str(x) for x in squares], e=e, tag="Odd one out",
                spec=("odd_sq", (base, odd)))


def alphabet(rng):
    pos = rng.randrange(3, 21)
    shift = rng.choice([2, 3, 4, 5, 6])
    target = pos + shift
    ans = chr(ord("A") + target - 1)
    q = (f"Which letter is the {shift}th letter to the right of the {pos}th letter from the "
         f"left of the English alphabet?")
    e = (f"The {pos}th letter from the left is {chr(ord('A') + pos - 1)}. Moving {shift} places "
         f"to the right gives position {pos} + {shift} = {target}, which is {ans}.")
    dl = [chr(ord(ans) + 1), chr(ord(ans) - 1), chr(ord(ans) + 2)]
    return dict(q=q, a=ans, d=dl, e=e, tag="Alphabet test",
                spec=("alphabet", (pos, shift)))


def ranking(rng):
    n = rng.randrange(25, 61)
    left = rng.randrange(5, 21)
    ans = n - left + 1
    q = (f"In a row of {n} students, A is {left}th from the left end. What is A's position "
         f"from the right end?")
    e = (f"Position from the right = total - position from the left + 1 = {n} - {left} + 1 = {ans}. "
         f"The 1 is added because A is counted at both ends.")
    dl = [str(ans + 1), str(ans - 1), str(n - left)]
    return dict(q=q, a=str(ans), d=dl, e=e, tag="Ranking",
                spec=("ranking", (n, left)))


def clock(rng):
    h = rng.randrange(1, 13)
    m = rng.choice([0, 10, 20, 30, 40, 50])
    ang = abs(30 * h - 5.5 * m)
    ang = min(ang, 360 - ang)
    ang = Fraction(ang).limit_denominator(2)
    q = f"What is the angle between the hour hand and the minute hand of a clock at {h}:{m:02d}?"
    e = (f"Angle = |30H - 5.5M| = |30 x {h} - 5.5 x {m}| = {_num(ang)} degrees. "
         f"The hour hand moves 0.5 degree a minute and the minute hand 6 degrees a minute.")
    dl = [f"{_num(ang + 10)} degrees", f"{_num(abs(360 - ang))} degrees", f"{_num(ang + 15)} degrees"]
    return dict(q=q, a=f"{_num(ang)} degrees", d=dl, e=e, tag="Clock",
                spec=("clock", (h, m)))


import datetime


def calendar(rng):
    _pool = [(2026, mm, dd) for mm in range(1, 13) for dd in (1, 5, 10, 15, 20, 25)]
    d = rng.choice(_pool)
    ref = datetime.date(2026, 1, 1)
    target = datetime.date(*d)
    days = (target - ref).days
    ref_name = ref.strftime("%A")
    ans = target.strftime("%A")
    q = (f"If 1 January 2026 is a {ref_name}, what day of the week is "
         f"{target.day} {target.strftime('%B')} {target.year}?")
    e = (f"From 1 January 2026 to {target.day} {target.strftime('%B')} {target.year} is "
         f"{days} days. Dividing {days} by 7 leaves a remainder of {days % 7}, so the day "
         f"advances {days % 7} place(s) from {ref_name}, giving {ans}.")
    names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    i = names.index(ans)
    dl = [names[(i + 1) % 7], names[(i + 2) % 7], names[(i - 1) % 7]]
    return dict(q=q, a=ans, d=dl, e=e, tag="Calendar",
                spec=("calendar", d))


ANALOGY = [
    ("Doctor : Hospital :: Teacher : ?", "School", ["Court", "Factory", "Farm"],
     "A doctor works in a hospital as a teacher works in a school."),
    ("Pen : Write :: Knife : ?", "Cut", ["Sharp", "Metal", "Handle"],
     "A pen is used to write as a knife is used to cut."),
    ("Bird : Nest :: Bee : ?", "Hive", ["Web", "Burrow", "Kennel"],
     "A bird lives in a nest as a bee lives in a hive."),
    ("Book : Pages :: Ladder : ?", "Rungs", ["Wood", "Height", "Steps"],
     "A book is made of pages as a ladder is made of rungs."),
    ("Eye : See :: Ear : ?", "Hear", ["Sound", "Lobe", "Deaf"],
     "The eye is the organ of sight as the ear is the organ of hearing."),
    ("Cow : Calf :: Sheep : ?", "Lamb", ["Kid", "Puppy", "Foal"],
     "The young of a cow is a calf as the young of a sheep is a lamb."),
    ("Water : Thirst :: Food : ?", "Hunger", ["Taste", "Cook", "Plate"],
     "Water removes thirst as food removes hunger."),
    ("2 : 8 :: 3 : ?", "27", ["9", "12", "18"],
     "8 is 2 cubed, so the answer is 3 cubed = 27."),
    ("5 : 25 :: 7 : ?", "49", ["35", "42", "56"],
     "Each number is paired with its square: 5 squared is 25, so 7 squared is 49."),
]


def analogy(rng):
    q, a, dl, e = rng.choice(ANALOGY)
    return dict(q=q, a=a, d=list(dl), e=e, tag="Analogy", spec=("analogy", (q,)))


REASON = [series_arith, series_geo, series_square, coding, blood, direction, odd_square,
          alphabet, ranking, clock, calendar, analogy]


def build_pool(seed=8080):
    rng = random.Random(seed)
    items = []
    seen = set()

    def add(it):
        key = it["q"].strip().lower()
        if key in seen:
            return False
        seen.add(key)
        items.append(it)
        return True

    for kind, gens, target in (("arith", ARITH, 200), ("reason", REASON, 120)):
        got = 0
        i = 0
        stalls = 0
        while got < target and stalls < 600:
            g = gens[i % len(gens)]
            i += 1
            it = g(rng)
            it["kind"] = kind
            it = _finalize(it)
            if it is None:
                stalls += 1
                continue
            if add(it):
                got += 1
                stalls = 0
            else:
                stalls += 1
        if got < target:
            raise RuntimeError(f"{kind}: only {got} of {target} unique items")

    return items


if __name__ == "__main__":
    pool = build_pool()
    print("pool size:", len(pool))
    from collections import Counter
    print(Counter(i["kind"] for i in pool))
    print(Counter(i["tag"] for i in pool).most_common())
    for i in pool[:3]:
        print(i["q"], "|", i["a"], "|", i["d"], "|", i["e"][:60])

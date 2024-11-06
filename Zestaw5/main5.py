#Adam Nowak
import math

# frac1 + frac2
def add_frac(frac1, frac2):
    if frac1[1] == 0 and frac2[1] == 0:
        raise ZeroDivisionError("Denominator can't be zero")
    else:
        #common denominator y, x is a numerator
        x = frac1[0] * frac2[1] + frac1[1] * frac2[0]
        y = frac1[1] * frac2[1]
        return simplify_fraction(x,y)

# frac1 - frac2
def sub_frac(frac1, frac2):
    if frac1[1] == 0 and frac2[1] == 0:
        raise ZeroDivisionError("Denominator can't be zero")
    else:
        x = frac1[0] * frac2[1] - frac1[1] * frac2[0]
        y = frac1[1] * frac2[1]
        return simplify_fraction(x, y)

# frac1 * frac2
def mul_frac(frac1, frac2):
    x = frac1[0] * frac2[0]
    y = frac1[1] * frac2[1]
    if x == 0 and y == 0:
        raise ZeroDivisionError("Denominator can't be zero")
    else:
        return simplify_fraction(x, y)

# frac1 / frac2
def div_frac(frac1, frac2):
    x = frac1[0] * frac2[1]
    y = frac1[1] * frac2[0]
    if x == 0 and y == 0:
        raise ZeroDivisionError("Denominator can't be zero")
    else:
        return simplify_fraction(x, y)

# bool, czy dodatni
def is_positive(frac):
    if frac[1] == 0:
        raise ZeroDivisionError("Denominator can't be zero")
    else:
        return frac[0] > 0 and frac[1] > 0 or frac[0] < 0 and frac[1] < 0

 # bool, typu [0, x]
def is_zero(frac):
    if frac[1] == 0:
        raise ZeroDivisionError("Denominator can't be zero")
    else:
        return frac[0] == 0

 # -1 | 0 | +1
def cmp_frac(frac1, frac2):
    if frac1[1] == 0 and frac2[1] == 0:
        raise ZeroDivisionError("Denominator can't be zero")
    else:
        new_x1 = frac1[0] * frac2[1]
        new_x2 = frac2[0] * frac1[1]
        if new_x1 == new_x2:
            return 0
        if new_x1 > new_x2:
            return 1
        else:
            return -1

# konwersja do float
def frac2float(frac):
    if frac[1] == 0:
        raise ZeroDivisionError("Denominator can't be zero")
    else:
        return float(frac[0] / frac[1])

def simplify_fraction(x, y):
    nwd = math.gcd(x, y)
    new_x = x / nwd
    new_y = y / nwd
    return [new_x, new_y]


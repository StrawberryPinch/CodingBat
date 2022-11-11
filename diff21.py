"""Brainstorm:
    result = 21 - n
        if result < 0:
            return abs(result) * 2
        else:
            return abs(result)
"""

from unit_test import unit_test

def diff21(n):
    result = 21 - n
    if result <= 0:
        return abs(result) * 2
    else:
        return abs(result)

unit_test(2, diff21(19))
unit_test(11, diff21(10))
unit_test(0, diff21(21))

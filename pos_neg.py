"""Psudocode:
If parameter 'negative' is true AND both ints are negative,
    return True
else:
    return False
If parameter 'negative' is false,
check values of both ints
both neg or both pos
    return False"""

from unit_test import unit_test

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))


unit_test(True, pos_neg(1, -1, False))
unit_test(True, pos_neg(-1, 1, False))
unit_test(True, pos_neg(-4, -5, True))
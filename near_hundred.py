from unit_test import unit_test

def near_hundred(n):
    if abs(n - 100) <= 10:
        return True
    if abs(n - 200) <= 10:
        return True
    else:
        return False
  

unit_test(True, near_hundred(93))
unit_test(True, near_hundred(90))
unit_test(False, near_hundred(89))

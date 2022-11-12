from unit_test import unit_test

def makes10(a, b):
    if a == 10 or b == 10:
        return True
    if a + b == 10:
        return True
    else:
        return False

unit_test(True, makes10(9,10))
unit_test(False, makes10(9,9))
unit_test(True, makes10(1,9))
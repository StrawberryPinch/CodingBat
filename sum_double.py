from unit_test import unit_test

def sum_double(a, b):
    sum = a + b
    if a == b:
        sum = sum * 2
    return sum

unit_test(4, sum_double(a = 1, b = 1))
unit_test(8, sum_double(a = 6, b = 2))
unit_test(0, sum_double(a = 0, b = 0))
unit_test(8, sum_double(a = 5, b = 3))
unit_test(23, sum_double(a = 22, b = 1))
unit_test(5, sum_double(a = 0, b = 5))
unit_test(0, sum_double(a = -1, b = 1))
unit_test(5, sum_double(a = 7, b = -2))


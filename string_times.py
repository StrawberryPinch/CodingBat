from unit_test import unit_test

def string_times(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result
        

unit_test('HiHi', string_times('Hi', 2))
unit_test('HiHiHi', string_times('Hi', 3))
unit_test('Hi', string_times('Hi', 1))


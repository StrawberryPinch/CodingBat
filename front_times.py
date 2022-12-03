from unit_test import unit_test

def front_times(str, n):
    result = ""
    for i in range(n):
        result = result + str[:3]
    return result

unit_test('ChoCho', front_times('Chocolate', 2))
unit_test('ChoChoCho', front_times('Chocolate', 3))
unit_test('AbcAbcAbc', front_times('Abc', 3))
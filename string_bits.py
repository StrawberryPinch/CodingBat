from unit_test import unit_test

def string_bits(str):
    n = len(str)
    result = ""
    for i in range(n):
        if (i % 2) == 0:
            result = result + str[i]
    print(result)
    return result
    


unit_test('Hlo', string_bits('Hello'))
unit_test('H', string_bits('Hi'))
unit_test('Hello', string_bits('Heeololeo'))
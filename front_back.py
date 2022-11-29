from unit_test import unit_test

def front_back(str):
    print(str[0])
    print(str[-1])
    print(str[-1] + str[1:-1] + str[0])
    if len(str) <= 1:
        return str
    return str[-1] + str[1:-1] + str[0]

unit_test('eodc', front_back('code'))
unit_test('a', front_back('a'))
unit_test('ba', front_back('ab'))
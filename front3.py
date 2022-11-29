from unit_test import unit_test

def front3(str):
    # return str[:3] + str[:3] + str[:3]
    return str[:3] * 3

unit_test('JavJavJav', front3('Java'))
unit_test('ChoChoCho', front3('Chocolate'))
unit_test('abcabcabc', front3('abc'))
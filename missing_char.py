from unit_test import unit_test

def missing_char(str, n):
    print(str[:n])
    print(str[n+1:])
    return str[:n] + str[n+1:]

unit_test('ktten', missing_char('kitten', 1))
unit_test('itten', missing_char('kitten', 0))
unit_test('kittn', missing_char('kitten', 4))
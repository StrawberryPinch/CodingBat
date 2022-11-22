from unit_test import unit_test

def not_string(str):
    if str[:3] == "not":
        return str
    return 'not ' + str


unit_test('not candy', not_string('candy'))
unit_test('not x', not_string('x'))
unit_test('not bad', not_string('not bad'))
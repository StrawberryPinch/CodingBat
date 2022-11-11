from unit_test import unit_test

"""

if a and b are not smily: return true
if a and b are smily: return true
otherwise return false

"""


def monkey_trouble(a_smile, b_smile):
    if not a_smile and not b_smile:
        return True
    elif a_smile and b_smile:
        return True
    else:
        return False



def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile




unit_test(True, monkey_trouble(a_smile = True, b_smile = True))
unit_test(True, monkey_trouble(a_smile = False, b_smile = False))
unit_test(False, monkey_trouble(a_smile = True, b_smile = False))
unit_test(False, monkey_trouble(a_smile = False, b_smile = True))



"""Brainstorm:
define talking or not
define hour
if not talking = no trouble
if hour >7 & talking = trouble
if hour <20 & talking = trouble
"""

from unit_test import unit_test

def parrot_trouble(talking, hour):
    if talking == True and (hour < 7 or hour > 20):
        return True
    return False

unit_test(True, parrot_trouble(talking = True, hour = 6))
unit_test(False, parrot_trouble(talking = True, hour = 7))
unit_test(False, parrot_trouble(talking = False, hour = 6))
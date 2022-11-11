def sleep_in(weekday, vacation):
    if not weekday or vacation: 
        return True
    else: 
        return False

print("======================================================")

print(sleep_in(weekday = False, vacation = False))
print(sleep_in(weekday = True, vacation = False))
print(sleep_in(weekday = False, vacation = True))
print(sleep_in(weekday = True, vacation = True))

print("======================================================")


""" 
Expected	Run		
sleep_in(False, False) → True	True	OK	
sleep_in(True, False) → False	False	OK	
sleep_in(False, True) → True	True	OK	
sleep_in(True, True) → True     True	OK

"""

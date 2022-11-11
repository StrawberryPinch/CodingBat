def monkey_trouble(a_smile, b_smile):
    if not a_smile and not b_smile:
        return True
    elif a_smile and b_smile:
        return True
    else:
        return False





print("======================================================")

print(monkey_trouble(a_smile = True, b_smile = True))
print(monkey_trouble(a_smile = False, b_smile = False))
print(monkey_trouble(a_smile = True, b_smile = False))
print(monkey_trouble(a_smile = False, b_smile = True))


print("======================================================")


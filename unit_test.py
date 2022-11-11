def unit_test(expected, actual):
    print("================================")
    if expected == actual:
        print("Success!!")
    else:
        print("Fail")
        print("Expected: " + str(expected))
        print("Actual  : " + str(actual))

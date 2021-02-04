weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.lower() == 'l':
    print("Your are " + str(int(weight) * 0.453592) + " Kilos")
elif unit.lower() == 'k':
    print("Your are " + str(int(weight) * 2.20462) + " Pounds")
else:
    print("Make Sure to Use Right Choice")
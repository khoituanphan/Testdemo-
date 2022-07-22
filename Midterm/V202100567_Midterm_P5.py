def compare(state1, state2):
    if len(state1) == len(state2):
        if state1 < state2:
            print(state1+" should be listed first.")
        else:
            print(state2+" should be listed first.")
        print(True)
    else:
        print(False)

    if name1 == name2:
        print("The strings are identical!")
    else:
        print("The strings are NOT identical!")

name1 = 'North Carolina'
name2 = 'South Carolina'
name3 = 'Virginia'
result1 = compare(name1, name2)
result2 = compare(name2, name3)


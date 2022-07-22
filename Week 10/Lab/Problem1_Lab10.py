def key_find(arr, number):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low)//2
        value = arr[mid]
        if value == number:
            return mid
        if value > number:
            high = mid -1
        if value < number:
            low = mid + 1
    return False
winer_id = list(map(int, input("Enter the top participant's ID: ").split()))
sorted_List = sorted(winer_id)
print("Sorted top participant's ID: {}".format(sorted_List))
search_participants = int(input("Enter Participant's ID: "))

if key_find(sorted_List, search_participants) != False:
    print('Congratulations! You have been short listed in the Top 10 "Best Programmer 2020" .')
else:
    print("Unsuccessfulll!")

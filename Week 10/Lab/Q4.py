
list_of_integer  = list(map(int, input("Enter a list of integer number: ").split()))
sorting_list = sorted(list_of_integer)
number_to_search = int(input("Enter a number to search: "))
list_after_check = []
def linear_search(arr, number):
    check_list = []
    for i in range (len(arr)):
        check_list.append((arr[i]))
        if number == arr[i]:
            print("Linear Search: List of checked number: {}".format(check_list))
            return True
    else:
        return -1



def binary_search(array, key):
    low = 0
    mid = 0
    high = len(array)-1
    while low <= high:
        mid = (high + low)//2
        value = array[mid]
        list_after_check.append(value)
        if value == key:
            return mid
        if value > key:
            high = mid -1
        if value < key:
            low = mid + 1
    return -1


    
if linear_search(list_of_integer, number_to_search) == True:
    print("Found!")
else:
    print("Not found!")
print("Sorted List: {}".format(sorting_list))


binary_search(list_of_integer, number_to_search)
print("Binary Search: List of checked numbers:".format(list_after_check))
if binary_search(list_of_integer, number_to_search) != False:
    print("Found!")
else:
    print("Not found!")

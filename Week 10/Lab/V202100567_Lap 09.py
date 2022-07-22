"""
VinUniversity
COMP1010  Introduction  to  Programming
Lab 9 - Week 10 - Sorting and Search Algorithms
by Phan Tuan Khoi (V202100567)

Group: 1
Date: Nov 25, 2021

Disclaimer: I certify  that  this  assignment  is my own  work  and←↩
that I have  not  copied  in part or whole or  otherwise  plagiarised←↩
the  work of other  students  and/or  persons.
"""

"""
#--------------------------Problem 1--------------------------------
# Shorting participants
#-------------------------------------------------------------------
"""
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
"""
#--------------------------Problem 2--------------------------------
#  Sorting a list in ascending order
#-------------------------------------------------------------------
"""
numbers_of_elements = int(input("Enter number of elements: "))
list_of_number = []
for i in range (numbers_of_elements):
    arr = int(input())
    list_of_number.append(arr)
    sorted_list = (sorted(list_of_number))
print("Sorted array:")
print(*sorted_list)
"""
#--------------------------Problem 3--------------------------------
#  Partially sorted list
#-------------------------------------------------------------------
"""
A = [5, 4, 6, 3, 1, 2]
for i in range(len(A)):
    min_value = A.index(min(A[i:]))
    A[min_value], A[i] = A[i], A[min_value]
    print("Partially sorted list {}".format(i+1))
    print(*A)
    print()
print("Sorted list: ")
print(*A)
"""
#--------------------------Problem 4--------------------------------
#  Linear search vs Binary search
#-------------------------------------------------------------------
"""

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

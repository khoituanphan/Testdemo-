"""
VinUniversity
COMP1010 Introduction to Programming
Lab 08 - Week 9 - Tuples, Dictionaries, Algorithm Complexity,and Linear Search
by Phan Tuan Khoi V202100567

Group: 1
Date: Nov 18, 2021

Disclaimer: I certify that this assignment is my own work and that I have not copied in part or whole or
otherwise plagiarised the work of other students and/or persons.
#--------------------------Problem 1--------------------------------
#  The sum of the elements in a tuple
#-------------------------------------------------------------------
"""
my_tuple  = tuple(input("Enter a tuple elements separated by space: ").split(" "))
print("Your tuple is {}".format(my_tuple))
total = sum(map(int, my_tuple))
print("The sum of the elements in your tuple is {}.".format(total))
"""
#--------------------------Problem 2--------------------------------
#  Dictionary
#-------------------------------------------------------------------
"""

sales_2020 = {"Jan": 500, "Feb": 1200, "March": 750, "Apr": 250, "May": 950, "June": 1350, "July": 300, "Aug": 320,
              "Sept": 1000, "Oct": 200, "Nov": 1400, "Dec": 980}
sales_2019 = {"Jan": 1500, "Feb": 1000, "March": 850, "Apr": 1250, "May": 980, "June": 1020, "July": 800, "Aug": 1320,
              "Sept": 960, "Oct": 1200, "Nov": 1300, "Dec": 1980}
sales_2018 = {"Jan": 100, "Feb": 1500, "March": 2150, "Apr": 560, "May": 780, "June": 820, "July": 400, "Aug": 220,
              "Sept": 1960, "Oct": 920, "Nov": 600, "Dec": 180}
sales_2017 = {"Jan": 410, "Feb": 620, "March": 1150, "Apr": 190, "May": 380, "June": 220, "July": 490, "Aug": 1120,
              "Sept": 190, "Oct": 1130, "Nov": 330, "Dec": 720}

sales_year = {2020, 2019, 2018, 2017}

while True:
    targeted_year = int(input("Enter the targeted year: "))
    if targeted_year not in sales_year:
        print("Records not found")
        continue
    elif targeted_year == 2017:
        chosen_year = sales_2017
    elif targeted_year == 2018:
        chosen_year = sales_2018
    elif targeted_year == 2019:
        chosen_year = sales_2019
    elif targeted_year == 2020:
        chosen_year = sales_2020
    sales = float(input("Enter the sales target amount (USD): "))
    numbers_of_year = 0
    for month in chosen_year:
        if chosen_year[month] >= sales:
            print(f"{month}, ${chosen_year[month]:,.2f}")
            numbers_of_year += 1
    print()
    print("Total months that met the sales target: {}".format(numbers_of_year))
    print(f"Total sales for this year is ${sum(chosen_year.values()):,.2f}")
    break
"""
#--------------------------Problem 3A--------------------------------
#  Complexity and Big-O Notation
#-------------------------------------------------------------------
    The complexity of this function is O(n) because it run from 2 to n
"""
"""
#--------------------------Problem 3C--------------------------------
#  Complexity and Big-O Notation
#-------------------------------------------------------------------

The complexity here is 0(Log2(n) because it constainly divide by 2
#--------------------------Problem 4-------------------------------
# Linear Search
#------------------------------------------------------------------
"""
arr = [10, 7, 2, 13, 4, 52, 6, 17, 81, 49]
num = int(input("Enter first number: "))
def linear_search(arr, num_find):
    for i in range(len(arr)):

        if arr[i] == num_find:
            return i
    return "not found"
place = linear_search(arr, num) + 1
if linear_search(arr, num) == "not found":
    print("Number {} not found".format(num))
else:
    print("Number {} is found at position {}".format(num,place))


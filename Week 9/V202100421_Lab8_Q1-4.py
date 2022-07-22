"""
VinUniversity
COMP1010  Introduction  to  Programming
Lab 8 - Week 8 - Tuples, Dictionaries, Algorithm Complexity, and Linear Search
by Vu Binh Minh (V202100421)

Group: 1
Date: Nov 18, 2021

Disclaimer: I certify  that  this  assignment  is my own  work  and←↩
that I have  not  copied  in part or whole or  otherwise  plagiarised←↩
the  work of other  students  and/or  persons.
"""

"""
#--------------------------Problem 1--------------------------------
# The sum of the elements in a tuple
#-------------------------------------------------------------------
"""
# Prompt user for the input
my_tuple = input("Enter a tuple elements separated by space: ")
# Split the input and convert it to tuple
my_tuple = tuple(my_tuple.split())
# Create a empty tuple
new_tuple = ()
# Create new tuple with integer element
for i in my_tuple:
    new_tuple += (int(i),)
# Print out the result
print(f"Your tuple is {my_tuple}")
print(f"The sum of the elements in your tuple is {sum(new_tuple)}.")
print()
"""
#--------------------------Problem 2--------------------------------
# Dictionary
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
    # Prompt user for the year
    target = input("Enter the targeted year: ")
    # Check if the year is found
    if int(target) not in sales_year:
        print("Records not found")
        # Continue the while-loop, skipping other steps
        continue
    # Check which year is the year
    elif int(target) == 2017:
        sales = sales_2017
    elif int(target) == 2018:
        sales = sales_2018
    elif int(target) == 2019:
        sales = sales_2019
    else:
        sales = sales_2020
    # Prompt user for the sales target amount
    amount = float(input("Enter the sales target amount (USD): "))
    # Set up a counter
    count = 0
    # Print out the result
    for i in sales:
        if sales[i] >= amount:
            print(f"{i}, ${sales[i]:,.2f}")
            count += 1
    print("\n")
    # Print out the result
    print(f"Total months that met the sales target: {count}")
    print(f"Total sales for this year is ${sum(sales.values()):,.2f}")
    break
print()
"""
#--------------------------Problem 3--------------------------------
# Complexity and Big-O Notation
#-------------------------------------------------------------------
"""
#3A
"""
    The complexity of this iterative Fibonancci function is O(n)
    because there is a for-loop of n - 2 time, there is a simple statement with complexity O(1).
    Therefore, again the complexity of the program is O(1) * n = O(n),
    which is linear with the input n.
"""
#3B
"""
    The complexity of this function is O(log(n)) because the while-loop
    will run log2(n). Therefore, the complexity of the function is O(log(n))
"""
"""
#--------------------------Problem 4--------------------------------
# Linear Search
#-------------------------------------------------------------------
"""
arr = [10, 7, 2, 13, 4, 52, 6, 17, 81, 49]
# Prompt user for the number to search
num = int(input("Enter first number: "))

def linear_search(arr, num_find):
    # Loop through the list to search for the number
    for i in arr:
        # Check if number is in list
        if i == num_find:
            # Record the index
            index = arr.index(i) + 1
            # Print out the result
            print(f"Number {num_find} found at position {index}")
            return index
    # Print the result if number is not found
    print(f"Number {num_find} not found")

# Call the function
a = linear_search(arr, num)
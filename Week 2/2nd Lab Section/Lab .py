"""
VinUniversity
COMP1010 Introduction to Programming
Lab 02 - Week 2 - Getting started with Python
by Phan Tuan Khoi V202100567

Group: 1
Date: Sept 30, 2021

Disclaimer: I certify that this assignment is my own work and that I have not copied in part or whole or
otherwise plagiarised the work of other students and/or persons.
"""

"""
#--------------------------Problem 1--------------------------------
#  Assignment Operators
#-------------------------------------------------------------------
"""
# Declare the number
value1 = 12
value2 = 9
#Add together
a = value1 + value2
b = a + value1
# print out the number
print(b)
"""
#--------------------------Problem 2--------------------------------
# Assignment with User Input
#-------------------------------------------------------------------
"""
cnumber = int(input("Enter the class number: "))
grade =  float(input("Enter the total grade: "))
averagescore = grade/cnumber # calculate the average number before print out
print(averagescore)
"""
#--------------------------Problem 3--------------------------------
# Membership Operators
#-------------------------------------------------------------------
"""
a = 10
b = 18
list = [19,12,3, 14, 25, 10]
if a or b in list: # check wether a or b in the declared list
    print("value is in the list ")
else:
    print("value is not in the list")
"""
#--------------------------Problem 4--------------------------------
# Data Types
#-------------------------------------------------------------------
"""
number1 =    int(input("Enter the integer number: "))
number2 =  float(input("Enter the float grade: "))

#calculate the number
total = str(number1 +number2)
different = str(abs(number1 - number2))
print("The total value is: " + total + "the different is: " + different)
"""
#--------------------------Problem 5--------------------------------
# Geometric sequence
#-------------------------------------------------------------------
"""
# Declare the input
n = int(input("Number of terms: "))
a = float(input("The first term: "))
r = float(input("The common ratio"))
# Calculate the number
final = a*(1-r**n)/1-r
print (final)


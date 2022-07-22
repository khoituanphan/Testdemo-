"""
VinUniversity
COMP1010 Introduction to Programming
Lab 04 - Week 4 - Strings and Testing
by Phan Tuan Khoi V202100567

Group: 1
Date: Oct 14, 2021

Disclaimer: I certify that this assignment is my own work and that I have not copied in part or whole or
otherwise plagiarised the work of other students and/or persons.
"""
import random

"""
#--------------------------Problem 1--------------------------------
#  Create a long multi-line string in Python
#-------------------------------------------------------------------
"""
print("""Dear Alice,

How have you been? I am fine. There is a container in the fridge
that is labeled "Milk Experiment". Please do not drink it.

Sincerely,
Bob""")

"""
#--------------------------Problem 2--------------------------------
#  String slicing
#-------------------------------------------------------------------
"""
a = "Everyone Should"
b = " Lea"
c = " tC"
should = a[8:]
rn = a[3:7:3]
t = c[0:2]
o = a[5:6]
C = c[0:3:2]
od = a[5:19:9]
e = a[2:3]

print(a + b + rn + t + o + C + od + e)
"""
#--------------------------Problem 3--------------------------------
#  String methods (a)
#-------------------------------------------------------------------
"""
str1 = "Everyone should know how to program a computer"
str2 = "because it teaches you how to think!"
print("{},{} ".format(str1, str2))
"""
#--------------------------Problem 3--------------------------------
#  String methods (b)
#-------------------------------------------------------------------
"""
str1 = "Everyone should know how to program a computer"
str2 = "because it teaches you how to think!"
a = str2[:19]
b = str2[19:23]
c = str2[22:36]
d = '"{}","{}","{}"'.format(a,b,c)
print (d)
"""
#--------------------------Problem 3--------------------------------
#  String methods (c)
#-------------------------------------------------------------------
"""
str1 = "Everyone should know how to program a computer"
str2 = "because it teaches you how to think!"
a = str2[:18]
b = str2[19:23]
c = str2[23:36]
d = '"{}","{}","{}"'.format(a,b,c)
e = d[28:45]
print (e)
"""
#--------------------------Problem 3--------------------------------
#  String methods (d)
#-------------------------------------------------------------------
"""
str1 = "Everyone should know how to program a computer"
str2 = "because it teaches you how to think!"
a = str2[:18]
b = str2[19:23]
c = str2[23:36]
d = '"{}","{}","{}"'.format(a,b,c)
e = d[28:45]
print(len(e))
"""
#--------------------------Problem 3--------------------------------
#  String methods (e)
#-------------------------------------------------------------------
"""
str1 = "Everyone should know how to program a computer"
str2 = "because it teaches you how to think!"
str3 = input("Type here: ")
print (str1.replace("program a computer", str3))
"""
#--------------------------Problem 4--------------------------------
#  Combine the character
#-------------------------------------------------------------------
"""
a = input("Enter a word: ")
b = random.choice(a.upper())
c = random.randint(10, 30)
print("{}{}".format(b, c))
"""
#--------------------------Problem 5--------------------------------
#  Debugging
#-------------------------------------------------------------------
"""
h = float(input("Enter your height in metres: "))
w = float(input("Enter your weight in kg: "))


def calculate_bmi(weight, height):
    return weight / (height ** 2)


bmi = calculate_bmi(w, h)

print("Patient's BMI is: %f" % bmi)
"""
#--------------------------Problem 6--------------------------------
#  Identifying Variable Name Errors
#-------------------------------------------------------------------
"""
# use a if the number is a multiple of 3 , otherwise use b



message = ""
for number in range(10):
    if (number % 3) == 0:
        message = message + "a"
    else:
        message = message + "b"
print(message)

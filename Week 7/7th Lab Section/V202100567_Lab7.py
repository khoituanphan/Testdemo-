"""
VinUniversity
COMP1010 Introduction to Programming
Lab 07 - Week 7 - Lists, iteration, and loops
by Phan Tuan Khoi V202100567

Group: 1
Date: Oct 11, 2021

Disclaimer: I certify that this assignment is my own work and that I have not copied in part or whole or
otherwise plagiarised the work of other students and/or persons.
"""
"""
#--------------------------Problem 1--------------------------------
#  Check prime number
#-------------------------------------------------------------------
"""
def is_prime(x):
    for num in range(2, x):
        if x % num == 0:
            return False
    return True
for num in range(2, 200):
    if is_prime(num):
        print(num, end=" ")
"""
#--------------------------Problem 2--------------------------------
#  Creating an acronym generator
#-------------------------------------------------------------------
"""
word=["but", "do", "not", "to", "has", "have", "had", "then", "who", "when", "is", "why","what", "how", "while", "hence", "I", "you", "he", "she", "it", "a", "for", "by","an", "am", "the", "so", "and", "my", "are", "in", "at", "on"]
user_input = (input("Enter sentence")).split()
for i in user_input:
    if i != "I":
        a = i.lower()
        if a not in word:
            print(i[0].upper(), end="")
"""
#--------------------------Problem 3--------------------------------
#  Sum of zero ending numbers
#-------------------------------------------------------------------
"""
def zero_ending(scores):
    total = 0
    for num in scores:
        if num % 10 == 0:
            total += num
    return total

"""
#--------------------------Problem 4--------------------------------
#  Nested Loops and Matrices
#-------------------------------------------------------------------
"""

file1  = [[12, 7, 3],[4, 5, 6],[7, 8, 9]]
file2  = [[5, 8, 1],[6, 7, 3],[4, 5, 9]]
result = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for i in range(len(file1)):
    for j in range(len(file1[0])):
        result[i][j] = file1[i][j] + file2[i][j]
for row in result:
    print(row)

"""
#--------------------------Problem 5--------------------------------
             Make a diamond using nested for loops
#-------------------------------------------------------------------
"""

y = int(input("How many carats is your diamond? "))
for i in range(y//2):
    print(" "*(y-i), "*"*(i*2+1))
for i in range(y//2, -1, -1):
    print(" "*(y-i), "*"*(i*2+1))



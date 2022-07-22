"""
VinUniversity
COMP1010 Introduction to Programming
Lab 06 - Week 6 - Objects, Lists and Sequences
by Phan Tuan Khoi V202100567

Group: 1
Date: Oct 28, 2021

Disclaimer: I certify that this assignment is my own work and that I have not copied in part or whole or
otherwise plagiarised the work of other students and/or persons.
"""
"""
#--------------------------Problem 1--------------------------------
#  List Operations in Python
#-------------------------------------------------------------------
"""
food = []
food.append("ham")
food.append("cheese")
food.append("ice scream")
food.remove("ham")
print(food)
"""
#--------------------------Problem 2--------------------------------
#  Past tense words
#-------------------------------------------------------------------
"""
past_tense_words = ["use", "rain", "open","admire", "learn", "switch", "advise", "cook", "accept", "add", "like", "move", "raise", "share"]
leng = len(past_tense_words)
for i in range(leng):
    if (past_tense_words[i].endswith("e")):
        past_tense_words[i] = past_tense_words[i] + "d"
    else:
        past_tense_words[i] = past_tense_words[i] + "ed"
print(past_tense_words)

"""
#--------------------------Problem 3--------------------------------
#  Searching and deleting a word in a given list
#-------------------------------------------------------------------
"""
usen = input("Enter a string:")
usde = input("Enter a word to delete:")
str_data = usen.split()
str_data.remove(usde)
print(("String after deletion: {}".format(" ".join(str_data))))


"""
#--------------------------Problem 4--------------------------------
#  Reverse the content of a given list
#-------------------------------------------------------------------
"""
oupt = []
secondouot = []
listnum = int(input("How many elements you want to enter?\n"))
print("Enter {} elements".format(listnum))
for i in range(listnum):
    usdt = int(input())
    oupt.append(usdt)
for j in range((listnum - 1), -1, -1):
    secondouot.append(oupt[j])

print("Reverse list: {}".format(secondouot))
"""
#--------------------------Problem 5--------------------------------
#  Nested list
#-------------------------------------------------------------------
"""
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original  Nested  list:")
print(list)
length = len(list)
for i in range(length):
    list[i]. remove(list[i][0])

print("After removing 1st column:")
print(list)

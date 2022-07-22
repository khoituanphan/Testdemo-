import random
a = input("Enter a word: ")
b = random.choice(a.upper())
c = random.randint(10, 30)
print("{}{}".format(b, c))

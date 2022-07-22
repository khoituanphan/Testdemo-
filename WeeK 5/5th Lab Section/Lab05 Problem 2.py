score = int(input("What is your percentage in class? "))
if 100> score > 85:
    print("You got an A!")
elif 84>score>70:
    print("You got a B!")
elif 69>score>55:
    print("You got a C!")
elif 54>score>40:
    print("You got a D!")
elif 39>score>0:
    print("Sorry, you got a F.")
else:
    print("Enter a valid number")
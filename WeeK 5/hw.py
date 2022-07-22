import math

a = int(input("Enter Alibubu's number: "))

if a>100:
    print("Your result {}".format(a))
else:
    if (a % 2)==1:
        b = math.log10(a)
        print("This is an odd number. The log base 10: {}".format(b))
    else:
        print("This is an even number")



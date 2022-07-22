
y = int(input("How many carats is your diamond? "))
for i in range(y//2):
    print(" "*(y-i), "*"*(i*2+1))
for i in range(y//2, -1, -1):
    print(" "*(y-i), "*"*(i*2+1))
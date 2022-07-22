def fizzbuzz(x):
    if x >= 0:
        if x ==0:
            print("")
        elif (x % 5 == 0) and (x % 3 == 0):
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
fizzbuzz(int(input("Enter a number: ")))
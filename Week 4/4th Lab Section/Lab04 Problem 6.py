# use a if the number is a multiple of 3 , otherwise use b
message = ""
for number in range(10):
    if (number % 3) == 0:
        message = message + "a"
    else:
        message = message + "b"
print(message)

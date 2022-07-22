my_tuple  = tuple(input("Enter a tuple elements separated by space: ").split(" "))
print("Your tuple is {}".format(my_tuple))
total = sum(map(int, my_tuple))
print("The sum of the elements in your tuple is {}.".format(total))

list = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print("Original  Nested  list: ")
print(list)
length = len(list)
for i in range(length):
    list[i]. remove(list[i][2])

print("After removing 3st column: ")
print(list)
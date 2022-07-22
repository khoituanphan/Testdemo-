list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original  Nested  list:")
print(list)
length = len(list)
for i in range(length):
    list[i]. remove(list[i][0])
print("After removing 1st column:")
print(list)
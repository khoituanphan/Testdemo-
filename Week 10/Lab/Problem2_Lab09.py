numbers_of_elements = int(input("Enter number of elements: "))
list_of_number = []
for i in range (numbers_of_elements):
    arr = int(input())
    list_of_number.append(arr)
    sorted_list = (sorted(list_of_number))
print("Sorted array:")
# for i in range (numbers_of_elements):
#     print(sorted_list[i], end=" ")
print(*sorted_list)



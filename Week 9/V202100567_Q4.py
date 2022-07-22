arr = [10, 7, 2, 13, 4, 52, 6, 17, 81, 49]
num = int(input("Enter first number: "))
def linear_search(arr, num_find):
    for i in range(len(arr)):

        if arr[i] == num_find:
            return i
    return "not found"
place = linear_search(arr, num) + 1
if linear_search(arr, num) == "not found":
    print("Number {} not found".format(num))
else:
    print("Number {} is found at position {}".format(num,place))
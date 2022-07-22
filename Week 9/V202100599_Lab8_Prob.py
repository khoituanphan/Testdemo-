def linear_search(arr, num_find):
    j = 0
    while j < len(arr):
        if arr[j] == num_find:
            print("Number", num_find, f'found at position {j+1}')
            break
        elif j == len(arr)-1:
            print(f"Number {num_find} not found")
            break
        else:
            j+=1
arr = [10, 7, 2, 13, 4, 52, 6, 17, 81, 49]
num = int(input("Enter first number: "))
linear_search(arr, num)
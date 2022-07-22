def combination(n, k):
    if k == 0 or k == n :
        return 1
    elif k == 1:
        return n
    else:
        return combination (n-1, k-1) + combination (n-1, k)

input = list(map(int, (input("Enter two numbers (n, k): ").split())))
n = input[0]
k = input[1]
result = combination(n, k)
print("Combination({}, {}) = {}".format(n,k, result ))


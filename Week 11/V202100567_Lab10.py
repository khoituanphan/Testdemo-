"""
VinUniversity
COMP1010  Introduction  to  Programming
Lab 10 - Week 11 -  Recursion and Recursive Algorithms
by Phan Tuan Khoi (V202100567)

Group: 1
Date: Dec 2, 2021

Disclaimer: I certify  that  this  assignment  is my own  work  and←↩
that I have  not  copied  in part or whole or  otherwise  plagiarised←↩
the  work of other  students  and/or  persons.
"""
"""
#--------------------------Problem 1--------------------------------
# Compute the number of k-combinations
#-------------------------------------------------------------------
"""
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
"""
#--------------------------Problem 2--------------------------------
# Compute the factorial of an positive integer using recursion
#-------------------------------------------------------------------
"""
def fact(n):
    if n ==1:
        return n
    else:
        return n*fact(n-1)
n = int(input("Enter an interger: "))
print("factorial({}) = {}! = {}".format(n,n, fact(n)))
"""
#--------------------------Problem 3--------------------------------
# Generating the Pascal triangle
#-------------------------------------------------------------------
"""
#iterative method
def pascal(n):
    pascal_triangle = []
    for i in range (n):
        l = len(pascal_triangle)
        if l == 0 or l == 1:
            pascal_triangle.append(1)
        elif l != 0:
            for j in range(l - 1):
                pascal_triangle[j] = pascal_triangle[j] + pascal_triangle[j +1]
            pascal_triangle.insert(0, 1)
        print(pascal_triangle)

pascal (6)

# recursive method
def pascal2(n):
    if n == 0:
        return []
    elif n == 1:
        print([1])
        return [1]
    else:
        pascal_triangle = [1]
        new_line = pascal2(n - 1)
        for i in range(len(new_line) - 1):
            pascal_triangle.append(new_line[i] + new_line[i + 1])
        pascal_triangle += [1]
        print(pascal_triangle)
    return pascal_triangle
pascal2 (6)
"""
#--------------------------Problem 4--------------------------------
# Producing the Fibonacci numbers out of Pascal’s triangle
#-------------------------------------------------------------------
"""
pascal_triangle_row = []
def pascal_triag(n):
    if n == 0:
        return []
    elif n == 1:
        pascal_triangle_row.append([1])
        return [1]
    else:
        new_row = [1]
        previous_row = pascal_triag(n-1)
        for i in range(len(previous_row)-1):
            new_row.append(previous_row[i] + previous_row[i+1])
        new_row += [1]
        pascal_triangle_row.append(new_row)
    return new_row

n = 10
pascal_triag(n)

for i in range(0, n):
    sum = 0
    for j in range(0, i + 1):
        if j <= i - j:
            sum += pascal_triangle_row[i - j][j]
    print(sum)



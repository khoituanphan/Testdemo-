first = float(input())
d =float(input())
n =float(input())
def find_term (n, first, d):
    last = first + (n-1)*d
    return(last)
def arithmetic_sum(n, first, last):

    return(n*(first + last)/2)
temp = find_term (n, first, d)
print(arithmetic_sum(n, first, temp))

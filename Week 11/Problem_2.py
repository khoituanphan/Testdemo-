def fact(n):
    if n ==1:
        return n
    else:
        return n*fact(n-1)
n = int(input("Enter an interger: "))
print("factorial({}) = {}! = {}".format(n,n, fact(n)))
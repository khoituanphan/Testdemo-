import math

a = int(input())
u = int(input())
v = int(input())

ans = math.log(u/v, a)
print (ans)
def quotient_rule (a,u,v):
    return math.log(u,a) - math.log(v,a)
print(quotient_rule(a,u,v))

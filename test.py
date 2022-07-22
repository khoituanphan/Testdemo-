import math 


a = int(input('Enter a: '))  
b = int(input('Enter b: '))  
c = int(input('Enter c: '))  
  

dis = b * b - 4 * a * c 
sqrt_val = math.sqrt(abs(dis)) 
      
if dis > 0: 
    sol1 = (-b + sqrt_val)/(2 * a)  
    sol2 = (-b - sqrt_val)/(2 * a)
    print("Equation has two root {0} and {1}".format(sol1, sol2))    
elif dis == 0:  
    sol3 = -b / (2 * a)
    print("Equation has one root {}".format(sol3))
  
else:  
    print("Equation has no root")  

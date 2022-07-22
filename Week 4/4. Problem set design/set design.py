def M_to_Ft(meter):
  Ft = meter * 3.2808
  return (Ft)
def Kg_to_Ibs(kg):
    Ibs = kg * 2.2046
    return (Ibs)
x = float(input("Your height: "))
y = float(input("Your weigh: "))
print("Your weigh is:  {}. Your heigh is: {}".format(Kg_to_Ibs(x), M_to_Ft(x)))

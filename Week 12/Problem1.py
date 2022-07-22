
class Apartment:
    apartment_name = "Sunshine Apartment"
    # Ali_Baba = "Phoenix Apartment"
    # James_Nguyen =  "Rainbow Apartment"
    # Mario = "Hanoi Apartment"
    # Wong = "HLT Apartment"

    def __init__(self,apartment,tenant, block, floor, unit):
        self.apartment = apartment
        self.tenant = tenant
        self.block = block
        self.floor = floor
        self.unit = unit
    def apart_name(self,name):
        self.name = name

    def display(self):
        print("'Welcome to '{}'!'".format(self.name))
        print("{} staying at Block {}, {}F-#{}.".format(self.tenant, self.block, self.floor, self.unit))

R1 = Apartment("Ali Baba", "B", 24, 1103)
R2 = Apartment("James Nguyen", "A", 15, 1120)
R3 = Apartment("Mario", "A", 2, 1250)
R4 = Apartment("Wong", "C", 2, 1010)

R1 = Apartment.apart_name("Phoenix Apartment")
R2 = Apartment.apart_name("Rainbow Apartment")
R3 = Apartment.apart_name("Hanoi Apartment")
R4 = Apartment.apart_name("HLT Apartment")

R1.display()
R2.display()
R3.display()
R4.display()
"""
VinUniversity
COMP1010  Introduction  to  Programming
Lab 11 - Week 12 -  Basic Object-Oriented Programming
by Phan Tuan Khoi (V202100567)

Group: 1
Date: Dec 9, 2021

Disclaimer: I certify  that  this  assignment  is my own  work  and←↩
that I have  not  copied  in part or whole or  otherwise  plagiarised←↩
the  work of other  students  and/or  persons.
"""
"""
#--------------------------Problem 1--------------------------------
# Tenant Information
#-------------------------------------------------------------------
"""
class Apartment:
    apartment_name = "Sunshine Apartment"

    def __init__(self, tenant, block, floor, unit):
        self.tenant = tenant
        self.block = block
        self.floor = floor
        self.unit = unit

    def display(self):
        print(f"{self.tenant} staying at Block {self.block}, {self.floor}F-#{self.unit}.")


R1 = Apartment("Ali Baba", "B", 24, 1103)
R2 = Apartment("James Nguyen", "A", 15, 1120)
R3 = Apartment("Mario", "A", 2, 1250)
R4 = Apartment("Wong", "C", 2, 1010)

print(f"Welcome to {Apartment.apartment_name}!")
R1.display()
R2.display()
R3.display()
R4.display()
"""
#--------------------------Problem 2--------------------------------
# Update the Tenant Information
#-------------------------------------------------------------------
"""
class Apartment:
    apartment_name = "Sunshine Apartment"

    def __init__(self, tenant, block, floor, unit):
        self.tenant = tenant
        self.block = block
        self.floor = floor
        self.unit = unit

    def apart_name(self, name):
        self.name = name

    def display(self):
        print("Welcome to '{}'!".format(self.name))
        print("{} staying at Block {}, {}F-#{}.".format(self.tenant, self.block, self.floor, self.unit))
        print()


R1 = Apartment("Ali Baba", "B", 24, 1103)
R2 = Apartment("James Nguyen", "A", 15, 1120)
R3 = Apartment("Mario", "A", 2, 1250)
R4 = Apartment("Wong", "C", 2, 1010)

R1.apart_name("Phoenix Apartment")
R2.apart_name("Rainbow Apartment")
R3.apart_name("Hanoi Apartment")
R4.apart_name("HLT Apartment")

R1.display()
R2.display()
R3.display()
R4.display()
"""
#--------------------------Problem 3--------------------------------
# Course Grade Information
#-------------------------------------------------------------------
"""
class Student:
    apartment_name = "Sunshine Apartment"

    def __init__(self, lab, midterm, final):
        self.lab = lab
        self.midterm = midterm
        self.final = final

    def cal_lab(self):
        self.lab = ((self.lab/80)*30, 1)

    def cal_midterm(self):
        self.midterm = ((self.midterm/60)*30, 1)

    def cal_final(self):
        self.final = ((self.final/70)*40, 1)

    def cal_total(self):
        total = round(self.cal_lab() + self.cal_midterm() + self.cal_final(), 1)
        return total
    def cal_grade(self):
        if self.total >= 80:
            self.grade = "A"
            return "A"
        if self.total < 80 and self.total >= 70:
            self.grade = "B"
            return "B"
        if self.total < 70 and self.total >= 60:
            self.grade = "C"
            return "c"
        if self.total < 60 and self.total >= 50:
            self.grade = "D"
            return "D"
        else:
            self.grade = "F"
            return "F"
    def __str__(self):
        return ("{}   {}   {}   {}%   {}".format(self.lab, self.midterm, self.final, self.grade))

student1 = Student(71, 53, 70)
student2 = Student(64, 60, 61)
student3 = Student(47, 35, 66)
student4 = Student(28, 37, 56)
student5 = Student(32, 31, 34)

list_std = [student1, student2, student3, student4, student5]
print("---------------Course Grade---------------")
print("  Lab   Midterm   Final   Total   Grade")
print(" (30%)   (30%)    (40%)   (100%) ")
for std in list_std:
    std.cal_lab()
    std.cal_midterm()
    std.cal_final()
    std.cal_total()
    std.cal_grade()
    print(std.__str__())
print("------------------------------------------")

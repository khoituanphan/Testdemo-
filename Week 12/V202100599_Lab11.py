"""
VinUniversity
COMP1010  Introduction  to  Programming
Lab 11 - Week 11 - Variables, Operators and Functions
by Cao Hai Lam (V202100599)

Group: 1
Date: Dec. 09th, 2021

Disclaimer: I certify  that  this  assignment  is my own  work  and that I have  not  copied  in part or whole or  otherwise  plagiarised the  work of other  students  and/or  persons.
"""

"""
#--------------------------Problem 1--------------------------------
#                     Tenant Information
#-------------------------------------------------------------------
"""
class Apartment:
    def __init__(self, ten, blo, flo, u):
        self.tenant = ten
        self.block = blo
        self.floor = flo
        self.unit = u
    def func(self):
        print(self.tenant, "staying at Block", self.block+",", self.floor+"F-#"+self.unit+".")
print ("Welcome to Sunshine Apartment!")
R1 = Apartment("Ali Baba", "B", "24", "1103")
R1.func()
R2 = Apartment("James Nguyen", "A", "15", "1120")
R2.func()
R3 = Apartment("Mario", "A", "2", "1250")
R3.func()
R4 = Apartment("Wong", "C", "2", "1010")
R4.func()

"""
#--------------------------Problem 2--------------------------------
#                  Update the Tenant Information
#-------------------------------------------------------------------
"""
class Apartment:
    def __init__(self, ten, blo, flo, u):
        self.tenant = ten
        self.block = blo
        self.floor = flo
        self.unit = u
    def apart_name(self, apa):
        self.apartment = apa
        print("Welcome to '", self.apartment+"'!")
    def func(self):
        print(self.tenant, "staying at Block", self.block+",", self.floor+"F-#"+self.unit+".")
        print()
R1 = Apartment("Ali Baba", "B", "24", "1103")
R1.apart_name("Phoenix Apartment")
R1.func()
R2 = Apartment("James Nguyen", "A", "15", "1120")
R2.apart_name("Rainbow Apartment")
R2.func()
R3 = Apartment("Mario", "A", "2", "1250")
R3.apart_name("Hanoi Apartment")
R3.func()
R4 = Apartment("Wong", "C", "2", "1010")
R4.apart_name("HLT Apartment")
R4.func()

"""
#--------------------------Problem 3--------------------------------
#                  Course Grade Information
#-------------------------------------------------------------------
"""
class Students:
    def __init__(self, lab, midterm, final):
        self.lab = lab
        self.midterm = midterm
        self.final = final
    def cal_lab(self):
        percent_lab = self.lab*3/8
        return percent_lab
    def cal_midterm(self):
        percent_mid = self.midterm*3/6
        return percent_mid
    def cal_final(self):
        percent_final = self.final*4/8
        return percent_final
    def cal_total(self):
        total = self.cal_lab() + self.cal_midterm() + self.cal_final()
        return total
    def cal_grade(self):
        total = self.cal_total()
        if total >= 80:
            grade = "A"
        elif total >= 70:
            grade = "B"
        elif total >= 60:
            grade = "C"
        elif total >= 50:
            grade = "D"
        else:
            grade = "F"
        return grade
    def string(self):
        print("{:,.1f}".format(self.cal_lab())+"   ", "{:,.1f}".format(self.cal_midterm())+"  ", "{:,.1f}".format(self.cal_final())+"  ", "{:,.1f}".format(self.cal_total())+"%  ", self.cal_grade())

print("""
------------Course Grade------------
Lab   Midterm  Final  Total  Grade
(30%)  (40%)   (40%)  (100%)
""")

std1 = Students(71, 53, 70)
std2 = Students(64, 60, 61)
std3 = Students(47, 35, 66)
std4 = Students(28, 37, 56)
std5 = Students(32, 31, 34)

std = [std1, std2, std3, std4, std5]
for i in std:
    i.cal_lab()
    i.cal_midterm()
    i.cal_final()
    i.cal_total()
    i.cal_grade()
    i.string()

print("------------------------------------")
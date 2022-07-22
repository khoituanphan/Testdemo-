"""
VinUniversity
COMP1010 Introduction to Programming
Lab 12 - Week 13 - Getting started with Python
by Duong Nguyen Viet (V202100414)

Group: 2
Date: Dec 16, 2021

Disclaimer: I certify that this assignment is my own work and that I have not copied in part or whole or
otherwise plagiarised the work of other students and/or persons.
"""

"""
#--------------------------Problem1--------------------------------
#            Create a super class and sub-classes
#-------------------------------------------------------------------
"""








class Vinuni:
    def __init__(self, ID, fname, lname, category):
        self.ID = ID
        self.fname = fname
        self.lname = lname
        self.category = category
    def disp_info(self):
        print('''Name: {}{}
Category: {}'''.format(self.lname, self.fname, self.category))

class Student(Vinuni):
    def __init__(self, ID, fname, lname, category):
        Vinuni.__init__(self, ID, fname, lname, category)
    def disp_id(self):
        print('Student ID:{}\n'.format(self.ID))

class Staff(Vinuni):
    def __init__(self, ID, fname, lname, category):
        Vinuni.__init__(self, ID, fname, lname, category)
    def disp_id(self):
        print('Staff ID:{}\n'.format(self.ID))

student1 = Student(20115415, ' James', 'Park', 'Student')
student1.disp_info()
student1.disp_id()

student2 = Student(20202419, ' Baba', 'Ali', 'Student')
student2.disp_info()
student2.disp_id()

staff1 = Staff(19114451, ' Wang', 'Lee', 'Professor')
staff1.disp_info()
staff1.disp_id()

staff2 = Staff(19124289, ' Anh Tu', 'Nguyen', 'Admin')
staff2.disp_info()
staff2.disp_id()



"""
#--------------------------Problem2--------------------------------
#                 The base class constructor
#-------------------------------------------------------------------
"""





class Person:
    def __init__(self, name, age, birth_place):
        self.name = name
        self.age = age
        self.birth_place = birth_place
    def birth_year(self):
        return 2021-self.age
    def __str__(self):
        return '''{} was born in {} in {}.
{}'''.format(self.name, self.birth_place, self.birth_year(), self.birth_year())

class Student(Person):
    def __init__(self, name, age, birth_place, gender):
        Person.__init__(self, name, age, birth_place)
        self.gender = gender
    
    def __str__(self):
        return '{} was born in {} in {}. {} is {} years old this year.'.format(self.name, self.birth_place,
                                                                              self.birth_year(), self.gender, self.age)
person1 = Person('Richard', 22, 'London')
print(person1)

player1 = Student('Fiona', 35, 'Seoul', 'She')
print(player1)

player2 = Student('Mike', 45, 'Washington', 'He')
print(player2)



"""
#--------------------------Problem3--------------------------------
#    Inheritance in Python: Finding the area of the triangle
#-------------------------------------------------------------------
"""


from math import sqrt
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
class Triangle(Polygon):
    def __init__(self, no_of_sides):
        Polygon.__init__(self, no_of_sides)

    def findArea(self):
        p = sum(self.sides)/2
        area = sqrt(p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2]))
        print(f'The area of the triangle is {area}')

triangle = Triangle(3)
triangle.inputSides()
triangle.dispSides()
triangle.findArea()





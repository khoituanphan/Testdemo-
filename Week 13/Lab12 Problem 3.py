from math import sqrt
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in
range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
class Triangle(Polygon):
    def __init__(self, no_of_sides):
        Polygon.__init__(self, no_of_sides)

    def findArea(self):
         a = sum(self.sides)/2
         area = sqrt(a * (a - self.sides[0]) * (a - self.sides[1]) * (a - self.sides[2]))
         print("The area of the triangle is {}".format(area))


triangle = Triangle(3)
triangle.inputSides()
triangle.dispSides()
triangle.findArea()


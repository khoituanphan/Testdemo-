class Person:
    def __init__(self, name, age, birth_place):
        self.name = name
        self. age = age
        self.birth_place = birth_place
    def birth_year(self):
        print(2021 - self.age)
    def __str__(self):
        print("{} was born in {} in {}.".format(self.name, self.birth_place, (2021 - self.age)))

class Student(Person):
    def __init__(self, name, age, birth_place, Sex):
        super().__init__(name, age, birth_place)
        self.Sex = Sex

    def __str__(self):
        if self.Sex == "Female":
            print("{} was born in {} in {}. She is {} years old this year.".format(self.name, self.birth_place, (2021 - self.age), self.age))
        else:
            print("{} was born in {} in {}. He is {} years old this year.".format(self.name, self.birth_place, (2021 - self.age),
                                                                                      self.age))


person1 = Person("Richard", 22, "London")
person1.__str__()
person1.birth_year()

player1 = Student("Fiona", 35, "Seoul", "Female")
player1.__str__()

player2 = Student("Mike", 45, "Washington", "Male")
player2.__str__()
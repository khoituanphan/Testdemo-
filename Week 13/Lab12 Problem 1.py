class VinUni:
    def __init__(self, ID,fname, lname, category):
        self.ID = ID
        self.fname = fname
        self.lname = lname
        self.category = category

    def disp_info(self):
        print("Name: {} {}".format(self.lname, self.fname))
class Student (VinUni):
    def __init__(self,ID, lname, fname, category):
        super().__init__(ID, lname, fname, category)

    def disp_ID(self):
        print("Category: {}".format(self.category))
        print("Student ID:{}".format(self.ID))
class Staff (VinUni):
    def __init__(self,ID, lname, fname, category):
        super().__init__(ID, lname, fname, category)

    def disp_ID(self):
        print("Category: {}".format(self.category))
        print("Staff ID:{}".format(self.ID))

student1 = Student("20115415","James","Park", "Student")
student1.disp_info()
student1.disp_ID()
print()
student2 = Student("20202419","Ali","Baba", "Student")
student2.disp_info()
student2.disp_ID()
print()
staff1 = Staff("19114451","Wang","Lee", "Professor")
staff1.disp_info()
staff1.disp_ID()
print()
staff1 = Staff("19124289","Anh Tu","Nguyen", "Admin")
staff1.disp_info()
staff1.disp_ID()

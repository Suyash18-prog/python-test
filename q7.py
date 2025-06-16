class Student:
    def __init__(self,name, age, marks):
        self.name=name
        self.age =age
        self.marks=marks

    def get_info(self):
        print(f"Name = {self.name}")
        print(f"age = {self.age}")
        print(f"marks = {self.marks}")


    def check_pass(self):
        if self.marks>=40:
            print(f"{self.name} has been passed")
        else :
            print(f"{self.name} has been failed")

Student1 = Student("Suyash",20,44)
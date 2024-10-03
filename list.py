class Student:
    def display(self):
        return f"Name: {self.name}, Age: {self.age}"
class ab:
    def details(self):
        students=[]
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        student=Student()
        student.name=name
        student.age=age
        students.append(student)
        for student in students:
                    print(student.display())

m=ab()
m.details()        


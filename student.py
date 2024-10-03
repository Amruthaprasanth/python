class Student:
    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class Menu:
        students = []
        def add(self):
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = input("Enter student's grade: ")
            student = Student()
            student.name = name
            student.age = age
            student.grade = grade
            Menu.students.append(student)
           
        def display(self):
             if len(Menu.students) == 0:
                print("No students added")
             else:
                  for student in Menu.students:
                    print(student.display_details())
        def run(self):
            while True:
                print("1.add student")
                print("2.display students")
                print("3.exit")
                ch=input("enter choice:")
                if ch=='1':
                    self.add()
                elif ch=='2':
                    self.display()
                elif ch=='3':
                    print("exit")
                    break
                else:
                    print("wrong option")


m=Menu()
m.run()
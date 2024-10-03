class Student:
    def __init__(self, name, rnum, marks):
        self.name =name
        self.rnum =rnum
        self.marks =marks

    def updateMarks(self, new_marks):
        if len(new_marks) == 3:
            self.marks = new_marks
        else:
            print("Please provide exactly three marks.")

    def averageMarks(self):
        return sum(self.marks) / len(self.marks)

    def studentInfo(self):
        return f"Name: {self.name}, Roll Number: {self.rnum}, Marks: {self.marks}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def addStudent(self):
        name = input("Enter the student's name: ")
        roll_number = input("Enter the roll number: ")
        marks = []
        for i in range(1, 4):
            mark = float(input(f"Enter marks for subject {i}: "))
            marks.append(mark)
        new_student = Student(name, roll_number, marks)
        self.students.append(new_student)
        print("Student added successfully.")

    def viewStudents(self):
        if not self.students:
            print("No students available.")
            return
        for student in self.students:
            print(student.studentInfo())

    def updateStudentMarks(self):
        roll_number = input("Enter the roll number of the student to update marks: ")
        for student in self.students:
            if student.rnum == roll_number:
                new_marks = []
                for i in range(1, 4):
                    mark = float(input(f"Enter new marks for subject {i}: "))
                    new_marks.append(mark)
                student.updateMarks(new_marks)
                print("Marks updated successfully.")
                return
        print("Student not found.")

    def calculateAverageMarks(self):
        roll_number = input("Enter the roll number of the student: ")
        for student in self.students:
            if student.rnum == roll_number:
                avg = student.averageMarks()
                print(f"Average marks for {student.name}: {avg:.2f}")
                return
        print("Student not found.")

    def run(self):
        while True:
            print("\nStudent Management System")
            print("1. Add a new student")
            print("2. View all students")
            print("3. Update marks of a student")
            print("4. Calculate average marks of a student")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                self.addStudent()
            elif choice == '2':
                self.viewStudents()
            elif choice == '3':
                self.updateStudentMarks()
            elif choice == '4':
                self.calculateAverageMarks()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please try again.")
sms = StudentManagementSystem()
sms.run()
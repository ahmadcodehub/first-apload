# =========================
# STUDENT CLASS (DATA ONLY)
# =========================

class Student:
    def __init__(self, id, name, age, grade, semester):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.semester = semester

    def display_info(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)
        print("Semester:", self.semester)
        print("----------------------")


# =========================
# MANAGEMENT SYSTEM (LOGIC)
# =========================

class StudentManagementSystem:
    def __init__(self):
        # list to store all students
        self.students = []

    # ADD STUDENT
    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    # VIEW ALL STUDENTS
    def view_students(self):
        if len(self.students) == 0:
            print("No students found.")
        else:
            for student in self.students:
                student.display_info()

    # SEARCH STUDENT BY NAME
    def search_student(self, name):
        for student in self.students:
            if student.name == name:
                print("Student Found:")
                student.display_info()
                return student
        print("Student not found.")
        return None

    # DELETE STUDENT BY NAME
    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print("Student deleted successfully!")
                return
        print("Student not found.")


# =========================
# MAIN PROGRAM (RUN CODE)
# =========================

# create system object
sms = StudentManagementSystem()

# create students
s1 = Student(1, "ahmd khan ", 20, "A", 4)
s2 = Student(2, "hareem batool", 22, "B", 6)

# add students to system
sms.add_student(s1)
sms.add_student(s2)

# view all students
print("\nALL STUDENTS:")
sms.view_students()

# search student
print("\nSEARCH RESULT:")
sms.search_student("ahmd khan ")

# delete student
print("\nDELETE OPERATION:")
sms.delete_student("hareem batool =")

# view again after delete
print("\nAFTER DELETION:")
sms.view_students()
# =========================
# STUDENT CLASS
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
# MANAGEMENT SYSTEM
# =========================

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.load_from_file()   # 🔥 load data when program starts

    # ---------------- LOAD FROM FILE ----------------
    def load_from_file(self):
        try:
            with open("students.txt", "r") as file:
                lines = file.readlines()[1:]  # skip header

                for line in lines:
                    data = line.strip().split(",")
                    student = Student(data[0], data[1], data[2], data[3], data[4])
                    self.students.append(student)

        except FileNotFoundError:
            pass

    # ---------------- SAVE TO FILE ----------------
    def save_to_file(self):
        with open("students.txt", "w") as file:
            file.write("ID,Name,Age,Grade,Semester\n")
            for s in self.students:
                file.write(f"{s.id},{s.name},{s.age},{s.grade},{s.semester}\n")

    # ---------------- ADD ----------------
    def add_student(self):
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")
        semester = input("Enter Semester: ")

        student = Student(id, name, age, grade, semester)
        self.students.append(student)

        self.save_to_file()
        print("Student added successfully!")

    # ---------------- VIEW ----------------
    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for s in self.students:
            s.display_info()

    # ---------------- SEARCH ----------------
    def search_student(self):
        name = input("Enter name to search: ")

        for s in self.students:
            if s.name == name:
                print("Student Found:")
                s.display_info()
                return

        print("Student not found.")

    # ---------------- DELETE ----------------
    def delete_student(self):
        name = input("Enter name to delete: ")

        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                self.save_to_file()
                print("Student deleted successfully!")
                return

        print("Student not found.")


# =========================
# MENU SYSTEM
# =========================

sms = StudentManagementSystem()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sms.add_student()

    elif choice == "2":
        sms.view_students()

    elif choice == "3":
        sms.search_student()

    elif choice == "4":
        sms.delete_student()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
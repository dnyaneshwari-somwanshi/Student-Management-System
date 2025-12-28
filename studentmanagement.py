import json
import os

# ---------------- Student Class ----------------
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }


# ---------------- Manager Class ----------------
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.students = json.load(file)

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        student_id = input("Enter Student ID: ")

        if student_id in self.students:
            print("❌ Student ID already exists!")
            return

        name = input("Enter Name: ")
        grade = input("Enter Grade: ")

        student = Student(student_id, name, grade)
        self.students[student_id] = student.to_dict()
        self.save_data()

        print("✅ Student added successfully!")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")

        if student_id not in self.students:
            print("❌ Student not found!")
            return

        name = input("Enter new Name: ")
        grade = input("Enter new Grade: ")

        self.students[student_id]["name"] = name
        self.students[student_id]["grade"] = grade
        self.save_data()

        print("✅ Student updated successfully!")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")

        if student_id in self.students:
            del self.students[student_id]
            self.save_data()
            print("✅ Student deleted successfully!")
        else:
            print("❌ Student not found!")

    def list_students(self):
        if not self.students:
            print("⚠ No students available.")
            return

        print("\n📋 Student Records")
        print("-" * 30)
        for student in self.students.values():
            print(f"ID: {student['id']} | Name: {student['name']} | Grade: {student['grade']}")
        print("-" * 30)


# ---------------- CLI Menu ----------------
def main():
    manager = StudentManager()

    while True:
        print("""
====== Student Management System ======
1. Add Student
2. Update Student
3. Delete Student
4. List Students
5. Exit
======================================
        """)

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.update_student()
        elif choice == "3":
            manager.delete_student()
        elif choice == "4":
            manager.list_students()
        elif choice == "5":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
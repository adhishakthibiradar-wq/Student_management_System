import json
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except:
    students = []

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        print("\n------ Add Student ------")

        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        marks = input("Enter Marks: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "marks": marks
        }

        students.append(student)
        save_data()
        print("\nStudent Added Successfully!")

    # View Students
    elif choice == "2":
        print("\n------ Student List ------")

        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print("----------------------------")
                print(f"Student ID : {student['id']}")
                print(f"Name       : {student['name']}")
                print(f"Age        : {student['age']}")
                print(f"Course     : {student['course']}")
                print(f"Marks      : {student['marks']}")
            print("----------------------------")

    # Search Student
    elif choice == "3":
        print("\n------ Search Student ------")

        search_id = input("Enter Student ID to search: ")

        found = False

        for student in students:
            if student["id"] == search_id:
                print("\nStudent Found!")
                print(f"Student ID : {student['id']}")
                print(f"Name       : {student['name']}")
                print(f"Age        : {student['age']}")
                print(f"Course     : {student['course']}")
                print(f"Marks      : {student['marks']}")
                found = True
                break

        if not found:
            print("Student not found.")

    # Update Student
    elif choice == "4":
        print("\n------ Update Student ------")

        update_id = input("Enter Student ID to update: ")

        found = False

        for student in students:
            if student["id"] == update_id:
                print("\nStudent Found!")

                student["name"] = input("Enter New Name: ")
                student["age"] = input("Enter New Age: ")
                student["course"] = input("Enter New Course: ")
                student["marks"] = input("Enter New Marks: ")

                save_data()
                print("\nStudent Updated Successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # Delete Student
    elif choice == "5":
        print("\n------ Delete Student ------")

        delete_id = input("Enter Student ID to delete: ")

        found = False

        for student in students:
            if student["id"] == delete_id:
                students.remove(student)
                save_data()
                print("\nStudent Deleted Successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == "6":
        print("\nThank you for using Student Management System!")
        break

    # Invalid Choice
    else:
        print("\nInvalid Choice! Please try again.")
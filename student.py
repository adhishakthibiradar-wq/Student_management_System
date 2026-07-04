import sqlite3
def get_connection():
    return sqlite3.connect("students.db")

def add_student():
    connection = get_connection()
    cursor = connection.cursor()

    student_id = input("Enter Student ID: ")

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    if cursor.fetchone():
        print("Student ID already exists!")
        connection.close()
        return

    while True:
        name = input("Enter Student Name: ").strip()

        if name:
            break

        print("Name cannot be empty.")
        
    while True:
        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid age.")
            
    while True:
        course = input("Enter Course: ").strip()

        if course:
            break

        print("Course cannot be empty.")

    while True:
        try:
            marks = int(input("Enter Marks: "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
            else:
                break
        except ValueError:
            print("Please enter a valid marks.")

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
        (student_id, name, age, course, marks)
    )

    connection.commit()
    connection.close()

    print("Student Added Successfully!")

def view_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if len(students) == 0:
        print("\nNo students found.")
    else:
        print("\n------ Student List ------")

        for student in students:
            print("----------------------------")
            print(f"Student ID : {student[0]}")
            print(f"Name       : {student[1]}")
            print(f"Age        : {student[2]}")
            print(f"Course     : {student[3]}")
            print(f"Marks      : {student[4]}")

    connection.close()
def search_student():
    connection = get_connection()
    cursor = connection.cursor()

    search_id = input("Enter Student ID: ")

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (search_id,)
    )

    student = cursor.fetchone()

    if student:
        print("\n------ Student Found ------")
        print(f"Student ID : {student[0]}")
        print(f"Name       : {student[1]}")
        print(f"Age        : {student[2]}")
        print(f"Course     : {student[3]}")
        print(f"Marks      : {student[4]}")
    else:
        print("Student not found.")

    connection.close()

def update_student():
    connection = get_connection()
    cursor = connection.cursor()

    update_id = input("Enter Student ID to update: ")

    cursor.execute("SELECT * FROM students WHERE id = ?", (update_id,))
    student = cursor.fetchone()

    if student:

        print("\nStudent Found!")

        while True:
            name = input("Enter New Name: ").strip()
            if name:
                break
            print("Name cannot be empty.")

        while True:
            try:
                age = int(input("Enter New Age: "))
                if age < 0:
                    print("Age must be a positive integer.")
                else:
                    break
            except ValueError:
                print("Please enter a valid age.")

        while True:
            course = input("Enter New Course: ").strip()
            if course:
                break
            print("Course cannot be empty.")

        while True:
            try:
                marks = int(input("Enter New Marks: "))
                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100.")
                else:
                    break
            except ValueError:
                print("Please enter a valid marks.")

        cursor.execute("""
            UPDATE students
            SET name = ?, age = ?, course = ?, marks = ?
            WHERE id = ?
        """, (name, age, course, marks, update_id))

        connection.commit()

        print("\nStudent Updated Successfully!")

    else:
        print("Student not found.")

    connection.close()

def delete_student():
    connection = get_connection()
    cursor = connection.cursor()

    delete_id = input("Enter Student ID to delete: ")

    cursor.execute("SELECT * FROM students WHERE id = ?", (delete_id,))
    student = cursor.fetchone()

    if student:

        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (delete_id,)
        )

        connection.commit()

        print("\nStudent Deleted Successfully!")

    else:
        print("Student not found.")

    connection.close()
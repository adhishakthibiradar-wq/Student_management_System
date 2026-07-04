from student import *

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
        add_student()
        
    # View Students
    elif choice == "2":
        view_students()

    # Search Student
    elif choice == "3":
        search_student()

    # Update Student
    elif choice == "4":
        update_student()

    # Delete Student
    elif choice == "5":
        delete_student()

    # Exit
    elif choice == "6":
        print("\nThank you for using Student Management System!")
        break

    # Invalid Choice
    else:
        print("\nInvalid Choice! Please try again.")
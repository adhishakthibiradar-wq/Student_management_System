from student import *

while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Show Topper")
    print("8. Average Marks")
    print("9. Sort Students by Marks")
    print("10. Search Student by Name")
    print("11. Export Students to CSV")
    print("12. Exit")

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
        delete_students()

    # Count Students
    elif choice == "6":
        count_students()

    # show topper 
    elif choice == "7":
        show_topper()

    # Average Marks
    elif choice == "8":
        average_marks()
    
    # Sort student by marks
    elif choice == "9":
        sort_students_by_marks()

    # Search student by name
    elif choice == "10":
        search_student_by_name()
    
    # Export students to csv
    elif choice == "11":
        export_to_csv()

    # Exit
    elif choice == "12":
        print("\nThank you for using Student Management System!")
        break

    # Invalid Choice
    else:
        print("\nInvalid Choice! Please try again.")
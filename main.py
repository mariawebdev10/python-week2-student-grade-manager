from student import Student

students = []

while True:
    print("\n===== Student Grade Manager =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))

        student = Student(name, roll, marks)
        students.append(student)

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\n===== Student List =====")
            for student in students:
                student.display()

    elif choice == "3":
        print("Thank you for using Student Grade Manager.")
        break

    else:
        print("Invalid choice! Please try again.")
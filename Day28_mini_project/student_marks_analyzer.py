marks = []
names = []


for i in range(5):
    student_name = input("Enter the name of student: ")
    student_mark = int(input("Enter the marks of student: "))

    names.append(student_name)
    marks.append(student_mark)

while True:

    print("""
===== Student Marks Analyzer =====

1. Display students
2. Highest mark
3. Lowest mark
4. Average mark
5. Remove student
6. Sort marks
7. Exit
""")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("\nStudents:")
        for i in range(len(names)):
            print(names[i], "-", marks[i])

    elif choice == 2:
        print("Highest mark:", max(marks))

    elif choice == 3:
        print("Lowest mark:", min(marks))

    elif choice == 4:
        average = sum(marks) / len(marks)
        print("Average mark:", average)

    elif choice == 5:
        name = input("Enter the name to remove: ")

        if name in names:
            index = names.index(name)

            names.pop(index)
            marks.pop(index)

            print("Student removed successfully.")
        else:
            print("Student not found.")

    elif choice == 6:
        marks.sort()
        print("Sorted marks:", marks)

    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

# ===============================
# STUDENT PERFORMANCE SYSTEM
# ===============================

students = []


# -------------------------------
# FUNCTION: Calculate Average
# -------------------------------
def calculate_average(grades):
    return sum(grades) / len(grades)


# -------------------------------
# FUNCTION: Classify Performance
# -------------------------------
def classify_student(avg):
    if avg >= 85:
        return "Excellent"
    elif avg >= 70:
        return "Good"
    else:
        return "Needs Improvement"


# -------------------------------
# FUNCTION: Add Student
# -------------------------------
def add_student():
    name = input("Enter student name: ").strip()

    # Prevent duplicate names
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student already exists!\n")
            return

    age = int(input("Enter student age: "))

    grades = []
    for i in range(1, 4):
        grade = float(input(f"Enter grade {i}: "))
        grades.append(grade)

    student = {
        "name": name,
        "age": age,
        "grades": grades
    }

    students.append(student)
    print("Student added successfully!\n")


# -------------------------------
# FUNCTION: View Students
# -------------------------------
def view_students():
    if not students:
        print("No students available.\n")
        return

    for student in students:
        avg = calculate_average(student["grades"])
        performance = classify_student(avg)

        print("===================================")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grades: {student['grades']}")
        print(f"Average: {round(avg, 2)}")
        print(f"Performance: {performance}")
        print("===================================\n")


# -------------------------------
# FUNCTION: Search Student
# -------------------------------
def search_student():
    name = input("Enter student name to search: ").strip()
    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            avg = calculate_average(student["grades"])
            performance = classify_student(avg)

            print("\nStudent Found:")
            print("-----------------------------------")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grades: {student['grades']}")
            print(f"Average: {round(avg, 2)}")
            print(f"Performance: {performance}")
            print("-----------------------------------\n")

            found = True
            break

    if not found:
        print("Student not found.\n")


# ===============================
# MAIN MENU LOOP
# ===============================

while True:
    print("====== STUDENT SYSTEM MENU ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting system. Goodbye 👋")
        break
    else:
        print("Invalid option. Try again.\n")

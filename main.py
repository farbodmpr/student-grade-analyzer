
# Student Grade Analyzer

# Store student information
students = []

# Store all student names
student_names = []

# Store all grades
all_grades = []

# Register 5 students
registered = 0

while registered < 5:

    print("\nStudent Number:", registered + 1)

    name = input("Enter student name: ").strip().title()

    # Check for empty names
    if name == "":
        print("Name cannot be empty.")
        continue

    grades = []

    # Get 3 valid grades for each student
    while len(grades) < 3:

        grade = input("Enter grade: ").strip()

        # Check whether grade is a valid number
        if grade.replace(".", "", 1).isdigit() is False:
            print("Invalid grade. Enter a number.")
            continue

        grade = float(grade)

        # Check grade range
        if grade < 0 or grade > 20:
            print("Grade must be between 0 and 20.")
            continue

        grades.append(grade)

    # Register student after all grades are valid
    students.append([name, grades])
    student_names.append(name)
    all_grades.extend(grades)

    registered += 1

# Analyze student grades
print("\n========== STUDENT REPORT ==========")

total_class = 0

for student in students:

    name = student[0]
    grades = student[1]

    total = 0

    for grade in grades:
        total += grade

    average = total / len(grades)

    total_class += average

    print("\nName:", name)
    print("Grades:", grades)
    print("Average:", round(average, 2))

    if average >= 10:
        print("Status: Passed")
    else:
        print("Status: Failed")

# Calculate class average
if len(students) > 0:

    class_average = total_class / len(students)

    print("\nClass Average:", round(class_average, 2))

else:
    print("\nNo student was registered.")

# Find highest and lowest grades
if len(all_grades) > 0:

    highest = all_grades[0]
    lowest = all_grades[0]

    for grade in all_grades:

        if grade > highest:
            highest = grade

        if grade < lowest:
            lowest = grade

    print("Highest Grade:", highest)
    print("Lowest Grade:", lowest)

# Search for a student
search_name = input("\nEnter a name to search: ").strip().lower()

if search_name == "":
    print("Search name cannot be empty.")

else:

    found = False

    for student in students:

        if search_name in student[0].lower():

            print("Student found:", student[0])
            print("Grades:", student[1])

            found = True
            break

    if found is False:
        print("Student not found.")

# Sort student names
student_names.sort()

print("\n========== SORTED STUDENT NAMES ==========")

for name in student_names:
    print(name)

print("\nProgram finished.")

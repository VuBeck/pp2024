def input_student():
    number_student = int(input("Enter number of students: "))
    students = []
    for i in range(number_student):
        student_id = int(input("Enter student ID: "))
        student_name = str(input("Enter student name: "))
        student_dob = str(input("Enter student date of birth (DD/MM/YYYY): "))
        student = (student_id, student_name, student_dob)
        students.append(student)
    return students, number_student


def input_course():
    number_course = int(input("Enter number of courses: "))
    courses = []
    for i in range(number_course):
        course_id = int(input("Enter course ID: "))
        course_name = str(input("Enter course name: "))
        course = (course_id, course_name)
        courses.append(course)
    return courses, number_course


def input_mark(students, courses):
    course_id = int(input("Enter course ID that you want to input marks for: "))
    selected_course = None
    for course in courses:
        if course[0] == course_id:
            selected_course = course
            break
    if selected_course is None:
        print("Error! Please enter a valid course.")
        return

    student_mark = {}
    for student in students:
        mark = float(input(f"Enter mark for {student[1]}: "))
        student_mark[student[1]] = mark

    return selected_course, student_mark


def course_list(courses):
    print("Course information:")
    for course in courses:
        print(f"Course ID: {course[0]} --- Course name: {course[1]}")


def student_list(students):
    print("Student information:")
    for student in students:
        print(f"Student ID: {student[0]} --- Name: {student[1]} --- Dob: {student[2]}")


def student_mark_list(students, courses):
    print("Available courses:")
    for index, course in enumerate(courses):
        print(f"{index + 1}. Course ID: {course[0]} --- Course name: {course[1]}")

    course_choice = int(input("Enter the number of the course to see marks: "))
    if course_choice < 1 or course_choice > len(courses):
        print("Error! Please enter a valid course number.")
        return

    selected_course = courses[course_choice - 1]
    student_marks = None
    for course_id, marks in student_mark.items():
        if course_id == selected_course[0]:
            student_marks = marks
            break

    if student_marks is None:
        print(f"No marks found for course: {selected_course[1]}")
        return

    print(f"Marks for course: {selected_course[1]}")
    for student_name, mark in student_marks.items():
        print(f"Name: {student_name} --- Mark: {mark}")


# Main
students, number_student = input_student()
courses, number_course = input_course()
selected_course = None
student_mark = {}

while True:
    print("-------Menu------")
    print("1. Input marks for a course")
    print("2. List of courses")
    print("3. List of students")
    print("4. Student marks of a course")
    print("5. Total number of students")
    print("6. Total number of courses")
    print("7. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        output = input_mark(students, courses)
        if output is not None:
            selected_course, student_mark = output
    elif choice == 2:
        course_list(courses)
    elif choice == 3:
        student_list(students)
    elif choice == 4:
        if selected_course is not None:
            student_mark_list(students, courses)
        else:
            print("No course selected. Please select a course first.")
    elif choice == 5:
        print(f"Total number of students: {number_student}")
    elif choice == 6:
        print(f"Total number of courses: {number_course}")
    elif choice == 7:
        break
    else:
        print("Error! Please enter a valid number.")
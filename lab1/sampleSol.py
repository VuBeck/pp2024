def input_students():
    num_students = int(input("Enter the number of students: "))
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth: ")
        student = (student_id, student_name, student_dob)
        students.append(student)
    return students

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course = (course_id, course_name)
        courses.append(course)
    return courses

def input_marks(students, courses):
    course_id = input("Enter the course ID: ")
    selected_course = None
    for course in courses:
        if course[0] == course_id:
            selected_course = course
            break
    if selected_course is None:
        print("Course not found!")
        return
    marks = {}
    for student in students:
        mark = float(input(f"Enter the mark for student {student[1]}: "))
        marks[student[0]] = mark
    return selected_course, marks

def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def show_student_marks(selected_course, marks):
    print(f"Marks for course {selected_course[1]}:")
    for student_id, mark in marks.items():
        print(f"Student ID: {student_id}, Mark: {mark}")

# Main program
students = input_students()
courses = input_courses()

while True:
    print("\nMenu:")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a course")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        result = input_marks(students, courses)
        if result is not None:
            selected_course, marks = result
    elif choice == "2":
        list_courses(courses)
    elif choice == "3":
        list_students(students)
    elif choice == "4":
        if selected_course is not None:
            show_student_marks(selected_course, marks)
        else:
            print("No course selected.")
    elif choice == "5":
        break
    else:
        print("Invalid choice! Please try again.")
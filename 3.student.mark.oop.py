import math
import numpy as np

students = []
courses = []
student_marks = {}


class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob

    def __str__(self):
        return f"Student ID: {self.student_id} --- Name: {self.student_name} --- Dob: {self.student_dob}"


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def __str__(self):
        return f"Course ID: {self.course_name} --- Course name: {self.course_name}"


class StudentMarkManagement:
    def input_student(self):
        number_student = int(input("Enter number of students: "))
        for _ in range(number_student):
            student_name = input("Enter student name: ")
            student_id = int(input("Enter student ID: "))
            student_dob = input("Enter student dob (DD/MM/YYYY): ")
            student = Student(student_id, student_name, student_dob)
            students.append(student)

    def student_list(self):
        print("Student information: ")
        for student in students:
            print(f"Student ID: {student.student_id} --- Student name: {student.student_name} --- DOB: {student.student_dob}")
            print()

    def input_course(self):
        number_course = int(input("Enter number of courses: "))
        for _ in range(number_course):
            course_id = int(input("Enter course ID: "))
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            courses.append(course)

    def course_list(self):
        print("Course information: ")
        for course in courses:
            print(f"Course ID: {course.course_id} --- Course name: {course.course_name}")
            print()

    def input_mark(self):
        course_id = int(input("Enter course ID to input marks for: "))
        selected_course = None
        for course in courses:
            if course.course_id == course_id:
                selected_course = course
                break
        if selected_course is None:
            print("Error! Please enter a valid course ID.")
            return

        for student in students:
            mark = float(input(f"Enter mark for student {student.student_name}: "))
            student_marks[student.student_name] = mark

        selected_course.marks = student_marks

    def student_mark_list(self):
        course_id = int(input("Enter course ID you want to see marks for: "))
        selected_course = None
        for course in courses:
            if course.course_id == course_id:
                selected_course = course
                break
        if selected_course is None:
            print("Error! Please enter a valid course ID.")
            return

        print(f"Marks for course {selected_course.course_name}: ")
        for key, value in selected_course.marks.items():
            print(f"Student name: {key} --- Mark: {math.floor(value * 10) / 10}")  # Rounded down to 1 decimal place

    def total_students(self):
        print(f"Total number of students: {len(students)}")

    def total_courses(self):
        print(f"Total number of courses: {len(courses)}")

    def calculate_gpa(self, student_marks, weights):
        marks = np.array(list(student_marks.values()))
        weighted_sum = np.sum(marks * weights)
        total_credits = np.sum(weights)
        gpa = weighted_sum / total_credits
        return round(gpa, 2)

    def sort_students_by_gpa(self):
        weights = np.array([3, 4, 3])  # Example weights for three courses

        for student in students:
            gpa = self.calculate_gpa(student.marks, weights)
            student.gpa = gpa

        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        print("Students sorted by GPA (descending order):")
        for student in sorted_students:
            print(f"Student ID: {student.student_id} --- Name: {student.student_name} --- GPA: {student.gpa}")
            print()


# Main
x = StudentMarkManagement()
while True:
    print("-------Menu------")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks for a course")
    print("4. List of courses")
    print("5. List of students")
    print("6. Student marks of a course")
    print("7. Total number of students")
    print("8. Total number of courses")
    print("9. Sort students by GPA")
    print("10. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        x.input_student()
    elif choice == 2:
        x.input_course()
    elif choice == 3:
        x.input_mark()
    elif choice == 4:
        x.course_list()
    elif choice == 5:
        x.student_list()
    elif choice == 6:
        x.student_mark_list()
    elif choice == 7:
        x.total_students()
    elif choice == 8:
        x.total_courses()
    elif choice == 9:
        x.sort_students_by_gpa()
    elif choice == 10:
        break
    else:
        print("Error! Please enter a valid number.")
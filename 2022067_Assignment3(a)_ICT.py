class Student:
    def __init__(self):
        self.name = ""  # Initialize student name
        self.reg_number = ""  # Initialize registration number
        self.date_of_birth = ""  # Initialize date of birth
        self.program = ""  # Initialize student program

    def read_student_info(self):
        self.name = input("Enter Student Name: ")
        self.reg_number = input("Enter Registration Number: ")
        self.date_of_birth = input("Enter Date of Birth: ")
        self.program = input("Enter Student Program: ")

    def display_student_info(self):
        print("Student Name:", self.name)
        print("Registration Number:", self.reg_number)
        print("Date of Birth:", self.date_of_birth)
        print("Program:", self.program)


class Course(Student):
    def __init__(self):
        super().__init__()
        self.course_code = ""  # Initialize course code
        self.course_title = ""  # Initialize course title
        self.course_grade = ""  # Initialize course grade

    def read_course_info(self):
        super().read_student_info()  # Inherit student info
        self.course_code = input("Enter Course Code: ")
        self.course_title = input("Enter Course Title: ")
        self.course_grade = input("Enter Course Grade: ")

    def display_course_info(self):
        super().display_student_info()  # Display student info
        print("Course Code:", self.course_code)
        print("Course Title:", self.course_title)
        print("Course Grade:", self.course_grade)


class Semester(Course):
    def __init__(self):
        super().__init__()
        self.year = 0  # Initialize academic year
        self.semester = ""  # Initialize semester (e.g., Spring, Fall)
        self.courses = []  # Initialize list of courses for the semester

    def read_semester_info(self):
        super().read_course_info()  # Inherit course info
        self.year = int(input("Enter Year: "))
        self.semester = input("Enter Semester: ")
        num_courses = int(
            input("Enter the number of courses in this semester: "))
        for i in range(num_courses):
            course = Course()
            course.read_course_info()
            self.courses.append(course)

    def compute_semester_gpa(self):
        total_grade_points = 0  # Initialize total grade points
        total_credits = 0  # Initialize total credits

        for course in self.courses:
            if course.course_grade.isdigit():
                total_grade_points += int(course.course_grade)
            total_credits += 1

        if total_credits > 0:
            semester_gpa = total_grade_points / total_credits
            return semester_gpa
        else:
            return 0

    def display_semester_info(self):
        super().display_course_info()  # Display course info
        print("Year:", self.year)
        print("Semester:", self.semester)
        print("Courses:")
        for course in self.courses:
            course.display_course_info()
        print("Semester GPA:", self.compute_semester_gpa())


class Transcript(Semester):
    def __init__(self):
        super().__init__()
        self.semesters = []  # Initialize list of semesters in the transcript

    def compute_cgpa(self):
        total_grade_points = 0  # Initialize total grade points
        total_credits = 0  # Initialize total credits

        for semester in self.semesters:
            semester_gpa = semester.compute_semester_gpa()
            total_grade_points += semester_gpa
            total_credits += 1

        if total_credits > 0:
            cgpa = total_grade_points / total_credits
            return cgpa
        else:
            return 0

    def display_transcript_info(self):
        super().display_semester_info()  # Display semester info
        print("Cumulative GPA:", self.compute_cgpa())

    def read_transcript(self):
        num_semesters = int(input("Enter the number of semesters: "))
        for i in range(num_semesters):
            semester = Semester()
            semester.read_semester_info()
            self.semesters.append(semester)


def main():
    transcript = Transcript()

    while True:
        print("\nOptions:")
        print("1. Enter Transcript Information")
        print("2. Display Transcript")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            transcript.read_transcript()
        elif choice == '2':
            print("\nTranscript:")
            transcript.display_transcript_info()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()

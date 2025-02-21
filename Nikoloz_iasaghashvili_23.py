import grades_utils

class InvalidCreditsError(Exception):
    pass

class InvalidGradeError(Exception):
    pass

class DuplicateCourseError(Exception):
    pass

class Course:
    def __init__(self, name, credits):
        if not (5 <= credits <= 10):
            raise InvalidCreditsError("Credits must be between 5 and 10")
        self.name = name
        self.credits = credits
        self.grades = []

    def add_grade(self, val):
        if not (0 <= val <= 100):
            raise InvalidGradeError("Grade must be between 0 and 100")
        self.grades.append(val)

    def get_final_grade(self):
        return grades_utils.calculate_average(self.grades) if self.grades else 0

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = {}

    def add_course(self, course_name, credits):
        if course_name in self.courses:
            raise DuplicateCourseError(f"Course '{course_name}' already exists for {self.name}.")

        try:
            new_course = Course(course_name, credits)
            self.courses[course_name] = new_course
        except (InvalidCreditsError, InvalidGradeError) as e:
            raise

    def remove_course(self, course_name):
        if course_name in self.courses:
            del self.courses[course_name]

    def get_gpa(self):
        total_grade_points = 0
        total_credits = 0
        for course in self.courses.values():
            final_grade = course.get_final_grade()
            if final_grade is not None:
                total_grade_points += final_grade * course.credits
                total_credits += course.credits
        return total_grade_points / total_credits if total_credits > 0 else 0

    def get_transcript(self):
        print(f"Transcript for {self.name}:")
        for course_name, course in self.courses.items():
            final_grade = course.get_final_grade()
            print(f" {course_name}: Credits: {course.credits}, Final Grade: {final_grade}")

    def check_scholarship_eligibility(self):
        return self.get_gpa() > 80


try:
    student1 = Student("Nika")
    student1.add_course("Math", 7)
    student1.add_course("Physics", 7)
    student1.courses["Math"].add_grade(95)
    student1.courses["Physics"].add_grade(85)

    student1.get_transcript()
    print(f"GPA: {student1.get_gpa()}")
    print(f"Scholarship Eligible: {student1.check_scholarship_eligibility()}")

    student1.remove_course("Chemistry")
    student1.remove_course("Math")
    student1.get_transcript()
    print(f"GPA: {student1.get_gpa()}")

except (InvalidCreditsError, InvalidGradeError, DuplicateCourseError) as e:
    print(f"Error: {e}")


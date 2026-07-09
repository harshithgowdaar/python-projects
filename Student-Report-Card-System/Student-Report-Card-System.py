class Student:
    """Represents a student and their academic records."""

    def __init__(self, rollno: int, name: str):
        self.rollno = rollno
        self.name = name
        self.__marks = {}

    def add_marks(self, subject: str, marks: int):
        """Add marks for a subject."""
        if not 0 <= marks <= 100:
            raise ValueError("Marks should be between 0 and 100.")
        self.__marks[subject] = marks

    def get_marks(self) -> dict:
        return self.__marks

    def calculate_average(self) -> float:
        if not self.__marks:
            return 0.0
        return sum(self.__marks.values()) / len(self.__marks)

    def is_passed(self) -> bool:
        return all(mark >= 35 for mark in self.__marks.values())

    def calculate_grade(self) -> str:
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"


class ReportCard:
    """Generates a student's report card."""

    @staticmethod
    def generate(student: Student):
        print("\n" + "=" * 40)
        print("        STUDENT REPORT CARD")
        print("=" * 40)
        print(f"Name     : {student.name}")
        print(f"Roll No. : {student.rollno}")

        print("\nMarks")
        print("-" * 40)
        for subject, marks in student.get_marks().items():
            print(f"{subject:<15} : {marks}")

        print("-" * 40)
        print(f"Average : {student.calculate_average():.2f}")
        print(f"Result  : {'Pass' if student.is_passed() else 'Fail'}")
        print(f"Grade   : {student.calculate_grade()}")
        print("=" * 40)


class ClassRoom:
    """Represents a classroom containing multiple students."""

    def __init__(self, grade: str, section: str):
        self.grade = grade
        self.section = section
        self.__students = []

    def add_student(self, student: Student):
        self.__students.append(student)

    def get_students_list(self):
        print(f"\nClass {self.grade}-{self.section}")
        print("-" * 25)
        for i, student in enumerate(self.__students, start=1):
            print(f"{i}. {student.name}")

    def calculate_class_average(self):
        if not self.__students:
            return 0.0

        total = sum(student.calculate_average() for student in self.__students)
        return total / len(self.__students)


# ---------------- Main Program ---------------- #

student1 = Student(1, "Harshith")
student1.add_marks("Kannada", 90)
student1.add_marks("English", 99)
student1.add_marks("Hindi", 99)
student1.add_marks("Math", 96)
student1.add_marks("Science", 94)
student1.add_marks("Social", 99)

student2 = Student(2, "Rama")
student2.add_marks("Kannada", 80)
student2.add_marks("English", 75)
student2.add_marks("Hindi", 78)
student2.add_marks("Math", 85)
student2.add_marks("Science", 81)
student2.add_marks("Social", 88)

classroom = ClassRoom("10", "B")
classroom.add_student(student1)
classroom.add_student(student2)

classroom.get_students_list()

ReportCard.generate(student1)

print(f"\nClass Average: {classroom.calculate_class_average():.2f}")
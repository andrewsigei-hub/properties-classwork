ALL_COURSES = [ ## Constant DO NOT CHANGE
    "Data Science",
    "Software Engineering",
    "DevOPS",
    "Cyber Security",
    "AI Engineering",
    "High School Bootcamp",
    "Product Design",
    "Data Analytics",
    "Data Analytics for HR Professionals",
]

GENDER = ["Female", "Male"]


class Student:
    student_count = 0
    all_students = []

    def __init__(self, first_name, last_name, age, gender, student_id, course, instructor):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student_id = student_id
        self.course = course
        self.instructor = instructor
        Student.student_count += 1
        Student.all_students.append(self)

    # Course property/getter
    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        if course in ALL_COURSES:
            self._course = course
        else:
            raise ValueError("The course listed is not offered yet.")

    # Gender property/getter
    @property
    def gender(self):
        return self._gender # Returns something hence getter

    @gender.setter
    def gender(self, gender):
        if gender in GENDER:
            self._gender = gender # converts into and accesible variable
        else:
            raise ValueError("You must be either Male or Female")

    # Age property
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 18:
            self._age = age
        else:
            raise ValueError("Your age must be 18 years or above")

    # Fullname property
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    # Email property
    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@student.moringaschool.com"

    # Class methods
    @classmethod
    def total_students(cls):
        return f"The total number of students is: {cls.student_count}"

    @classmethod
    def student_list(cls):
        return [student.fullname for student in cls.all_students]

    @classmethod
    def student_list_2(cls):
        return [student.fullname for student in cls.all_students]

    # Static method
    @staticmethod
    def reverse_name(first_name, last_name):
        return f"{last_name} {first_name}"



student1 = Student(
    "Bradley", "Murimi", 40, "Male", "MSS-1234", "Software Engineering", "Fainus Mudahe"
)
student2 = Student(
    "Mariam", "Rashid", 20, "Female", "MSS-1428", "Software Engineering", "Julius Mutindwa"
)
student3 = Student(
    "Fredrick", "Rangara", 50, "Male", "MSS-1480", "Software Engineering", "Julius Mutindwa"
)


print(student3.course)   # Software Engineering
print(student1.gender)   
print(student2.age)      
print(Student.total_students())  
print(Student.student_list())    
print(Student.student_list_2())   

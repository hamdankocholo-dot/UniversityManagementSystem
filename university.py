
from student import Student
from teacher import Teacher
from department import Department
from course import Course

class University:
    def __init__(self, name : str):
        self.__name = name
        self.__students = []
        self.__teachers = []
        self.__courses = []
        self.__departments = []


    #Returns the name of the university
    def get_name(self):
        return self.__name

    # Returns a copy of list of students registered at the university
    def get_students(self):
        return self.__students.copy() #since this field is a list, lists are mutable
                                        #we do not expose mutable objects because client notice it and temper with it
    # Returns a copy of  list of teachers employed by the university
    def get_teachers(self):
        return self.__teachers.copy()

    #returns number of departments the university has
    def get_total_departments(self):
        return len(self.__departments)

    # adds a student to the list of students
    def add_student(self, student: Student):
        self.__students.append(student)

    # sorts students using IDs in ascending order
    def sort_students(self):
        self.__students.sort(key=lambda student: student.get_student_id())

    # removes a student from a list of teachers
    def remove_student(self, student: Student):
        self.__students.remove(student)

    # adds a teacher to the list of teachers
    def add_teacher(self, teacher: Teacher):
        self.__teachers.append(teacher)

    # Removes a teacher from the list of teachers
    def remove_teacher(self, teacher: Teacher):
        self.__teachers.remove(teacher)

    # looks ip for a student from student list using student_id
    def find_student(self, student_id):
        for student in self.__students:  # loop thorugh all the students
            if student.get_student_id() == student_id:
                return student
        return f"A student with ID : {student_id} does not exist"

    def find_teacher(self, teacher_id):
        for teacher in self.__teachers:
            if teacher.get_employee_id() == teacher_id:
                return teacher
        return f"A teacher with ID : {teacher_id} does not exist"

    # Returns the total number of students registered at the university
    def get_total_students(self):
        return len(self.__students)

    # Returns the total number of teachers employed by the university
    def get_total_teachers(self):
        return len(self.__teachers)

    #returns the number of courses offered by the university
    def get_total_courses_offered(self):
        return len(self.__courses)

    # Returns the combined number of students and teachers in the university
    def get_total_people(self):
        return len(self.__students) + len(self.__teachers)

    # Returns the number of students classified as local students
    def get_local_students_count(self):
        count = 0
        for student in self.__students:
            student_type = (student.get_student_type().lower())
            if student_type == "local":
                count += 1

        return count

    # Returns the number of students classified as international students
    def get_international_students_count(self):
        count = 0
        for student in self.get_students():
            student_type = (student.get_student_type().lower())
            if student_type == "international":
                count += 1

        return count



    def __str__(self):
        return (f"{self.__name} "
            f"({len(self.__students)} students, "
            f"{len(self.__teachers)} teachers)"
        )



'''TESTING AREA'''
if __name__ == '__main__':
    university = University("University")
    s1 = Student("Nyanut  Kuot", 20, "00010", "local")
    s2 = Student("Machar Kuot", 24, "00005", "intenational")
    university.add_student(s1)
    university.add_student(s2)
    university.sort_students()
    print(university.find_student("00000")) #A student with ID : 00000 does not exist
    print(university.find_student("00010")) #Nyanut  Kuot (00010)

    for student in university.get_students():
        for key, value in student.get_details().items():
            print(f"{key}: {value}")
        print()

    university.remove_student(s1)
    for student in university.get_students():
        for key, value in student.get_details().items():
            print(f"{key}: {value}")
        print()
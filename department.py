from UniversityManagementSystem.course import Course
from UniversityManagementSystem.teacher import Teacher
from course import Course
from teacher import Teacher

'''
improvements:
find_teacher() 
courses_exist()
'''
class Department:
    def __init__(self, dep_name: str):
        self.__dep_name = dep_name
        self.__courses =[]
        self.__teachers = []

    #returns name of the department
    def get_dep_name(self):
        return self.__dep_name

    # Returns a copy of the courses list
    def get_courses(self):
        return self.__courses.copy()

    #returns a copy of list of teachers in the department
    def get_teachers(self):
        return self.__teachers.copy()

    #adds a course to the list of courses of the department
    def add_course(self, course):
        self.__courses.append(course)

    #removes a course from the department
    def remove_course(self, course: Course):
        self.__courses.remove(course)

    #returns the total number of courses
    def get_total_courses(self):
        return len(self.__courses)

    #looks up a course from list of courses using course id
    def find_course(self, course_id):
        for course in self.__courses:
            if course.get_course_id() == course_id:
                return course
        return f"A course with ID:" f"{course_id} does not exist."

    #adds a teacher to the list of teachers of the department
    def add_teacher(self, teacher: Teacher):
        self.__teachers.append(teacher)

    #searches a teacher from the list of teachers
    def find_teacher(self, teacher_id: str):
        for teacher in self.__teachers:
            if teacher.get_employee_id() == teacher_id():
                return teacher
        return  f" Teacher with id: {teacher_id } does not exist."


    #Removes a teacher from the department
    def remove_teacher(self, teacher: Teacher):
        self.__teachers.remove(teacher)


    #returns the total number of teachers
    def get_total_teachers(self):
        return len(self.__teachers)

    def __str__(self):
        return (
            f"{self.__dep_name}: "
            f"Teachers: {self.get_total_teachers()} | "
            f"Courses: {self.get_total_courses()}"
        )















if __name__ == "__main__":
    Mathematics_dep = Department("Maths Department")
    Science_dep = Department("Science Department")
    Engineering_dep = Department("Engineering Department")

    #create teacher objects for
    t1 = Teacher("Helmet", 40, "10001")
    t2 = Teacher("Hamdok", 30, "10002")
    t3 = Teacher("Kokani", 53, "10003")
    t4 = Teacher("Kaluni", 45, "10004")
    t5 = Teacher("Jaffa", 60, "10005")
    t6 = Teacher("Shushu", 39, "10006")

    #Create course objects
    c1 = Course('Java', "100", "3", "Science")
    c2 = Course('Python', "101","3", "Science")
    c3 = Course('Phy', "421", "3", "Engineering")
    c4 = Course('Cacl', "141", "3", "Mathematics")

    #add teachers to the math department
    Mathematics_dep.add_teacher(t1)
    Mathematics_dep.add_teacher(t2)
    Mathematics_dep.add_course(c1)
    Mathematics_dep.add_course(c2)


    #add teachers to the science department
    Science_dep.add_teacher(t3)
    Science_dep.add_teacher(t4)
    Science_dep.add_course(c3)

    #add teachers to the science department
    Engineering_dep.add_teacher(t5)
    Engineering_dep.add_teacher(t6)
    Engineering_dep.add_course(c4)


    print(Mathematics_dep) #Maths Department: Teachers: 2 | Courses: 2
    print(Mathematics_dep.get_total_teachers()) #2
    print(Mathematics_dep.get_total_courses()) #2

    #Engineering department
    print(Engineering_dep) #Engineering Department: Teachers: 2 | Courses: 1
    print(Engineering_dep.get_total_teachers()) #2
    print(Engineering_dep.get_total_courses()) #1

    #Science Department
    print(Science_dep) #Science Department: Teachers: 2 | Courses: 1
    print(Science_dep.get_total_teachers()) #2
    print(Science_dep.get_total_courses()) #1













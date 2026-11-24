from exceptions import CourseIdError

class Course:
    def __init__(self, course_name: str, course_id:str, course_credits : int, course_dept):
        #when validating, you use parameter directly like: course_id. not self.__course_id
        if len(course_id) != 3  or not course_id.isdigit():
            raise CourseIdError("Course ID must be 3 digits")
        self.__course_name = course_name
        self.__course_id = course_id
        self.__course_credits = course_credits
        self.__course_dept = course_dept
    #returns the course name
    def get_course_name(self) -> str:
        return self.__course_name

    #returns the course ID
    def get_course_id(self) :
        return self.__course_id

    #returns the number of credits of the course
    def get_course_credits(self):
        return self.__course_credits

    #returns the department the course belongs to
    def get_course_department(self) :
        return self.__course_dept





    def __str__(self) :
        return (f"Course name: ({self.__course_name}, ID: {self.__course_id},  Credits: {self.__course_credits}, "
                f"Course dept: {self.__course_dept})")








if __name__ == "__main__":
    course1 = Course("Comp303", "100", "3", "Science")
    course2 = Course("Python", "101", "4", "Science")


    print(course1) #Course name: (Comp303, ID: 100,  Credits: 3, Course dept: Science)
    print(course1.get_course_name())  #Comp303
    print(course1.get_course_id()) #100

    #course2
    print(course2) #Course name: (Python, ID: 101,  Credits: 4, Course dept: Science)
    print(course2.get_course_name())  #Python
    print(course2.get_course_id()) #101
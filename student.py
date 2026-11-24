from person import Person
from exceptions import InvalidAgeError, InvalidIdError

class Student(Person):
    def __init__(self, name: str, age: int,student_id: str, student_type: str):
        #since we do not want invalid age, we just raise exception
        #if we catch it, then it will raise it, then catch it , the program continues and object maybe created with
        # invalid state
        if age < 0 :
            raise InvalidAgeError("Age cannot be negative")

        # IDs are commonly stored as strings. for this, the IDs must be strings of digits and only 5 of them
        # raise exception if id is invalid, ID must be 5 digits
        # raise exception if id is invalid
        if len(student_id) != 5 or not student_id.isdigit():
            raise InvalidIdError("Student ID must be 5 digits.")

        super().__init__(name, age)
        self.__student_type = student_type
        self.__student_id = student_id


    #getter for student_type
    def get_student_type(self):
        return self.__student_type

    #getter for student_id
    def get_student_id(self):
        return self.__student_id

    def get_details(self):
       return {"name" : self.get_name(), "age" : self.get_age(),"student_id": self.get_student_id(), "student_type" :
           self.get_student_type()}
    #returns the name of the student and their id
    #called when a string representation of the object is called
    #eg: s1 = Student(...) Then we do print(s1) . if not implemented, class name and address of the object is printed instead
    def __str__(self):
        return (
            f"Student:"
            f"{self.get_name()} "
            f"({self.get_student_id()})")

#if __name__ == "__main__": is a common Python entry-point check. It runs the indented code only when you run that file
# directly. If another file imports it, the guarded code won’t run.
if __name__ == "__main__":
    '''Tests'''
    s1 =  Student("Kocholo", 15, "00101", "local")
    print(s1.get_details())#{'name': 'Kocholo', 'age': 15, 'student_id': '00101', 'student_type': 'local'}
    print(s1.get_age())#15
    print(s1.get_student_id())#00101
    print(s1.get_name())#Kocholo
    print(s1.get_student_type())#local


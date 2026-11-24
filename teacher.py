from person import Person
from exceptions import InvalidAgeError, InvalidIdError

class Teacher(Person):
    def __init__(self, name: str,  age: int, employee_id : str) :
        #validate first before you create object
        #raises exception if age
        if age < 0:
            raise InvalidAgeError("Age cannot be nagative.")

        #IDs are commonly stored as strings. for this, the IDs must be strings of digits and only 5 of them
        #raise exception if id is invalid, ID must be 5 digits
        #raise exception if id is invalid
        if len(employee_id) != 5 or not employee_id.isdigit():
            raise InvalidIdError("Employee ID must be 5 digits.")

        '''only after validation will the object be initialized
        remember, when a subclass that adds extra fields to those they inherited from super class,
         the objects of this subclass will be created in two steps, first we call superclass's constructor to initialize 
         the fields that the subclass inherited, then subclass initializes the fields that are unique to it
         '''
        super().__init__(name, age) #initializes the fields shared with the subclass
        self.__employee_id = employee_id  #subclass can now initialize fields tha are unique to it


    #getter for employee_id
    def get_employee_id(self):
        return self.__employee_id


    #returns the details of the teacher
    def get_details(self):
        return {"name": self.get_name(), "age": self.get_age(), "employee_id": self.__employee_id}


    def __str__(self):
        return(
            f"Teacher: "
            f"{self.get_name()} "
            f" ({self.get_employee_id()})"
        )








#if __name__ == "__main__": is a common Python entry-point check. It runs the indented code only when you run that file
# directly. If another file imports it, the guarded code won’t run.
#if we do: print(__name__) here we get  #__main__   but if we do  print(Teacher.__name__) in the class
#that imports it we get:  print(Teacher.__name__)
if __name__ == "__main__":
    '''Testing Area'''
    t1 = Teacher("Sherill", 15, "10001")
    print(t1) #Teacher: Sherill  (10001)
    print(t1.get_details()) #{'name': 'Sherill', 'age': 15, 'employee_id': '10001'}
    print(t1.get_employee_id()) #10001
    print(t1.get_name()) #Sherill
    print(t1.get_age()) #15


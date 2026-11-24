
"""
Application Entry Point

Defines no domain classes.
Creates objects, invokes business logic and serves as the starting point of the
University Management System.
"""
from university import University
from teacher import Teacher
from student import Student

if __name__=="__main__":
    '''#creates university object'''
    university = University("The Nuba University")

    ''' #prints the name of the university and number of students , teachers'''
    #secretly python does university.__str__ (which I implemented to print name of university, number of students
    #and number of teachers. If not implemented, a class name and the address of the will be printed instead
    print(f" {university} ")
    print()

    '''#creates and initializes teacher objects'''
    teacher1 = Teacher("Paul Mwangi", 30, "10000")
    teacher2 = Teacher("Recho Kibet", 30, "10001")
    teacher3 = Teacher("Willy Mtunga", 30, "10002")
    teacher4 = Teacher("Gabriel Martineli", 30, "10003")
    teacher5 = Teacher("Wambugu Wa Kamau", 30, "10004")

    '''#creates and initializes student objects'''
    student1 = Student("Nyanut  Kuot", 20, "00004", "local")
    student2 = Student("Kocholo Hamdan", 19, "00002", "local")
    student3 = Student("Sarah Zacks", 24, "00005", "local")
    student4 = Student("Mujib Tubaa", 23, "00001", "international")
    student5 = Student("Philips Ceasar", 21, "00003", "international")

    '''#adds students to university'''
    university.add_student(student1)
    university.add_student(student2)
    university.add_student(student3)
    university.add_student(student4)
    university.add_student(student5)

    '''#prints student details'''
    for student in university.get_students():
        for key, value in student.get_details().items():
            print(f"{key} : {value} ")
            print()

    '''#add teachers to the university'''
    university.add_teacher(teacher1)
    university.add_teacher(teacher2)
    university.add_teacher(teacher3)
    university.add_teacher(teacher4)
    university.add_teacher(teacher5)

    '''#prints teachers'''
    for teacher in university.get_teachers():
        for key, value in teacher.get_details().items():
            print(f'{key} : {value}')
            print()
    # prints the total number of people at The Nuba university
    print(f"The total count of students at {university.get_name()}: {university.get_total_students()}")
    # prints the total count of students at TNU
    print(f"Total count of local students at {university.get_name()} : {university.get_local_students_count()}")

    # prints the total number of international students
    print(f"Total count of international students at {university.get_name()}: "
          f"{university.get_international_students_count()}")

    # prints the total(students + teachers) of people at The Nuba University(TNU)
    print(f"The total count of people at {university.get_name()}: {university.get_total_people()}")

    # searches a student from the list of students at the university
    print(university.find_student("23234"))  #
    print(university.find_student("00004"))  # Nyanut Kuot






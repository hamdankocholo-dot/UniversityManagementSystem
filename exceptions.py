'''
*we put exceptions all in one file because multiple class may need same
exception and we do not want to duplicate the same courses everywhere
so we have all exceptions in one file then a class that want certain exception,
they can import them from this file
'''

class StudentNotFoundError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InvalidIdError(Exception):
    pass

class CourseIdError(Exception):
    pass
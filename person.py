from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    #getter for name
    def get_name(self):
        return self.__name
    #getter for age
    def get_age(self):
        return self.__age

    @abstractmethod
    def get_details(self):
        pass   #must be implemented by subclasses





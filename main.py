from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data(self):
        "write something"


class PersonSingleton(IPerson):

    __instance = None

    def get_instance(self):
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        else:
            return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("The other name and age does not implement")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    def print_data(self):
        return f"Name : {self.name} age : {self.age}"

obj = PersonSingleton('Radud', 10)
obj2 = PersonSingleton('Jva', 10)
print(obj.print_data())

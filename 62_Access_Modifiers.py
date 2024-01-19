class Employee:
    def __init__(self, name, height):
        self.name = name  # public variable
        self.__age = 18  # for private AM we need to do (__) in prefix of any variable
        self.height = height

    def _height(self):
        return self.height


class Programmer(Employee):
    pass


a = Employee("om", 5.6)


# Public
print(a.name)


# Private
# how to access private modifier indirectly: (_className_AttributeName) it is called Name Mangling
print(a._Employee__age)
print(a.__dir__())  # it gives the all attribute and method is being used in class


# Protected
obj1 = Employee("Hardik", "6")
obj2 = Programmer("Hardik", "6")
print(obj1._height())
print(obj2._height())
print(dir(obj1))

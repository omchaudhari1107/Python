# super in methods
class ParentClass:
    def ParentMethod(self):
        print("Parent Methods")


class ChildClass(ParentClass):
    def ParentMethod(self):
        print("Parent Methods in Child Class")
        super().ParentMethod()

    def ChildMethod(self):
        print("Child Method")
        super().ParentMethod()


obj = ChildClass()
obj.ChildMethod()
obj.ParentMethod()

print("----------------------------------------")


# super in constructor
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)  # using a super Keyword on constructor
        self.lang = lang


om = Employee("om", "1")
hardik = Programmer("Hardik", "420", "Python")
print(hardik.name)
print(hardik.id)
print(hardik.lang)

class Employee:
    def __init__(self, name, identity):
        self.name = name
        self.id = identity

    def showDetails(self):
        print(f"The name of Employee id {self.id} is {self.name}")


# this is how we do inheritance
class Programmer(Employee):
    def showLangauge(self):
        print(f"The default langauge is python of id {self.id}")


e1 = Employee("om", 1)
e1.showDetails()

e2 = Programmer("Hardik", 420)
e2.showDetails()
e2.showLangauge()

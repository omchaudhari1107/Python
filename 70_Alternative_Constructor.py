class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # class Methods is an Alternative Constructor
    @classmethod
    def fromstr(cls, str_):
        return cls(str_.split("-")[0], int(str_.split("-")[1]))


e = Employee("om", "1")
print(e.name)
print(e.salary)

string = "Om-1"
e = Employee(string.split("-")[0], string.split("-")[1])
print(e.name)
print(e.salary)

string = "Om-1"  # if name and salary come in one string then we use class Methods
e = Employee.fromstr(string)
print(e.name)
print(e.salary)

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")


class DancerEmployee(Dancer, Employee):
    def __init__(self, dance, name):
        super().__init__(dance)
        self.dance = dance
        self.name = name


o = DancerEmployee("Kathak", "Hardik")
print(o.dance)
print(o.name)
o.show()  # class DancerEmployee(Dancer,Employee):which is written 1st will run,means Dancers method will run
print(DancerEmployee.mro())  # Method Resolution Operator

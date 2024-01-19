class Employee:
    companyName = "Apple"  # class Variable(same for all):use className.attributeName to access

    def __init__(self, name):
        self.name = name  # instance variable(different for employee):use objName.attributeName to access
        self.raise_amount = 0.02

    def showDetails(self):
        print(
            f"The name of employee is {self.name} and raise amount in {self.companyName} is {self.raise_amount}"
        )


emp1 = Employee("Om")
# Here the things such as name, raise is associated with emp1 which is also called an instance of class or object thus the variable associated with instance if class is call as instance variable
emp1.companyName = "Apple India"
emp1.raise_amount = 0.3
emp1.showDetails()  # OR Employee.showDetails(emp1)

Employee.companyName = "Google"  # accessing class variable

emp2 = Employee("Hardik")
emp2.showDetails()

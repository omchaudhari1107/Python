# methods that allow instances of a class to interact with the built-in functions and operators of the language

class Employee:
    name = "om"

    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i

    def __str__(self):
        return f"The name of Employee is {self.name}"

    def __call__(self):
        print("This is call Method")


e = Employee()
print(len(e))
# here len(e) is give error if we cant define a method inside of class called __len__, at there we define it as __len__
# but we run it as len that's why it is called as Magic Methods

print(e)  # OR we can use repr Method
# here str in class give the detail of the class by printing e
# <__main__.Employee object at 0x00000217C989FF50> ----> The name of Employee is om

e()
# if there is no call Methods inside of class then it give error: 'Employee' object is not callable
# it automatically calls the call method which is inside of class

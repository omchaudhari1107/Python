class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} age is {self.age}")


a = Person("om", 20)
a.info()
b = Person("Hardik", 19)
b.info()

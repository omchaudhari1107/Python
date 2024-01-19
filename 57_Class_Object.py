class Person:
    name = "om"
    occupation = "Software Developer"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()

a.name = "Hardik"
a.occupation = "Front-end Developer"

b.name = "Manav"
b.occupation = "Python Developer"

a.info()
b.info()

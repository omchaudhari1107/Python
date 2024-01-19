class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(num1, num2):  # no self in static method
        return num1 + num2


a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(a.add(1, 2))
# or using className
print(Math.add(1, 2))

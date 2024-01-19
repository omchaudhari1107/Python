class Myclass:
    def __init__(self):
        self.num = None

    def show(self):
        print(f"Value is {self.Ten_value}")

    @property  # getter
    def Ten_value(self):
        return 10 * self.num

    @Ten_value.setter  # setter
    def Ten_value(self, new_value):
        self.num = new_value


obj = Myclass()

obj.Ten_value = 10
obj.show()
# @property:use to create getter and setter

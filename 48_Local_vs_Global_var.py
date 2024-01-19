x = 4  # this is global variable
print(x)


def hello():
    global x  # using global keyword we can use global variable
    # x = 5  # this is local variable which is different from outer ones variable x
    print(x)


hello()
x = 6  # this is the change of x in global variable
print(x)

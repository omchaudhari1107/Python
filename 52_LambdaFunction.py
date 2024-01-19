# def double(x):
#     return x * 2

# a lambda function doesn't have a name but the only skeleton on body or say a body with only skeleton without a skin
# which is a name
double = lambda x: x * 2  # it is used to create a mini type functions
cube = lambda x: x * x * x
# avg = lambda x, y: (x + y) / 2
test = lambda *x: x


def appl(fx, val1, val2):
    return 6 * fx(val1, val2)


print(double(5))
print(cube(5))
# print(avg(double(5), cube(5)))
print(test(1, 2, 3, 4))
print(appl(lambda x, y: (x + y) / 2, 1, 2))

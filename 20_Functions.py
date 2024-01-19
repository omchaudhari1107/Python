def CalculateGmean(a, b):
    return a * b / (a + b)


def isGreater(a, b):
    if a > b:
        print(a, "is Greater than", b)
    elif b > a:
        print(b, "is Greater than", a)
    else:
        print("Both are equal")


def isLesser(a, b):  # means that the body is written afterward but in the same isLesser
    pass


mean = CalculateGmean(3, 3)
print(mean)
isGreater(1, 2)

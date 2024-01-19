def average(a=9, b=1):  # default if no value is passed
    print("The avg is", (a + b) / 2)


average()
average(1, 2)


def average(*num):  # as Variable Arguments in java and this is Arbitrary Argument in python
    sum = 0
    for i in num:
        sum = sum + i
    print("the avg is", sum / len(num))


average(1, 2, 3)

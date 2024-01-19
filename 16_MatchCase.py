# As a switch case in C & C++
x = 1
match x:
    case 0:
        print("0")
    case 4:
        print("4")  # not a break in python
    case _ if x != 80:
        print(x, "is not 80")  # default case with if
    case _:
        print("default")  # default case

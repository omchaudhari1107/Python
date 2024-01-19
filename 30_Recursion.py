def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)


print(factorial_recursion(9))


def factorial_Iteration(n):
    fac = 1
    for i in range(n):
        fac = fac * n
        n = n - 1
        if n == 0:
            return fac


print(factorial_Iteration(9))
# def PrintNumbers(n, l):
#     if n == l:
#         print(l)
#         return 0
#     else:
#         print(n)
#         PrintNumbers(n + 1, l)
#
#
# PrintNumbers(1, 1)

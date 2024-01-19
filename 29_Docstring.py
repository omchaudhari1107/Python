# python docstring are the strings literals that appear right after the definition of a function, method, class,
# or module
def square(n):
    """Take number n and return square on n"""  # doc string is not comment and its read by interpreter(' OR ") but
    # in the latest version " is allowed

    # this is not doc string, and it is comment using(#)
    print(n ** 2)
    """Take number n and return square on n"""  # Not work( Output is:None)


square(5)
print(square.__doc__)  # use to print doc string

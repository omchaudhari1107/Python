# is vs "==":comparison operator
a = [1, 2, 43]
b = [1, 2, 43]

print(a is b)  # exact location of object in memory--refer only one object
print(a == b)  # value

c = 3
d = 3
print(c is d)  # it is true because 3 is constant which is store at same memory, which means that python don't wast
# memory for storing a same data
# immutable -> return true

l = [1, 2, 4, 6, 4, 3]

# MAP:it maps the data with the given function----------->map(function,iterable)
# newlst1 = list(map(cube, l))
# OR
newlst1 = list(map(lambda x: x * x * x, l))
print(newlst1)

# FILTER:it filters the data inside the list------------->filter(function,iterable)
newlst2 = list(filter(lambda x: x > 3, l))
print(newlst2)

# REDUCE:it reduced the data in one integer or string or any datatype------------->reduce(function,iterable)
from functools import reduce  # must need to import

newlst3 = reduce(lambda x, y: (x + y), l)
print(newlst3)

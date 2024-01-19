# if we want to change an tuple data then we to convert it in list first then change on it and then again change it
# to tuple

numbers = (1, 2, 3, 4, 5)
temp = list(numbers)
lst = [i for i in range(6, 11)]
temp = temp + lst
numbers = tuple(temp)
print(numbers) 

# but we can concat two tuple
print(len(numbers))

import time

a = True

print(a := False)
# Walrus operator(:=) The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable
# within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to
# repeat the calculation.

numbers = [1, 2, 3, 4, 5]
while n := len(numbers) > 0:
    print(numbers.pop())
    time.sleep(1)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
print(foods)

# if there is no walrus operator in python
# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#       break
#   foods.append(food)

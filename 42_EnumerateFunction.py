marks = [12, 56, 32, 98, 45, 1, 4]
num = 0
for mark in marks:
    print(mark)
    if num == 3:
        print("Excellent")
    num += 1

# here we need to declare index for accessing an list index, but using Enumerate Function it is possible easily
print("-----")

# index var,marks var
# it give (index,value)
for index, mark in enumerate(marks):
    print(f"At index {index} the marks is {mark}")
    if index == 3:
        print("Excellent")
    index += 1

print("-----")

# for string
name = "Om"
for i, char in enumerate(name, start=1):
    print(f"At index {i} character {char} exist")

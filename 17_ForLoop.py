name = "Hello World"
for i in name:
    print(i)
    if i == "d":
        print("Its end")

colors = ["red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for r in range(5):  # (to)
    print(r + 1)
# Output
# 1
# 2
# 3
# 4
# 5

for r in range(1, 11):  # (from,to)
    print(r)
# Output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

for r in range(1, 11, 11):  # (from,to,steps per loop)
    print(r)
# Output
# 1
# 3
# 5
# 7
# 9

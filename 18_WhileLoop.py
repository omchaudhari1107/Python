cnt = 5
while cnt > 0:
    print(cnt)
    cnt -= 1
# Output
# 5
# 4
# 3
# 2
# 1


i = 1
while i != 0:
    i = int(input("Enter number:"))
    print(i)
else:
    print("you entered 0")

# simulate DO WHILE LOOP in py
i = 0
while True:
    if i == 10:
        break
    else:
        print(i)
        i += 1

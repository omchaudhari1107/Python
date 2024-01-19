# a = int(input("Enter the range"))
for i in range(10):
    if i % 2 == 0:
        print(i)
else:
    print("Sorry")
# else will use with if,for,while
# if loop break using break keyword the else will not execute

for i in range(100):
    if i == 10:
        print("----")
        print(i)
        break
else:
    print("Sorry")  # it will not be executed

for x in range(5):
    print(f"iteration no.{x + 1} in loop")
else:
    print("else block in loop")
print("out of loop")

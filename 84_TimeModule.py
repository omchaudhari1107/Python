import time


# time.time()

def UsingWhile():
    i = 0
    while i < 500000:
        i += 1
        print(i)


def UsingFor():
    for i in range(500000):
        print(i)


init = time.time()
UsingFor()
secFor = time.time() - init
init = time.time()
UsingWhile()
secWhile = time.time() - init
print("For loop is better than while loop") if secFor < secWhile else print("while loop is better than for loop")
print(secFor, secWhile)


# time.sleep()

print(4)
time.sleep(3)
print("After 3 seconds")


# time.strftime()

while True:
    t = time.localtime()
    formatted_time = time.strftime("%d/%M/%Y", t)
    # %Y - %m - % d % H: % M: %S
    print(formatted_time)
    time.sleep(1)

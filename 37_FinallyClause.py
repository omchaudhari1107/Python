def func1():
    try:
        l = [1, 5, 6, 2]
        i = int(input("Enter index"))
        print(l[i])
        return 1
    except Exception as e:
        print(f"Error:{e}")
        return 0
    finally:
        print("i am always execute")
    print("this print will not executed")


x = func1()  # that's why finally is being use
print(x)

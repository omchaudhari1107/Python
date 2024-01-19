try:
    a = int(input("Enter number:"))
    print(f"Multiplication table of {a} is:")
    for i in range(1, 11):
        print(f"{a} * {i} = {a * i}")
except Exception as e:
    print(f"Error:{e}")

print("------")
print("Some imp line of code")
print("------")
# if error ocuurs then this code block will not run, so to handle this type of error we use exception handling

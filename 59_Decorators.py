# decorators is a function with decorate the original function or modify and return that function
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks")

    return mfx()


@greet
def Hello():
    print("Hello world")

# if we want to decorate a function

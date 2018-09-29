import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_thet_runs_fun():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_thet_runs_fun

@my_decorator
def my_function():
    print("I'm the function")

my_function()

##

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_thet_runs_fun(*args, **kwargs):
            print("In the decorator!")
            if number == 56:
                print("Not running the function")
            else:
                func(*args, **kwargs)
            print("After the decorator!")
        return function_thet_runs_fun
    return my_decorator

@decorator_with_arguments(56)
def my_function_too():
    print("Hello")

my_function_too(57, 67)
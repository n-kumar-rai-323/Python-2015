

def decorate_me(func):
    def inner_func():
        print("I am nishan rai")
        func()
    return inner_func

def message():
    print("Hello world")
    

result = decorate_me(message)
result()
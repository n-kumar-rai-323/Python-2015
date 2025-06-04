

def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

result = outer_func("Hello world")
result()
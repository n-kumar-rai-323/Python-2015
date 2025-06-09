def to_upper(func):
    def inner_func():
        value = func()
        return value.upper()
    return inner_func
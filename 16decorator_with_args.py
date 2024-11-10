def add2(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 2
    return wrapper

def add4(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 4
    return wrapper

# Refactoring this repetitive code to below
def add(increment):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + increment
        return wrapper
    return decorator


@add2
def foo(x):
    return x * 2

@add4
def bar(x):
    return x ** 2

print(foo(2)) # 6
print(bar(2)) # 8

# After refactored
@add(6)
def foo(x):
    return x * 2


@add(7)
def bar(x):
    return x ** 2

print(foo(1)) # 8
print(bar(3)) # 16

################################
#Remember that @ is a shorthand:

# @some_decorator
# def some_function(arg):
#     # blah blah
#     # ... is translated by Python into this:

# def some_function(arg):
#     # blah blah
#     some_function = some_decorator(some_function)

#########################################################

####################################
# This function definition...
@add2
def foo(x):
    return x ** 2

# ... is translated by Python into this:
def foo(x):
    return x ** 2
foo = add2(foo)

###### So
@add(2)
def foo(x):
    return x ** 2
# ... is translated by Python into this:
def foo(x):
    return x ** 2
foo = add(2)(foo)
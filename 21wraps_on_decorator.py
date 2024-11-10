from functools import wraps, update_wrapper

def func_decorator_log(func):
    @wraps(func) # on commenting gives wrong metadata
    def wrapper(*args, **kwargs):
        f"Calling the {func.__name__}"
        return func(*args, **kwargs)
    return wrapper

def foo(x):
    """Function to multiply by 2"""
    return x * 2

def bar(y):
    """Function to add by 2"""
    return y + 2

print(foo.__name__, foo.__doc__, foo.__module__, foo.__annotations__) # foo Function to multiply by 2 __main__ {}
print(bar.__name__, bar.__doc__, bar.__module__, bar.__annotations__) # bar Function to add by 2 __main__ {}

@func_decorator_log
def foo(x):
    """Function to multiply by 4"""
    return x * 4

@func_decorator_log
def bar(y):
    """Function to add by 4"""
    return y + 4

print(foo.__name__, foo.__doc__, foo.__module__, foo.__annotations__) # wrapper None __main__ {}
print(bar.__name__, bar.__doc__, bar.__module__, bar.__annotations__) # wrapper None __main__ {}

# After applying wraps

print(foo.__name__, foo.__doc__, foo.__module__, foo.__annotations__) # foo Function to multiply by 4 __main__ {}
print(bar.__name__, bar.__doc__, bar.__module__, bar.__annotations__) # bar Function to add by 4 __main__ {}

# Under the hood of @wraps or @wrapt module by pip install wrapt
def func_decorator_log(func):
    def wrapper(*args, **kwargs):
        print('CALLING: {}'.format(func.__name__))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper.__module__ = func.__module__
    wrapper.__annotations__ = func.__annotations__
    return wrapper

############################################################################
# Note: wraps only works with function-based decorators, 
# your class-based decorators must use update_wrapper instead
#############################################################################
print("Class based decorator on functions")

class ClassDecoratorLogOnFunction:
    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        print('CALLING: {}'.format(self.func.__name__))
        return self.func(*args, **kwargs)
    

def foo(x):
    """Function add by 10"""
    return x + 10

def bar(y):
    """Function subtract by 10"""
    return y - 10

print(foo.__name__, foo.__doc__, foo.__module__, foo.__annotations__) # foo Function add by 10 __main__ {}
print(bar.__name__, bar.__doc__, bar.__module__, bar.__annotations__) # bar Function subtract by 10 __main__ {}


@ClassDecoratorLogOnFunction # foo Function add by 10 __main__ {} only works on update_wrapper in __name, __doc__, __module__, __
def foo(x):
    """Function add by 10"""
    return x + 10

@ClassDecoratorLogOnFunction  # bar Function subtract by 10 __main__ {}
def bar(y):
    """Function subtract by 10"""
    return y - 10

print(foo.__name__, foo.__doc__, foo.__module__, foo.__annotations__) # AttributeError without update_wrapper
print(bar.__name__, bar.__doc__, bar.__module__, bar.__annotations__) # AttributeError without update_wrapper
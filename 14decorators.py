class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

p1 = Person('Mohamed', 'Luqman', 30)
print(p1.full_name)


def make_log(func):
    def wrapper(arg):
        print(f"Logging the function: {func.__name__}")
        return func(arg)
    return wrapper

@make_log
def print_foo(x):
    print(x + 1)

print_foo(5)

# This is more sensible.
def enhanced_printlog_for_method(func):
    def wrapper(self, *args, **kwargs):
        print('CALLING: {} on object ID {}'.format(
        func.__name__, id(self)))
        return func(self, *args, **kwargs)
    return wrapper

class Invoice:
    def __init__(self, id_number, total):
        self.id_number = id_number
        self.total = total
        self.owed = total

    @enhanced_printlog_for_method
    def record_payment(self, amount):
        self.owed -= amount

print("Invoice")
iv1 = Invoice("ITI3423", 115.46)
print(id(iv1))
iv1.record_payment(7)

# Running average

# data = {"total": 0, "count": 0} # This version has bug and the count parameter is common on all function
def running_average(func):
    data = {"total": 0, "count": 0} # Acts as common scope on each call iteration of particular function
    def wrapper(*args, **kwargs):
        # data = {"total": 0, "count": 0} # Each time its newly evaluated and resets its value
        value = func(*args, **kwargs)
        data["total"] += value
        data["count"] += 1
        print("Average of {} so far: {:.01f} and count: {}".format(func.__name__, data["total"], data["count"]))
        return func(*args, **kwargs)
    wrapper.data = data
    return wrapper

@running_average
def foo(x):
    return x + 2

@running_average
def bar(x):
    return 3 * x


print("Running Average")
print(foo(1), foo.data)  # Decorator: 1+2=3 = 3.0       foo: 1+2=3
print(foo(10), foo.data) # Decorator: 10+2=12+3 = 15.0  foo: 10+2=12
print(bar(3), bar.data)  # Decorator: 3*3=9     = 9     bar: 3*3=9
print(foo(1), foo.data)  # Decorator: 1+2=3+15  = 18.0  foo: 1+2=3
print(foo(1), foo.data)  # Decorator: 1+2=3+18  = 21.0  foo: 1+2=3
print(bar(3), bar.data)  # Decorator: 3*3=9+9   = 18     bar: 3*3=9




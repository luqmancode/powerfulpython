class Prefixer:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, message):
        return self.prefix + " " + message

p = Prefixer("Abul Kassim")
print(p("Mohamed Luqman"))

# printlog function decorator

def printlog(func):
    def wrapper(*args, **kwargs):
        print("CALLING: " + func.__name__)
        return func(*args, **kwargs)
    return wrapper

# class printlog generator
class Printlog:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print('CALLING from Class: {}'.format(self.func.__name__))
        return self.func(*args, **kwargs)

@Printlog
def foo(y):
    return y * 2

print(foo(9))

# Class Based decorator supports inheritance in code reusability
import sys
class ResultAnnouncer:
    stream = sys.stdout
    prefix = "RESULT"
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        value = self.func(*args, **kwargs)
        self.stream.write('{}: {}, {}\n'.format(self.prefix, value, self.stream))
        return value 

class StdErrResultAnnouncer(ResultAnnouncer):
    stream = sys.stderr
    prefix = "ERROR"

@StdErrResultAnnouncer
@ResultAnnouncer
def hi(x):
    return x 

print(hi("Hi"))


# Count decorator in class

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        print("calling the decorator")
        print('# of calls: {}'.format(self.count))
        self.count += 1
        return self.func(*args, **kwargs)

@CountCalls
def foo(x):
    return x + 5

@CountCalls
def bar(x):
    return x + 10

print(foo(1))
print(bar(1))
print(foo(8))
# print(bar(8))
print(foo.count)
print(bar.count)

# Class based decorator with accepting arguments
print("Class decorator with args")
class Add:
    def __init__(self, increment):
        self.increment = increment

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + self.increment
        return wrapper

@Add(50)
def foo(x):
    return x + 4

@Add(100)
def bar(x):
    return x * 4

print(foo(7))
print(bar(3))
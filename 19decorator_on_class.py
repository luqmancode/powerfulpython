from functools import wraps 


def decoratorclass(klass): # Not working as expected
    @wraps(klass)
    def wrapper_repr_class(*args, **kwargs):
        _repr =  f"{klass.__name__}()"
        # klass.__repr__ = klass
        return _repr
    return wrapper_repr_class

def class_decorator(klass): # class decorator working pattern function based
    def wrapper_klass(self):
        print("E")
        return '{}()'.format(klass.__name__)
        print("F")
    print("A")
    klass.__repr__ = wrapper_klass
    print("B")
    return klass
    

class Penny:
    year = 1
    def __init__(self, value):
        self.value = value
        print(id(self))
p = Penny(1)
print(p.year, id(p))
print(str(p), id(p))
print(repr(p), id(p))
print("repr not implemented completed here")

# @decoratorclass # getting AttributeError
@class_decorator
class Penny:
    year = 1
    def __init__(self, value):
        self.value = value
        print("C :", id(self))
p = Penny(1)
print("D :", p.year, id(p))
print(str(p))
print(repr(p))


class UpperCaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result.upper()

@UpperCaseDecorator
def get_inputs_from_user():
    name = input("Enter your name: ")
    return name

print(get_inputs_from_user()) # MOHAMED

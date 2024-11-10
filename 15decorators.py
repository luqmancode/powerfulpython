# count = 0 Not working as expected
def count_calls(func):
    count = 0 # UnboundLocalError
    def wrapper(*args, **kwargs):
        # global count # Not working
        nonlocal count # Fix the UnboundLocalError This needed only here due to count is the variable has changed its address and in dict its state is changing and not its id(dict) is changing
        count += 1
        print('# of calls: {}'.format(count))
        return func(*args, **kwargs)
    wrapper.count = count
    return wrapper

@count_calls
def foo(x):
    return x + 2

@count_calls
def bar(x):
    return x * 3

print(foo(2), foo.count)
print(bar(2), bar.count)
print(foo(3), foo.count)
print(bar(3), bar.count)
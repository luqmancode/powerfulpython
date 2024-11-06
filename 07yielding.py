def simple_generator():
    yield 1
    yield 2
    yield 3

simple_gen = simple_generator()
for i in simple_gen:
    print(i)
print("Completed")
def another_generator():
    yield from simple_generator()
    yield 4
    yield 5

for value in another_generator():
    print(value)
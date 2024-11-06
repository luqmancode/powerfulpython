def generate_nums(n=10):
    print("A : Starting ...")
    i = 0
    print("B : before while")
    yield 50
    while i < n:
        print("C: after while")
        yield i
        print("D: after yield, start")
        i += 1
    yield 100

for i in generate_nums():
    print(i)
def generate_squares(num=5):
    for i in range(num):
        yield i ** 2

for i in generate_squares(10):
    print(i)

print(generate_squares)
gen4 = generate_squares(4)
print(gen4)
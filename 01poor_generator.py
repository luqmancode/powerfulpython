def generate_squares(num=5):
    squares = []
    for i in range(num):
        squares.append(i**2)
    return squares

for num in generate_squares(10):
    print(num)

print(generate_squares)
gen4 = generate_squares(4)
print(type(gen4))
print(gen4)
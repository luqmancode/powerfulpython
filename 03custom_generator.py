class GenerateSquares:
    def __init__(self, max_number=10):
        self.current_number = 0
        self.max_number = max_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number >= self.max_number:
            raise StopIteration
        square_number = self.current_number ** 2
        self.current_number += 1
        return square_number

gen_squares = GenerateSquares(5)
print(gen_squares, type(gen_squares))

for i in gen_squares:
    print(i)


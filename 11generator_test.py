def read_from_file(path):
    with open(path) as fh:
        for line in fh:
            yield line.rstrip("\n")

def text_to_words(lines):
    for line in lines:
        words = line.split()
        for word in words:
            yield word

def convert_word_to_letters(word):
    for letter in word:
        yield letter

def read_letters(path):
    lines = read_from_file(path)
    words = text_to_words(lines)
    letters = convert_word_to_letters(words)
    yield from letters

for letter in read_letters("house_data.txt"):
    if letter:
        print(letter)
def matching_lines_from_file(path, pattern):
    with open(path) as fhandle:
        for line in fhandle: # dont use fhandle.read() or fhandle.readlines()
            if pattern in line:
                yield line.rstrip('\n')

# Should use fhandle.readline()  and check the last line with line != ""

def parse_log_records(lines):
    for line in lines:
        line = line.split(": ", 1)
        yield {"Level": line[0], "Message": line[-1]}
       
        level, message = line.split(": ", 1)
        yield {"Level": level, "Message": message}

# usage

log_lines = matching_lines_from_file("server.log", "WARNING")
for record in parse_log_records(log_lines):
    print(record)

with open("server.log") as loghandle:
    for record in parse_log_records(loghandle):
        print(record)



# reusable code
def lines_from_file(path):
    with open(path) as fhandle:
        for line in fhandle:
            yield line.rstrip("\n")

def matching_lines(lines, pattern):
    for line in lines:
        if pattern in line:
            yield line

# reusable usage
log_lines = lines_from_file('server.log')
matching = matching_lines(log_lines, 'ERROR:')
for line in matching:
    print(line)

# or
def matching_lines_from_file(pattern, path):
    file_lines = lines_from_file(path) # yield
    matching = matching_lines(file_lines, "WARNING:") # yield
    for line in matching:
        yield line # yield


# words_of_line
def word_in_text(lines):
    for line in lines:
        for word in line.split():
            yield word 
            

# usage in poem
poem_lines = lines_from_file("poem.txt")
poem_words =  word_in_text(poem_lines)
for word in poem_words:
    print(word)


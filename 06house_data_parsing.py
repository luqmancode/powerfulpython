# house price reading

def lines_from_file(path):
    with open(path) as fh:
        for line in fh:
            yield line.rstrip("\n")

def house_records(lines): # much elegant
    record = {}
    for line in lines:
        print("4444444", line)
        if line == '':
            yield record
            record = {}
            continue
        key, value = line.split(': ', 1)
        record[key] = value
    yield record

house_lines = lines_from_file('house_data.txt')

house_records = house_records(house_lines)
for rec in house_records:
    print(rec)
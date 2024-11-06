print([i*2 for i in range(6)])
print({i:"x" * i for i in range(8)})
range_list = [range(1,7), range(4,12,3), range(-5,9,4)]
print([float(num) for subrange in range_list for num in subrange]) # both sequence is dependent so its expand its variables
for ran in range_list:
    for ra in ran:
        print(ra)

colors = ["orange", "purple", "pink"]
toys = ["bike", "basketball", "skateboard", "doll"]
print([color + " " + toy for color in colors for toy in toys]) # both sequence is independent and takes each one of outside loop with all inside loop

numbers = [1, -2, 3, 5, 6, 8, -54]
print([num for num in numbers if num > 0 if num % 2 == 1 if num != 1]) # any no of if conditions available


weights = [0.2, 0.5, 0.9]
values = [27.5, 13.4]
offsets = [4.3, 7.1, 9.5]

print([(weight, value, offset)
for weight in weights
for value in values
for offset in offsets
if offset > 5.0
if weight * value < offset])

# print(sorted((user.email for user in all_users if user.is_active), reverse=True)) # generator
# print(sorted(user.email for user in all_users if user.is_active)) # generator

prices_flat_list = [
    "orange", 0.70, "banana", 0.86,
    "cantaloupe", 0.63, "bok choy", 1.56,
    "coconuts", 1.06 ]
print({prices_flat_list[i]: prices_flat_list[i+1] for i in range(0, len(prices_flat_list), 2) if len(prices_flat_list) %2 == 0})

def list2dict(flattened_list):
    assert len(flattened_list) % 2 == 0
    result_dict = {}
    for i in range(0, len(flattened_list), 2):
        result_dict[flattened_list[i]] = flattened_list[i+1]
    return result_dict

print(list2dict(prices_flat_list))

names = [
    "Joe", "Jim", "Todd",
    "Tiffany", "Zelma", "Gerry", "Gina"
]
print({name[0]: [].append(name) for name in names}) # Not supporting

def group_by_first_letter(flattened_list):
    result_dict = {}
    for item in flattened_list:
        if item[0] not in result_dict:
            result_dict[item[0]] = [item]
        else:
            result_dict[item[0]].append(item)
    return result_dict

print(group_by_first_letter(names))

from collections import defaultdict

def group_by_first(items):
    grouped = defaultdict(list)
    for item in items:
        key = item[0].lower()
        grouped[key].append(item)
    return grouped

print(group_by_first(names))
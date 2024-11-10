def get_variable_data(*args):
    # packing variables to tuple
    print(type(args), args)

get_variable_data([1,2,3])
get_variable_data(1,2,3)

def get_unpacking_variable(a, b, c):
    print(f"a: {a}, b: {b}, c: {c}")

x = [1,2,3]
y = {"a": "old", "b": "small", "c": "short"}
get_unpacking_variable(x, 4, 5)
get_unpacking_variable(*x) # calling with unpacking
get_unpacking_variable(**y)


def order_book(title, author, isbn):
    """
    Place an order for a book.
    """
    print("Ordering '{}' by {} ({})".format(
        title, author, isbn)
    )

def get_required_textbook(class_id):
    """
    Returns a tuple (title, author, ISBN)
    """
    order_book(*class_id)

get_required_textbook({"the king", "Stephen", "ISBN1214"})


def get_rental_cars(size, doors=4, transmission='automatic'):
    template = "I am looking for {} doors with {} car with {} transmission"
    print(template.format(doors, size, transmission))

get_rental_cars("economy", transmission='manual')

def set_config_defaults(config, **kwargs):
    for key, value in kwargs.items():
        if key not in config: # not rewrite the existing key else it will change based on default kwargs
            config[key] = value
    return

config = {"verbosity": 3, "theme": "Blue Steel"}
set_config_defaults(config, bass=11, verbosity=2)
print(config)


nums = ["12", "7", "30", "14", "3"]
def get_max_from_list(items):
    biggest = items[0]
    for item in items[1:]:
        if int(item) > int(biggest):
            biggest = item
    return biggest
print(get_max_from_list(nums))

integers = [3, -2, 7, -1, -20]
print(max(integers))
def get_absolute_max(items):
    biggest = items[0]
    for item in items[1:]:
        if abs(item) > abs(biggest):
            biggest = item
    return biggest

print(get_absolute_max(integers)) # -20


student_joe = {
    'gpa': 3.7, 'major': 'physics',
    'name': 'Joe Smith'
}
student_jane = {
    'gpa': 3.8, 'major': 'chemistry',
    'name': 'Jane Jones'
}
student_zoe = {
    'gpa': 3.4, 'major': 'literature',
    'name': 'Zoe Fox'
}
students = [student_joe, student_jane, student_zoe]

def get_max_gpa(items):
    max_gpa = items[0] 
    for item in items[1:]:
        if item["gpa"] > max_gpa["gpa"]:
            max_gpa = item
    return max_gpa

print(get_max_gpa(students))

# Create abstractions
def get_max_by_key(items, key):
    biggest = items[0]
    for item in items[1:]:
        if key(item) > key(biggest):
            biggest = item
    return biggest

def get_gpa(obj):
    return obj["gpa"]

print(get_max_by_key(nums, int))
print(get_max_by_key(integers, abs))
print(get_max_by_key(students, get_gpa))

print(sorted(students, key=get_gpa))

from operator import itemgetter, attrgetter

print(sorted(students, key=itemgetter('gpa')))

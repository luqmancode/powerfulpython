def favourite_dessert(category):
    "Describe my favorite food in a category."
    items = {
        "appetizer": "Tandoori",
        "vegetable": "Brocolli",
        "beverage": "Green Tea"
    }

    return "My favorite {} is {}.".format(category, items[category])

print(favourite_dessert.__doc__, favourite_dessert.__name__, favourite_dessert("beverage"))
# print(favourite_dessert("dessert"))

try:
    message = favourite_dessert("drinks")
    print(message)
except KeyError:
    print("I dont have anything specifics and I like them all") # success with 200 on catching exceptions


def print_description(category):
    try:
        message = favourite_dessert(category)
        print(message)
    except KeyError:
        print("I have no favorite {}. I love them all!".format(category))
# Changed the control flow with no error
print_description("appetizer")
print_description("gravy")

# try:
#     from 'speedyjson' import load
# except ImportError:
#     from json import load
import logging 

# try:
#     value = int(input("Enter user input: ")) 
# except ValueError:
#     print("Bad Value from User") # abc
#     logging.error("Bad value from user: %r", value)
# except TypeError:
#     print("Invalid type (probably a bug)")
#     logging.critical("Invalid type (probably a bug): %r", user_input)




# Another approach we could have taken with favdessert.py
def describe_favorite_or_default(category):
    'Describe my favorite food in a category.'
    favorites = {
        "appetizer": "Tandoori",
        "vegetable": "Carrot",
        "drinks": "Soup"
    }

    if category in favorites: # # Contrast with "try/except KeyError".
        message = "My favorite {} is {}.".format(category, favorites[category])
    else:
        message = "I have no favorite {}. I love them all!".format(category)
    return message 
################################################################
# Example finally block to save money or to secure the jobs

# fleet = CloudVMFleet(fleet_config)
# job = BatchJob(job_config)
# try:
#     fleet.start()
#     running_job = fleet.submit_job(job)
#     running_job.wait()
# finally:
#     fleet.terminate()

# Atomic numbers of noble gasses.
nobles = {'He': 2, 'Ne': 10, 'Ar': 18, 'Kr': 36, 'Xe': 54}

def show_element_info(elements: list):
    for element in elements:
        print('Atomic number of {} is {}'.format(element, nobles[element]))

try:
    show_element_info(['Ne', 'Ar', 'Br'])
except KeyError as exc:
    print(exc, type(exc), exc.args, type(exc.args))
    missing_element = exc.args[0]
    print('Missing data for element: ' + missing_element)

# First Version
import os, logging

UPLOAD_ROOT = "/var/www/uploads/"

def create_upload_dirs(username):
    userdir = os.path.join(UPLOAD_ROOT, username)
    try:
        os.makedirs(userdir)
    # First Version start
    except FileExistsError: 
        logging.error("Upload dir for new user already exists")
    # First Version ends
    # Best Version start
    except FileExistsError as exc:
        logging.error("Upload dir already exists: %s", exc.filename)
    # Best Version end

# Raising custom exception as :
#######################################
### raise ExceptionClass(arguments)
#######################################

def positive_int(value):
    number = int(value)
    if number <= 0:
        raise ValueError("Bad value "+ str(value)) # instantiating the ValueError Exception class with string as arguments
    return number

class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def __repr__(self):
        'Renders the object nicely on the prompt.'
        return "Money({self.dollars}, {self.cents})"

# First version
import re
def money_from_string(amount):
    # amount is a string like "$140.75"
    match = re.search(r'^\$(?P<dollars>\d+)\.(?P<cents>\d\d)$', amount)
    # Best version start
    if match is None:
        raise ValueError("Invalid amount: " + repr(amount))
    # Best version end
    dollars = int(match.group('dollars'))
    cents = int(match.group('cents'))
    return Money(dollars, cents)

# First version output
# >>> money_from_string("$12.30")
# Money(12,30)
# >>> money_from_string("Big money")
# Traceback (most recent call last):


# Best version output
# >>> money_from_string("Big money")
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# File "<stdin>", line 6, in money_from_string
# ValueError: Invalid amount: 'Big money'


# Catching and Re-raising Exceptions
# try:
#     do_something()
# except ExceptionClass:
#     handle_exception()
#     raise  # raising the same exception

# eg.
# try:
#     process_user_input(value)
# except ValueError:
#     logging.info("Invalid user input: %s", value)
#     raise



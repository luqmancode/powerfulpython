class Dog:
    pass
dog = Dog()
print(isinstance(dog, object)) # True bydefault, its inherited in python3


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    @full_name.setter
    def full_name(self, value):
        self.first_name, self.last_name = value.split(" ", 1)

    @full_name.deleter
    def full_name(self):
        del self.full_name
    
p1 = Person("Mohamed", "Luqman")
print(p1.full_name) # access as attributes // Mohamed Luqman
# print(p1.full_name()) # TypeError: 'str' object is not callable

# p1.full_name = "Meera banu" # AttributeError: property 'full_name' of 'Person' object has no setter

# After implement of setter
p1.full_name = "Meera Banu"
print(p1.full_name) # Meera Banu

class Coupon:
    def __init__(self, amount):
        self._amount = amount 

    @property   # variable non-public to mutate but only read-only
    def amount(self):
        return self._amount
    
# This code to access the coupon amount but not able to edit from outside
coupon = Coupon(1.25)
print(coupon.amount) # 1.25
# >>> coupon.amount = 1.50
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute

class Ticket:
    def __init__(self, price):
        # self._price = price # First version
        self.price = price # Best Version This prevents assigning -price on initialization on constructor

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        # Only allow positive prices.
        if value < 0:
            raise ValueError("Nice try: " + repr(value))
        self._price = value

t1 = Ticket(10)
print(t1.price)
# t1.price = -10 # ValueError: Nice try: -10

# t2 = Ticket(-10) # self._price = price can assign negative value change to self.price = price
# print(t2.price)

# Properties and Refactoring
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

# opensourced with above code and then later make the below change
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    # This refactoring fixes the error of existing usage of dollars and cents
    @property
    def dollars(self):
        return self.total_cents // 100
    
    @property
    def cents(self):
        return self.total_cents % 100
    
    @dollars.setter
    def dollars(self, new_dollars): # This is add dollars and not initializers
        self.total_cents += new_dollars * 100

    @cents.setter
    def cents(self, new_cents):
        self.total_cents += new_cents 

    @cents.setter
    def cents(self, new_cents):
        self.total_cents += new_cents


money = Money(27, 12)
message = "I have {:d} dollars and {:d} cents."
# This line breaks, because there's no longer
# dollars or cents attributes.
# print(message.format(money.dollars, money.cents)) # AttributeError: 'Money' object has no attribute 'dollars'

# After fix of refactoring property
print(message.format(money.dollars, money.cents))

money.dollars = 100
print(money.dollars)
money.cents = 75
print(message.format(money.dollars, money.cents))
# Refer pg.no:214
print(money.total_cents)

##################################################################################
# In Python, we have the best of both worlds. We make member variables
# public by default, refactoring them as properties if and when we ever need to.
# No one using our code even has to know.
###################################################################################


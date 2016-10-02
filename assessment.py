# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%
def calculate_total_cost(state_abbreviation, cost, tax = .05):
    """Returns total cost of an item, given a state abbreviation, the item cost, and the state tax rate
    """ 
    if state_abbreviation == 'CA':
        tax = .07
    return cost + cost * tax

#print calculate_total_cost('DE', 100)

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".
def is_berry(name):
    """takes in a fruit name as a string and returns boolean if fruit is a strawberry, cherry, or blackberry
    """
    return name == "strawberry" or name == "cherry" or name == "blackberry"
#print is_berry('blackberr')

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.
def shipping_cost(name):
    """takes a fruit name and returns '0' if the fruit is a strawberry, cherry, or blackberry, and returns '5' otherwise
    """
    if is_berry(name):
        return '0'
    else:
        return '5'

#print shipping_cost('strawbery')

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
def is_hometown(town):
    """returns true if town is my hometown, Potomac, and false otherwise
    """
    return town == "Potomac"

#print is_hometown('Potomac')

#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
def full_name(first, last):
    """takes a first and last name as arguments and returns the concatenation of the two names in one string
    """
    return first + " " + last

#print full_name('m', 'd')
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.
def hometown_greeting(hometown, first, last):
    """prints a greeting depending on where the person's hometown is
    """
    if is_hometown(hometown):
        print "Hi, {} {}, we're from the same place!".format(first, last)
    else:
        print "Hi {} {}, where is {}?".format(first, last, hometown)

#hometown_greeting('Poomac', 'm', 'd')


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.
def increment(x = 1):
    """adds a given integer together with my chosen y integer
    """
    def inner_increment(y = 1):
        return x + y
    return inner_increment(20)

#print increment()

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.
addfive = increment(5)
addfive = increment(5)
print addfive

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.
def append_number(number, lst):
    """appends a given number to a given list of numbers
    """
    lst.append(number)
    return lst 

print append_number(5, [8,9,10])

#####################################################################
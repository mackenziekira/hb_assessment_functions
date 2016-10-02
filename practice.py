"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""
################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".
def hello_world():
    """Prints 'Hello World.' Takes no arguments.
    """
    print 'Hello World'


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.
def say_hi(name):
    """Says 'Hi name' based on the string given to it.
    """
    print 'Hi {}'.format(name)

# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.
def print_product(int1, int2):
    """Prints product of two integers.
    """
    print str(int1 * int2)

# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times
def repeat_string(string, integer):
    """Takes a string and an integer and prints the string that many times.
    """

    print "".join([string for item in xrange(integer)])

# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".
def print_sign(integer):
    """prints if a given integer is higher than, lower than, or equal to zero.
    """
    if integer > 0:
        print "Higher than 0"
    elif integer < 0:
        print "Lower than 0"
    elif integer == 0:
        print "Zero"
    else:
        "Please enter a valid input"

# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.
def is_divisible_by_three(integer):
    """Returns a boolean depending on whether a given integer is evenly divisible by 3
    """
    return integer % 3 == 0


# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.
def num_spaces(sentence):
    """Returns the number of spaces in a given sentence
    """
    return len(sentence.split(" "))-1

# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.
def total_meal_price(price, tip_percentage = .15):
    """Given a meal price and a tip percentage, returns the total amount paid. If not given a tip percentage, defaults to 15%
    """
    if tip_percentage >= 0 and tip_percentage < 1:
        try:
            return price + price * tip_percentage 
        except ValueError:
            return "please enter a number for meal price"
    else:
        return "are you sure you gave them that much tip? please enter tip as a decimal conveying the percentage"

# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.
def sign_and_parity(integer):
    """Takes and integer and returns a list of if that integer is positive or negative, and even or odd.
    """
    result = []
    try:
        if integer % 2 == 0:
            result.append("Even")
        else:
            result.append("Odd")
    except TypeError:
        return "please enter a valid integer"

    if integer > 0:
        result.append("Positive")
    elif integer < 0:
        result.append("Negative")
    elif integer == 0:
        result.append("None")

    return result

result = sign_and_parity(-47)
parity = result[0]
sign = result[1]
print sign, parity


################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

def full_title(name, job_title = "Engineer"):
    """Takes a name and job title (optional), returning both in a string
    """
    return job_title + " " + name

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.
def write_letter(recipient_name, recipient_job_title, sender_name):
    """Prints a greeting, given a recipient name, sender name, and recipient job title (optional)
    """
    print "Dear {}, I think you are amazing! Sincerely, {}".format(full_title(recipient_name, recipient_job_title), sender_name)


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

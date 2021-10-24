# Python function to check if a value received from the user input is a number or not.

def is_number(user_input, is_positive=False):
    '''Function to check if a value received from user input is a number or not.
       Supports optional second argument as boolean to checks only positive numbers.'''

    if is_positive == False:
        try:
            user_input = int(user_input)
        except:
            return False
        return True
    else:
        try:
            user_input = int(user_input)
        except:
            return False

        if user_input > 0:
            return True
        else:
            return False


# Python function to repeat a string x times, when x is equal to the number passed.

def repeat(string, number):
    '''Recursive funtion to print x times a string passed as first argument,
       where x is equal to the number passed as second argument.'''

    if number == 0:
        return
    else:
        print(string)
        repeat(string, number - 1)

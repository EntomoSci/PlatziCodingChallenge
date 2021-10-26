
def calculator(string):
    '''This function extracts the digits and operator of a string to calculate them.'''

    characters = string.split()
    number_1 = float(characters[0])
    operator = characters[1]
    number_2 = float(characters[2])

    if operator == '+':
        return number_1 + number_2
    elif operator == '-':
        return number_1 - number_2
    elif operator == '*':
        return number_1 * number_2
    elif operator == '/':
        return number_1 / number_2
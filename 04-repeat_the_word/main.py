# This Python program takes a string and a number from the user and repeats
# the word x times using recursion, when x is equal to the user number.

from modules import is_number, repeat


def run():
    print('''
    Welcome!

    This Python program takes a string and a number from the user and repeats
    the word x times using recursion, when x is equal to the user number.

    ''')
    user_word = input('Enter a word: ')
    while True:
        user_number = input('Enter a number: ')
        if is_number(user_number, True):
            user_number = int(user_number)
            break
        else:
            print('Please enter a number')

    repeat(user_word, user_number)


if __name__ == '__main__':
    run()

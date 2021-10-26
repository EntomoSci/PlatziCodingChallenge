# This Python program imitates the behavior of a calculator.

from modules import calculator


def run():
    welcome_message = open('./program_messages/welcome.txt', 'r')
    print(welcome_message.read())

    while True:
        user_operation = input('\nOperation: ')
        if user_operation.lower() == 'exit':
            print('\nClosing the program...\n')
            return
        print('Result:', calculator(user_operation))


if __name__ == '__main__':
    run()

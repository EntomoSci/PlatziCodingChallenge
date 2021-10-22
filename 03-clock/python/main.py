# This Python program takes the hours and minutes from the user
# and return the seconds of the parameters passed.

from modules import get_seconds


def run():
    welcome_message = open('messages/welcome.txt', 'r')
    final_result = open('messages/result.txt', 'r')
    print(welcome_message.read())

    while True:
        user_decision = input("Hit enter to continue or type 'exit' to close the program: ")
        if user_decision.lower() == 'exit':
            print('\nClosing the program...\n')
            return
        elif user_decision == '':
            break
        else:
            print('Please enter a valid response')

    while True:
        hours = input('\nEnter the hours: ')
        try:
            hours = int(hours)
        except:
            print('Please enter a number')
            continue

        if hours < 0 or hours > 24:
            print('Please enter a valid hour')
        else:
            break

    while True:    
        minutes = input('\nEnter the minutes: ')
        try:
            minutes = int(minutes)
        except:
            print('Please enter a number')
            continue

        if minutes < 1 or minutes > 59:
            print('Please enter a valid quantity of minutes')
        else:
            break

    print(final_result.read().format(hours, minutes, get_seconds(hours, minutes)))


if __name__ == '__main__':
	run()
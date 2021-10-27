# This program imitates the game rock, paper or scissors.
import random


def run():
    welcome_message = open('./program_messages/welcome.txt', 'r')
    print(welcome_message.read())

    game_messages = {
        'user_win': open(, 'r'),
        'user_lose': open(, 'r'),
        'user_victory': open(, 'r'),
        'user_gameover': open(, 'r')
    }

    while True:
        machine_choice = random.randint(2)
        user_choice = input('1: Rock\n2: Paper\n3: Scissors')
        try:
            user_choice = int(user_choice)
        except:
            print('Please enter a valid number')
            continue


if __name__ == '__main__':
    run()

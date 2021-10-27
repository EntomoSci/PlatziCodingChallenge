# This program imitates the game "Rock, paper or scissors".

import random
from modules import get_string_choice, compare_choices


def run():
    messages_path = './program_messages/'
    welcome_message = open(messages_path + 'welcome.txt', 'r')
    print(welcome_message.read())

    game_messages = {
        'welcome': open(messages_path + 'welcome.txt', 'r'),
        'tie': open(messages_path + 'tie.txt', 'r'),
        'user_win': open(messages_path + 'user_win.txt', 'r'),
        'user_lose': open(messages_path + 'user_lose.txt', 'r'),
        'user_victory': open(messages_path + 'user_victory.txt', 'r'),
        'user_gameover': open(messages_path + 'user_gameover.txt', 'r')
    }

    score = {
        'user': 0,
        'machine': 0
    }

    while True:
        machine_choice = random.randint(1,3)
        user_choice = input('1: Rock\n2: Paper\n3: Scissors\n')

        try:
            user_choice = int(user_choice)
        except:
            print('Please enter a valid number')
            continue
        
        user_string_choice = get_string_choice(user_choice)
        machine_string_choice = get_string_choice(machine_choice)

        if compare_choices(user_choice, machine_choice) == 'tie':
            print(game_messages['tie']
            .read()
            .format(user_choice=user_string_choice,
            machine_choice=machine_string_choice))
        elif compare_choices(user_choice, machine_choice) == 'user':
            score['user'] += 1
            print(game_messages['user_win']
            .read()
            .format(user_choice=user_string_choice,
            machine_choice=machine_string_choice,
            user_score=score['user'],
            machine_score=score['machine']))
        else:
            score['machine'] += 1
            print(game_messages['user_lose']
            .read()
            .format(user_choice=user_string_choice,
            machine_choice=machine_string_choice,
            user_score=score['user'],
            machine_score=score['machine']))

        if score['user'] == 3:
            print(game_messages['user_victory'].read())
            return
        elif score['machine'] == 3:
            print(game_messages['user_gameover'].read())
            return


if __name__ == '__main__':
    run()

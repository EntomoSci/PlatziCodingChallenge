

def get_string_choice(number):
    '''This function takes a number between 1 and 3 and returns his equivalent in the game "Rock, paper or scissors"'''

    if number == 1:
        return 'Rock'
    elif number == 2:
        return 'Paper'
    elif number == 3:
        return 'Scissors'


def compare_choices(user_choice, machine_choice):
    '''This function recieve 2 numbers and using "1=Rock, 2=Paper, 3=Scissors" returns the winner'''
    
    if user_choice == machine_choice:
        return 'tie'
    elif user_choice == 1 and machine_choice == 3: # Rock beat Scissors
        return 'user'
    elif user_choice == 2 and machine_choice == 1: # Paper beat Rock
        return 'user'
    elif user_choice == 3 and machine_choice == 2: # Scissors beat Paper
        return 'user'
    else:
        return 'machine'


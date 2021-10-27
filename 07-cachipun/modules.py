

def machine_choice(random_number):
    if random_number == 0:
        return 'Rock'
    elif random_number == 1:
        return 'Paper'
    elif random_number == 2:
        return 'Scissors'


def compare_choices(user_choice, machine_choice, game_messages_dict=None):
    if user_choice == machine_choice:
        pass
    elif user_choice == 1 and machine_choice == 3: # Rock beat Scissors
        pass
    elif user_choice == 2 and machine_choice == 1: # Paper beat Rock
        pass
    elif user_choice == 3 and machine_choice == 2: # Scissors beat Paper
        pass
    else:
        return 'machine'

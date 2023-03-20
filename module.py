from random import randint


def set_enemy_health():
    return randint(80, 120)


def get_light_attack():
    return randint(2, 5)


def get_medium_attack():
    return randint(15, 25)


def get_heavy_attack():
    return randint(30, 40)


def compare_valumes(enemy_health, user_total_attack):
    point_difference = abs(enemy_health - user_total_attack)
    if 0 <= point_difference <= 10:
        return True
    return False


def get_user_attack():
    total = 0
    attacks_types = {
        'light': get_light_attack,
        'medium': get_medium_attack,
        'heavy': get_heavy_attack,
    }

    for i in range(5):
        input_attack = input('Enter the type of attack: ').lower()
        attack_value = attacks_types[input_attack]()
        print(f'Number of attack points: {attack_value}.')
        total += 1
    return total


def run_game():
    user_total_attack = get_user_attack()
    enemy_health = set_enemy_health()
    print(f'Damage done to the enemy {user_total_attack}.')
    print(f'Enemy health points after your attack: {enemy_health}.')
    if compare_valumes(enemy_health, user_total_attack):
        print('Hooray! Victory is yours!')
    else:
        print('No luck this time :( Battle lost.')
    yes_no = {
        'Y': True,
        'N': False,
    }
    replay = input('To play again, enter "y"; '
                   'if you don\'t want to continue, enter "n": ')
    if replay not in yes_no:
        raise ValueError('That command is not in the game.')
    return yes_no[replay]

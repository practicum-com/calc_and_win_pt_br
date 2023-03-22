from random import randint


def set_enemy_health():
    return randint(80, 120)


def get_lite_attack():
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
        'leve': get_light_attack,
        'médio': get_medium_attack,
        'pesado': get_heavy_attack,
    }

    for i in range(5):
        input_attack = input('Insira o tipo de ataque: ').lower()
        attack_value = attacks_types[input_attack]()
        print(f'O número de pontos de ataque: {attack_value}.')
        total += 1
    return total


def run_game():
    user_total_attack = get_user_attack()
    enemy_health = set_enemy_health()
    print(f'O dano causado ao inimigo é igual a {user_total_attack}.')
    print(f'Pontos de saúde do inimigo depois do ataque: {enemy_health}.')
    if compare_valumes(enemy_health, user_total_attack):
        print('Viva! A vitória é sua!')
    else:
        print('Desta vez, a sorte não estava ao seu lado :( Batalha perdida.')
    yes_no = {
        'Y': True,
        'N': False,
    }
    replay = input('Para jogar novamente, insira "y"; '
                   'se você não quiser continuar o jogo, insira "n": ')
    if replay not in yes_no:
        raise ValueError('Este comando não existe no jogo.')
    return yes_no[replay]

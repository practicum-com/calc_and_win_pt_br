from module import run_game

INTRO = '''CALCULE E VENÇA!
Carregando o jogo...

Você tem 5 turnos para ganhar um número de pontos de dano
que esteja dentro do intervalo de +/– 10 do valor de saúde do seu inimigo.

O valor de saúde do inimigo é gerado aleatoriamente
dentro do intervalo de 80 a 120 pontos.

Você tem três tipos de ataques à sua disposição:
leve — dano de 2 a 5 pontos
médio — dano de 15 a 25 pontos
pesado — dano de 30 a 40 pontos
VAMOS PARA A VITÓRIA!!!
'''

def main():
    print(INTRO)
    replay = True
    while replay:
        replay = run_game()

if __name__ == '__main__':
    main()

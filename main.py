from module import run_game

INTRO = '''CALCULATE AND WIN!
Loading...

You have 5 turns to do damage that falls within the
range of +-10 points of the health value of the enemy.

The enemy's health value is randomly
generated between 80 and 120 points.

You have three types of attacks at your disposal:
light — damage from 2 to 5 points
medium — damage from 15 to 25 points
heavy — damage from 30 to 40 points
GO FOR THE WIN!!!
'''

def main():
    print(INTRO)
    replay = True
    while replay:
        replay = run_game()

if __name__ == '__main__':
    main()

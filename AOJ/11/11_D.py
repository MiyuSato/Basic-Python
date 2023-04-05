import itertools


class Dice:
    def __init__(self, dice):
        self.dice = dice

    def __str__(self):
        return str(self.dice)

    def moveset(self, d):
        moves = {'N': '152304', 'S': '402351', 'E': '310542', 'W': '215043'}
        self.dice = [self.dice[int(i)] for i in moves[d]]


def judge(dice1, dice2):
    flg = False
    for d in 'NNNNEEE':
        dice1.moveset(d)
        if int(dice1.dice[0]) == int(dice2.dice[0]):
            dice1.moveset('N')
            dice2.moveset('N')
            for d in 'EEEE':
                dice1.moveset(d)
                if dice1.dice == dice2.dice:
                    flg = True
    return flg


flg = False
dices = []

n = int(input())
dices = [Dice(input().split()) for _ in range(n)]
for pair in itertools.combinations(dices, 2):
    if judge(*pair):
        flg = True
        break
print('No' if flg else 'Yes')

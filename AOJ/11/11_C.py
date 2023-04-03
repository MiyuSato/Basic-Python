class Dice:
    def __init__(self, dice):
        self.dice = dice

    def moveset(self, d):
        moves = {'N': '152304', 'S': '402351', 'E': '310542', 'W': '215043'}
        self.dice = [self.dice[int(i)] for i in moves[d]]


flg = False
dice1 = Dice(input().split())
dice2 = Dice(input().split())
for d in 'NNNNEEE':
    dice1.moveset(d)
    if int(dice1.dice[0]) == int(dice2.dice[0]):
        dice1.moveset('N')
        dice2.moveset('N')
        for d in 'EEEE':
            dice1.moveset(d)
            if dice1.dice == dice2.dice:
                flg = True
print('Yes' if flg else 'No')

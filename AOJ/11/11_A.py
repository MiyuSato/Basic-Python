class Dice:
    def __init__(self, dice):
        self.dice = dice

    def moveset(self, directions):
        moves = {'N': '152304', 'S': '402351', 'E': '310542', 'W': '215043'}
        for d in directions:
            self.dice = [self.dice[int(i)] for i in moves[d]]
            print(self.dice[0])


dice1 = Dice(input().split())
dice1.moveset(input())

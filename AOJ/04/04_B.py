import math as m


def calc(r):
    S = r * r * m.pi
    L = 2 * r * m.pi
    print(f'{S} {L}')


x = float(input())
calc(x)

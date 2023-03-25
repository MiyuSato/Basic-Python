cards = []
for chr in 'SHCD':
    for i in range(1, 14):
        cards.append(f'{chr} {i}')

n = int(input())

for i in range(n):
    cards.remove(input())
for card in cards:
    print(card)

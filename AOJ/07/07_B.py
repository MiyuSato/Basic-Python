import itertools

while True:
    i = 0
    a, b = map(int, input().split())
    if a == b == 0:
        break
    for c in itertools.combinations(range(1, a+1), 3):
        if sum(c) == b:
            i += 1
    print(i)

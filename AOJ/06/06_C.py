rooms = [[[0] * 10 for i in range(3)] for j in range(4)]

n = int(input())

for i in range(n):
    b, f, r, v = map(int, input().split())
    rooms[b-1][f-1][r-1] += v

for i in range(4):
    for j in range(3):
        print('', *rooms[i][j])
    if i < 3:
        print('#' * 20)

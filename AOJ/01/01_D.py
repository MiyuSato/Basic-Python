x = int(input())
h = x // 3600
m = x // 60 % 60
s = x % 60
print(h, m, s, sep=':')

def calc(x, y, op):
    x, y = int(x), int(y)
    if op == '+':
        print(x + y)
    elif op == '-':
        print(x - y)
    elif op == '*':
        print(x * y)
    elif op == '/':
        print(x // y)


while True:
    a, op, b = input().split()
    if op == '?':
        break
    calc(a, b, op)

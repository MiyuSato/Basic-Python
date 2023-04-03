while True:
    a = input()
    if a == '0':
        break
    print(sum(int(n) for n in a))

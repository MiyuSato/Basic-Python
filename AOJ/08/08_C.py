import sys
a = sys.stdin.read()
for i in range(97, 123):
    print(f'{chr(i)} : {a.count(chr(i))+a.count(chr(i-32))}')

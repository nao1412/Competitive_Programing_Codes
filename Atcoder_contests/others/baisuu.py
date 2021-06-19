a, b = map(int, input().split())
c = a * b
d = c % 2
if d == 0:
    print('Even')
else:
    print('Odd')
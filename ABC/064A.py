r, g, b = map(int, input().split())
if (10*g + b) % 4 == 0:
    print('YES')
else:
    print('NO')
a, b = map(int, input().split())
if a <= 9 and a >= 0 and b <= 9 and b >= 0:
    print(a*b)
else:
    print('-1')
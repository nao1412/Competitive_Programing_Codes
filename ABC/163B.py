n, m = map(int, input().split())
a = sum(list(map(int, input().split())))
if n >= a:
    print(n-a)
else:
    print('-1')
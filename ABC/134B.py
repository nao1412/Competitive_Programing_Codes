n, d = map(int, input().split())
a = n % (d*2+1)
if a == 0:
    print(int(n / (d*2+1)))
else:
    print(int(n/(d*2+1)) + 1)
n, k = map(int, input().split())
if n <= k-1:
    print(1)
else:
    n -= (k-1)
    for s in range(1, 1000000000):
        if n > (k**s)*(k-1):
            n -= (k**s)*(k-1)
        else:
            print(s+1)
            break

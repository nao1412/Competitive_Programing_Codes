n, k, m = map(int, input().split())
a = list(map(int, input().split()))
if sum(a) >= n*m:
    print(0)
else:    
    if n*m - sum(a) <= k:
        print(n*m - sum(a))
    else:
        print('-1')
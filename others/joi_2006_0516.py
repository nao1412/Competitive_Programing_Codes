while True: 
    n, k = map(int, input().split())
    if n == 0: break
    a = [int(input()) for _ in range(n)]

    cs = [0]*(n+1)
    for i in range(n):
        cs[i+1] = cs[i] + a[i]

    ans = -10**16
    for i in range(n-k+1):
        ans = max(ans, cs[i+k]-cs[i])

    print(ans)
n, d = map(int, input().split())
ans = [-1]*3
for x in range(n+1):
    for y in range(n-x+1):
        if d == 10000*x + 5000*y + 1000*(n-x-y):
            ans = [x, y, n-x-y]
        # if zd//1000 == n-x-y:
        #     ans[0] = x
        #     ans[1] = y
        #     ans[2] = zd//1000
        #     break
print(*ans)
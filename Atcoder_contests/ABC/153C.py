n, k = map(int, input().split())
h = list(map(int, input().split()))
g = sorted(h, reverse = True)
ans = 0
for i in range(k, n):
    ans += g[i]
print(ans)

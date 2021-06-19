n, m, x = map(int, input().split())
c = [0]*n
memo = [0]*m

for i in range(n):
    c[i] = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += c[i][0]
    for j in range(m):
        memo[j] = c[i][j+1]



print(ans)

def dfs(price, cnt):
    if cnt == n:
        if all memo >= 10:
            ans = min(ans, price)
            return ans
    for 
    
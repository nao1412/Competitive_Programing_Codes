n, m = map(int, input().split())
a, b = [0]*m, [0]*m
for i in range(m):
    a[i], b[i] = map(int, input().split())
ans = [0]*n
c = a + b
for i in range(1,n+1):
    ans[i-1] = c.count(i)

for i in range(n):
    print(ans[i])
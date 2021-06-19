A, B, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = [0]*m
y = [0]*m
c = [0]*m
for i in range(m):
    x[i], y[i], c[i] = map(int ,input().split())

ans = min(a) + min(b)
for i in range(m):
    ans = min(ans, a[x[i]-1] + b[y[i]-1] - c[i])

print(ans)
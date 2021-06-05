n = int(input())
t = list(map(int, input().split()))
m = int(input())
p = [0]*m
x = [0]*m
for i in range(m):
    p[i], x[i] = map(int, input().split())

ts = sum(t)
for i in range(m):
    ans = ts - t[p[i]-1] + x[i]
    print(ans)
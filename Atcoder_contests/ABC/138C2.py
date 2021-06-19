n = int(input())
v = list(map(int, input().split()))

vs = sorted(v)
ans = vs[0]
for i in range(1,n):
    ans = (ans + vs[i]) / 2

print(ans)

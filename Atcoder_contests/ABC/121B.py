n, m ,c = map(int, input().split())
b = list(map(int, input().split()))
a = []
for i in range(n):
    aa = list(map(int, input().split()))
    a.append(aa)

s = 0
cnt = 0
for i in range(n):
    for j in range(m):
        s += a[i][j]*b[j]
    if s + c > 0:
        cnt += 1
        s = 0
    else:
        s = 0

print(cnt)

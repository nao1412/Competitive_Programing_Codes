n, m = map(int, input().split())
a, b = [0]*n, [0]*n
c, d = [0]*m, [0]*m
for i in range(n):
    a[i], b[i] = map(int,input().split())
for i in range(m):
    c[i], d[i] = map(int,input().split())


for i in range(n):
    l = 10 ** 9
    for j in range(m):
        if abs(a[i] - c[j]) + abs(b[i] - d[j]) < l:
            l = abs(a[i] - c[j]) + abs(b[i] - d[j])
            idx = j + 1

    print(idx)
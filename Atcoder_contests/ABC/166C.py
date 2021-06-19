n, m = map(int, input().split())
h = list(map(int, input().split()))
h2 = [0]*n
a = [0]*m
b = [0]*m
for i in range(m):
    a[i], b[i] = map(int, input().split())
for j in range(m):
    if h[a[j]-1] < h[b[j]-1]:
        h2[a[j]-1] = 1
    elif h[a[j]-1] > h[b[j]-1]:
        h2[b[j]-1] = 1
    else:
        h2[a[j]-1] = 1
        h2[b[j]-1] = 1

print(h2.count(0))
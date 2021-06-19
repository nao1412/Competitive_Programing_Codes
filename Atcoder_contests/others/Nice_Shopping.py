#Nicee Shopping B
a, b, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = []
y = []
c = []
for i in range(m):
    xi, yi, ci = map(int, input().split())
    x.append(xi)
    y.append(yi)
    c.append(ci)
ans = min(a) + min(b)
for j in range(m):
    kk = a[x[j]-1] + b[y[j]-1] - c[j]
    if ans > kk:
        ans = kk
print(ans) 
a, b = map(int, input().split())
c = 0
d = 0
for i in range(b):
    c += (10 ** i) * a
for j in range(a):
    d += (10 ** j) * b
k = [str(c),str(d)]
k.sort()
print(k[0])
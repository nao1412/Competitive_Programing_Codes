#ABC 134C
n = int(input())
a = [int(input()) for _ in range(n)]
h = sorted(a)
b = h[-1]
c = h[-2]
for i in range(n):
    if a[i] != b:
        print(b)
    else:
        print(c)
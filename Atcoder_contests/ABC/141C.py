n, k, q = map(int,input().split())
a = []
for i in range(q):
    b = int(input())
    a.append(b)
pnt = [0] * n
for x in a:
    pnt[x-1] += 1
for j in range(n):
    if pnt[j] > q-k:
        print('Yes')
    else:
        print('No')
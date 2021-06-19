n, m = map(int, input().split())
l, r = [0]*m, [0]*m
for i in range(m):
    l[i], r[i] = map(int, input().split())

ll = max(l)
rr = min(r)
if rr-ll >= 0:
    print(rr-ll+1)
else:
    print(0)
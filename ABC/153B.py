h, n = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(a)
cnt = 0
for i in range(n):
    cnt += b[i]
if cnt >= h:
    print('Yes')
else:
    print('No')
#161B
n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if a[i] >= sum(a) / (4*m):
        cnt += 1
if cnt >= m:
    print('Yes')
else:
    print('No')
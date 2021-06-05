n, k = map(int,input().split())
h = list(map(int, input().split()))
cnt = 0
for i in range(n):      # for i in h:
    if h[i] >= k:       # if i >= k:
        cnt += 1
print(cnt)
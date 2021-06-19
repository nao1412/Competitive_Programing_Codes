h, w = map(int, input().split())
a = []
cnt = 0
for i in range(h):
    aa = list(map(str, input().split()))
    if aa != ['.'*w]:
        cnt += 1
        a.append(aa)

for i in range(w):
    d = 0
    for j in range(cnt):
        if a[j][i] == '.':
            d += 1
    if d = cnt:
        
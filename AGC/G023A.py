n = int(input())
a = list(map(int, input().split())) # 横入力

cs = [0]
aa = 0
for i in range(n):
    aa += a[i]
    cs.append(aa)

cs.sort()
cnt = 1
ans = 0
for i in range(n):
    if cs[i] == cs[i+1]:
        cnt += 1
    else:
        if cnt != 1:
            ans += cnt*(cnt-1)//2
            cnt = 1
if cnt != 1:
    ans += cnt*(cnt-1)//2
print(ans)
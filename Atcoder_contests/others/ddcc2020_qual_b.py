n = int(input())
a = list(map(int, input().split())) # 横入力

x = [0]
aaa = 0
aa = sum(a)
# y = [aa]
for i in range(n):
    aaa += a[i]
    x.append(aaa)
    # aa -= a[i]
    # y.append(aa)

ans = 202020202020
for i in range(n+1):
    ans = min(ans, abs(aa - x[i]*2))

print(ans)
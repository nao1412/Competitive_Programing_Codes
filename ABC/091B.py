n = int(input())
s = [input() for _ in range(n)] # 縦入力
m = int(input())
t = [input() for _ in range(m)] # 縦入力

ans = 0
for i in s:
    ans = max(ans, s.count(i) - t.count(i))

print(ans)
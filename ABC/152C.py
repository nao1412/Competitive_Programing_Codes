n = int(input())
p = list(map(int, input().split()))
cnt = 0
for _ in p:  #p[i]よりも小さいものが出てきたらだめ
    if _ <= n:
        cnt += 1
        n = _
print(cnt)
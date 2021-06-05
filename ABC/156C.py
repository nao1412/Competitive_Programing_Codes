n = int(input())
x = list(map(int, input().split()))
ans = 10 ** 9
for p in range(0, 101):
    cnt = 0
    for i in x:
        cnt += (i-p)**2
    ans = min(ans, cnt)
print(ans)
n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0
for i in range(1,n+1):
    ans += a[-2*i]

print(ans)
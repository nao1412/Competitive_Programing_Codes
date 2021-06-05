n = int(input())
a = list(map(int, input().split()))

a = sorted(a, reverse=True)
ans = a[0]
m = 1
for i in range(1,n):
    m *= -1
    ans += m * a[i]

print(ans)
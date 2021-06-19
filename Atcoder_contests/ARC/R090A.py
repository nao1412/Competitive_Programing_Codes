n = int(input())
a = []
for i in range(2):
    aa = list(map(int, input().split()))
    a.append(aa)

ans = 0
for i in range(n):
    ans = max(ans, sum(a[0][:i+1])+sum(a[1][i:n]))

print(ans)
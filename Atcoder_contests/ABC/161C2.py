n, k = map(int, input().split())

z = n%k
if k == 0:
    ans = 0
else:
    ans = min(z,k-z)

print(ans)
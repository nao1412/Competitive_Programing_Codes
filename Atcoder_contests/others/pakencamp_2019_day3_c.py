n, m = map(int, input().split())
a = []
for i in range(n):
  aa = list(map(int, input().split()))
  a.append(aa)

ans = 0
for i in range(m-1):
  for j in range(i+1, m):
    p = 0
    for k in range(n):
      p += max(a[k][i], a[k][j])
    ans = max(ans, p)

print(ans)
n, m = map(int, input().split())
g = [[-1]*n for _ in range(m)]
for i in range(m):
  s = list(map(int, input().split()))
  s.pop(0)
  for j in s:
    g[i][j-1] = 1
p = list(map(int, input().split()))

ans = 0
for i in range(2**n):
  switch = [0]*n
  for j in range(n):
    if ((i >> j) & 1):
      switch[j] = 1
  
  flag = True
  for j in range(m):
    cnt = 0
    for k in range(n):
      if g[j][k] == switch[k]:
        cnt += 1
    if cnt % 2 != p[j]:
      flag = False
  if flag:
    ans += 1

print(ans)
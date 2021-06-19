n, m , q = map(int, input().split())
pn = [0]*n
pm = [n]*m
toita = [[0]*m for _ in range(n)]
for i in range(q):
  s = list(map(int, input().split()))
  if s[0] == 1:
    print(pn[s[1]-1])
  if s[0] == 2:
    pm[s[2]-1] -= 1
    toita[s[1]-1][s[2]-1] = 1
 
    for k in range(n):
      point = 0
      for j in range(m):
        if toita[k][j] == 1:
          point += pm[j]
      pn[k] = point

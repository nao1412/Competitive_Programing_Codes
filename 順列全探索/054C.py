n, m = map(int, input().split())
graph = [[]*n for _ in range(n)]
for i in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  graph[a].append(b)
  graph[b].append(a)

import itertools
np = [i for i in range(1,n)]
p = list(itertools.permutations(np))
ans = 0
for pi in p:
  flag = True
  sta = 0
  for j in range(n-1):
    if pi[j] not in graph[sta]:
      flag = False
      break
    else:
      sta = pi[j]
  if flag: ans += 1

print(ans)
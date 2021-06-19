n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)

from collections import deque
arrow = [0]*n
def bfs(u, n):
    queue = deque([u]) # uからの距離の初期化
    d = [False]*n
    d[u] = 1
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i]:continue
            d[i] = True
            arrow[i] = v
            queue.append(i)
    return arrow

ans = bfs(0, n)
print('Yes')
for i in range(1,n):
    print(ans[i]+1)


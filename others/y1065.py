n,m = map(int, input().split())
x,y = map(int, input().split())
p, q = [0]*n, [0]*n
P, Q = [0]*m, [0]*m
for i in range(n):
    p[i], q[i] = map(int, input().split())
for i in range(m):
    P[i], Q[i] = map(int, input().split())

from collections import deque


def bfs(u, y, n):
    queue = deque([u]) # uからの距離の初期化
    d = [False]*n
    d[u] = 1
    while queue != y:
        v = queue.popleft()
        for i in g[v]:
            if d[i]:continue
            d[i] = True
            queue.append(i)
    return ans

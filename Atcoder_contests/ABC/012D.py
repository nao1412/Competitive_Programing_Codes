import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
import math
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
INF = 100100100100100
from heapq import heappop, heappush
def main():
  n, m = MI()
  g = [[] for _ in range(n)]
  for _ in range(m):
    a, b, t = MI()
    a -= 1; b -= 1
    g[a].append((b, t))
    g[b].append((a, t))
  # print(g)
  def dijkstra(s, n):
    d = [INF]*n
    hq = [(0, s)]

    d[s] = 0
    seen = [False]*n
    while hq:
      dist, node = heappop(hq)
      seen[node] = True
      for to, cost in g[node]:
        if seen[to] == False and dist + cost < d[to]:
          d[to] = dist + cost
          heappush(hq, (d[to], to))
    return max(d)
  ans = 100100100100100
  for i in range(n):
    # print(dijkstra(i, n))
    ans = min(ans, dijkstra(i, n))
  print(ans)
if __name__ == '__main__':
  main()
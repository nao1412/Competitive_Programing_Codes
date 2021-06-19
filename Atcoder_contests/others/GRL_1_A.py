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
from heapq import heappush, heappop

def main():
  V, E, r = MI()
  graph = [[] for _ in range(V)]
  for _ in range(E):
    s, t, d = MI()
    graph[s].append((t, d))

  def dijkstra(s, n): # 始点、ノード数
    dist = [INF]*n
    hq = [(0, s)] # (distance, node)

    dist[s] = 0
    seen = [False]*n # ノードが確定かどうか pairにすればルートを記録できる
    while hq:
      d, node = heappop(hq) # 最小値を持つノードを取り出す。key=1はノード
      seen[node] = True
      for to, cost in graph[node]: # 最小値を持つノードと隣接するノードに対して探索
        if seen[to] == False and d + cost < dist[to]:
          dist[to] = d + cost
          heappush(hq, (dist[to], to))
    return dist

  ans = dijkstra(r, V)
  for i in ans:
    if i != INF: print(i)
    else: print('INF')
if __name__ == '__main__':
  main()

INF = 100100100
from heapq import heappush, heappop
graph = []
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

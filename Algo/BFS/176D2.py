# 01-BFS

import sys
import math
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
from collections import deque
INF = 100100100
def main():
  h, w = MI()
  sy, sx = MI()
  gy, gx = MI()
  sy -= 1; sx -= 1; gx -= 1; gy -= 1
  m = ['#'*(w+4) for _ in range(2)]
  for _ in range(h):
    m.append(list('##' + S() + '##'))
  for _ in range(2):
    m.append('#'*(w+4))

  q = deque()
  dist = [[INF]*(w+4) for _ in range(h+4)]
  q.append((sx+2, sy+2))
  dist[sy+2][sx+2] = 0
  d = 0
  while q:
    x, y = q.popleft()
    d = dist[y][x]
    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
      nx = x + dx; ny = y + dy
      # if 0 < nx <= w or 0 < ny <= h: continue
      if m[ny][nx] == '#' or dist[ny][nx] <= d: continue
      dist[ny][nx] = d
      q.appendleft((nx, ny))

    for dx in [-2, -1, 0, 1, 2]:
      for dy in [-2, -1, 0, 1, 2]:
        nx = x + dx; ny = y + dy
        # if 0 < nx <= w or 0 < ny <= h: continue
        if m[ny][nx] == '#' or dist[ny][nx] <= d+1: continue
        dist[ny][nx] = d + 1
        q.append((nx, ny))
        
  # print(dist)
  ans = dist[gy+2][gx+2]
  if ans == INF: print(-1)
  else: print(ans)
if __name__ == '__main__':
  main()
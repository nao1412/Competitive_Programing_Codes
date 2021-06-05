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
def main():
  R, C = MI()
  sy, sx = MI()
  gy, gx = MI()
  m = []
  for _ in range(R):
    m.append(list(S()))

  q = deque()
  d = [[-1]*C for _ in range(R)]
  sx -= 1
  sy -= 1
  d[sy][sx] = 0
  q.append((sx, sy))
  while q:
    x, y = q.popleft()
    for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
      nx, ny = x + dx, y + dy
      if m[ny][nx] == '#': continue
      if d[ny][nx] != -1: continue
      d[ny][nx] = d[y][x] + 1
      q.append((nx, ny))
  print(d[gy-1][gx-1])  

if __name__ == '__main__':
  main()
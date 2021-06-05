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
  h, w = map(int, input().split())
  m = [input() for _ in range(h)]

  q = deque()
  d = [[-1]*w for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if m[i][j] == '#':
        d[i][j] = 0
        q.append((i, j))
  ans = 0
  while q:
    y, x = q.popleft()
    ans = d[y][x]
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
      nx, ny = x + dx, y + dy
      if not 0 <= nx < w or not 0 <= ny < h or d[ny][nx] != -1: continue
      if m[ny][nx] == '#': continue
      # if d[ny][nx] != -1: continue
      d[ny][nx] = ans + 1
      q.append((ny, nx))
  print(ans)
if __name__ == '__main__':
  main()
import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
from collections import deque
def main():
  h, w = MI()
  m = [S() for _ in range(h)]
  
  q = deque()
  q.append((0,0))
  d = [[-1]*w for _ in range(h)]
  d[0][0] = 0
  cnt = 0

  for i in range(h):
    for j in range(w):
      if m[i][j] == '.': cnt += 1

  while q:
    x, y = q.popleft()
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
      nx = x + dx; ny = y + dy
      if not 0 <= nx < w or not 0 <= ny < h or d[ny][nx] != -1: continue
      if m[ny][nx] == '#': continue
      d[ny][nx] = d[y][x] + 1
      q.append((nx, ny))
  # print(d)
  if d[h-1][w-1] == -1: ans = -1
  else: ans = cnt - d[h-1][w-1] - 1
  print(ans)

if __name__ == '__main__':
  main()
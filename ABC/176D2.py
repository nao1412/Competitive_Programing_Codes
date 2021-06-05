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
  h, w = MI()
  sy, sx = tuple(MI())
  gy, gx = tuple(MI())
  m = ['$'*(w+4) for _ in range(2)]
  for _ in range(h):
    m.append(list('$$' + S() + '$$'))
  for _ in range(2):
    m.append('$'*(w+4))

  q = deque()
  ans = [[-1]*w for _ in range(h)]
  q.append((sx, sy))
  ans[sy][sx] = 0

  while q:
    x, y = q.popleft()
    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
      

if __name__ == '__main__':
  main()
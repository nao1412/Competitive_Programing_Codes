import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
import math
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
from collections import deque

def main():
  n, m = MI()
  g = [[] for _ in range(n)]
  for _ in range(m):
    a, b = MI()
    a -= 1; b -= 1
    g[a].append(b)
  # print(g)
  ans = 0
  q = deque()
  for i in range(n):
    flag = [0]*n
    flag[i] = 1
    q.append(g[i])
    while q:
      now = q.popleft()
      # print(now)
      for c in now:
        if flag[c]: continue
        q.append(g[c])
        flag[c] = 1
    # print(flag)
    ans += sum(flag)
  print(ans)
if __name__ == '__main__':
  main()

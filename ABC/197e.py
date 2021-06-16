import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
import math
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n = I()
  INF = 1001001001
  l = [INF]*n; r = [-INF]*n
  for _ in range(n):
    x, c = MI()
    c -= 1
    l[c] = min(l[c], x)
    r[c] = max(r[c], x)
  
  d = []
  d.append((0,0))
  for i in range(n):
    if l[i] != INF: d.append((l[i], r[i]))
  d.append((0,0))

  dp = [0,0]
  inf = 1<<60
  for i in range(1, len(d)):
    p = [inf, inf]
    dp, p = p, dp
    l = d[i][0]; r = d[i][1]
    for j in range(2):
      dp[0] = min(dp[0], p[j] + abs(d[i-1][j] - r) + (r-l))
      dp[1] = min(dp[1], p[j] + abs(d[i-1][j] - l) + (r-l))
  print(dp[1])

if __name__ == '__main__':
  main()

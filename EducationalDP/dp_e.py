import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
import math
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
INF = 1001001001001
def main():
  N, W = MI()
  wei = []
  val = []
  for _ in range(N):
    ww, vv = MI()
    wei.append(ww)
    val.append(vv)

  dp = [[INF]*(max(val)*N+1) for _ in range(N+1)]
  dp[0][0] = 0
  for i in range(N):
    for j in range(max(val)*N+1):
      if j >= val[i]: dp[i+1][j] = min(dp[i][j], dp[i][j-val[i]] + wei[i])
      else: dp[i+1][j] = dp[i][j]
  # print(dp)
  for i in range(max(val)*N+1):
    if dp[N][i] <= W: ans = i
  print(ans)
if __name__ == '__main__':
  main()

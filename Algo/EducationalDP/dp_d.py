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
  N, W = MI()
  wei = []
  val = []
  for _ in range(N):
    ww, vv = MI()
    wei.append(ww)
    val.append(vv)

  dp = [[0]*(W+1) for _ in range(N+1)]
  for i in range(N):
    for j in range(W+1):
      if j >= wei[i]: dp[i+1][j] = max(dp[i][j-wei[i]] + val[i], dp[i][j])
      else: dp[i+1][j] = dp[i][j]
  # print(dp)
  print(dp[N][W])
if __name__ == '__main__':
  main()

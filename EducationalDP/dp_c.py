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
  v = [[] for _ in range(n)]
  for _ in range(n):
    v[_] = LI()
  dp = [[0]*3 for _ in range(n)]
  for i in range(3):
    dp[0][i] = v[0][i]
  
  for i in range(1, n):
    for j in range(3):
      for k in range(3):
        if j == k: continue
        dp[i][j] = max(dp[i][j], dp[i-1][k] + v[i][j])
  print(max(dp[-1]))
if __name__ == '__main__':
  main()

# A = [input() for i in range(H)]
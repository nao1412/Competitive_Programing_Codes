import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  # dp table ver.
  n = I()
  dp = [[0,0] for _ in range(n+1)]
  for i in range(2): dp[0][i] = 1 # x0の時の場合の数は 1... y = 0 or 1
  for i in range(n):
    s = S()
    for j in range(2):
      for x in range(2):
        nj = j
        if s == 'AND': nj &= x
        else: nj |= x
        dp[i+1][nj] += dp[i][j] # 一個前の場合の数を遷移先の0 or 1に足す
    # print(dp)
  print(dp[n][1])

  # 簡略化 ver.
  n = I()
  dp = [1,1]
  for _ in range(n):
    s = S()
    p = [0,0]
    dp, p = p, dp
    for j in range(2):
      for x in range(2):
        nj = j
        if s == 'AND': nj &= x
        else: nj |= x
        dp[nj] += p[j]
  print(dp[1])
if __name__ == '__main__':
  main()
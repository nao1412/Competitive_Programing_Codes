import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
import math
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
def H(n): return [input() for i in range(n)]
mod = 10**9 + 7

def main():
  s = S()
  t = S()
  
  ls = len(s)
  lt = len(t)

  dp = [[0]*(lt+1) for _ in range(ls+1)]
  # print(dp)
  for i in range(ls):
    for j in range(lt):
      if s[i] == t[j]: dp[i+1][j+1] = dp[i][j] + 1
      else: dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

  ans = ''
  i = ls
  j = lt
  while i != 0 and j != 0:
    if dp[i][j] == dp[i][j-1]: j -= 1
    elif dp[i][j] == dp[i-1][j]: i -= 1
    else:
      i -= 1; j -= 1
      ans += s[i]
      
  print(ans[::-1])
if __name__ == '__main__':
  main()

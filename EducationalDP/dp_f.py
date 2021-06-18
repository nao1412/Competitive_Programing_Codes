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

  # dp = [[0]*(ls+1) for _ in range(lt+1)]
  # for i in range(1,ls+1):
  #   for j in range(1, lt+1):
  #     if s[i] == t[j]: dp[i][j] = dp[i-1][j-1] + 1
  #     else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  
  # l = dp[ls][lt]
  # i = ls-1
  # j = lt-1

  # ans = ['' for _ in range(l)]
  # while l > 0:
  #   if s[i] == t[j]:
  #     ans[l] = s[i]
  #     i -= 1; j -= 1; l -= 1
  #   elif dp[i][j] == dp[i-1][j]: i -= 1
  #   else: j -= 1
  # print(''.join(ans))
if __name__ == '__main__':
  main()

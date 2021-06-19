import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n, k = MI()
  h = LI()
  dp = [0]*n
  for i in range(1,n):
    dp[i] = dp[i-1] + abs(h[i]-h[i-1])
    for j in range(1, k+1):
      if i-j >= 0:
        dp[i] = min(dp[i], dp[i-j] + abs(h[i]-h[i-j]))
  print(dp[-1])
if __name__ == '__main__':
  main()

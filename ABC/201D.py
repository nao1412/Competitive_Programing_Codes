import sys
sys.setrecursionlimit(10**8)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  h, w = MI()
  a = []
  for i in range(h):
    a.append(S())

  def cnt(i, j):
    if a[i][j] == '+': return 1
    else: return -1

  dp = [[-10**7]*w for _ in range(h)]
  dp[-1][-1] = 0
  for i in reversed(range(h)):
    for j in reversed(range(w)):
      if i+1 < h:
        dp[i][j] = max(dp[i][j], cnt(i+1, j) - dp[i+1][j])
      if j+1 < w:
        dp[i][j] = max(dp[i][j], cnt(i, j+1) - dp[i][j+1])
      # print(dp)

  if dp[0][0] > 0: ans = 'Takahashi'
  elif dp[0][0] == 0: ans = 'Draw'
  else: ans = 'Aoki'
  print(ans)
if __name__ == '__main__':
  main()
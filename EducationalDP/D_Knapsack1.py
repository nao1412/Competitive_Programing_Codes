def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n, W = I()
  w, v = [0]*n, [0]*n
  for i in range(n):
    w[i], v[i] = I()

  dp = [[0]*(W+1) for _ in range(n+1)]
  for i in range(1,n+1):
    for j in range(1, W+1):
      if j >= w[i-1]:
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
      else:
        dp[i][j] = dp[i-1][j]
  print(dp[-1][-1])
if __name__ == '__main__':
  main()
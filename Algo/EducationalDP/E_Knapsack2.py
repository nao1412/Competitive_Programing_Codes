def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  N, W  = I()
  w, v = [0]*N, [0]*N
  for i in range(N):
    w[i], v[i] = I()
  N += 1
  max_j = max(v)*N # なんでNかけた？ -> n 個maxを選んだ時に対応できるように
  # print(max_j)
  
  dp = [[0]*max_j for _ in range(N)]

  for j in range(1, max_j):
    dp[0][j] = 1001001001
  dp[0][0] = 0
  for i in range(1, N):
    for j in range(max_j):
      if j - v[i-1] >= 0:
        dp[i][j] = min(dp[i-1][j-v[i-1]] + w[i-1], dp[i-1][j])
      else:
        dp[i][j] = dp[i-1][j]
  ans = 0
  # print(dp)
  for j in range(max_j):
    if dp[N-1][j] <= W:
      ans = j
  print(ans)

  
if __name__ == '__main__':
  main()
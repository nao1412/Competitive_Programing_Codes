def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n, k = I()
  h = LI()
  dp = [1001001001]*n
  dp[0] = 0
  dp[1] = abs(h[0] - h[1])
  for j in range(2, n):
    for i in range(1, k+1):
      dp[j] = min(dp[j], dp[j-i] + abs(h[j]- h[j-i]))
  
  print(dp[n-1])
if __name__ == '__main__':
  main()
# 配るDP

def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n = int(input())
  h = LI() + [0] + [0]
  # print(h)
  dp = [1001001001]*(n+2) # 1001001001より大きくしないと一番多き数として初期化することができない
  dp[0] = 0
  for i in range(n):
    dp[i+1] = min(dp[i+1], dp[i] + abs(h[i] - h[i+1]))
    dp[i+2] = min(dp[i+2], dp[i] + abs(h[i] - h[i+2]))
  # print(dp)
  print(dp[n-1])
if __name__ == '__main__':
  main()

# 貰うDP

def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n = int(input())
  h = LI()
  # print(h)
  dp = [1001001001]*n # 1001001001より大きくしないと一番多き数として初期化することができない
  dp[0] = 0
  dp[1] = abs(h[0] - h[1])
  for i in range(2, n):
    dp[i] = min(dp[i-2] + abs(h[i] - h[i-2]), dp[i-1] + abs(h[i] - h[i-1]))

  # print(dp)
  print(dp[n-1])
if __name__ == '__main__':
  main()

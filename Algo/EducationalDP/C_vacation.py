def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n = int(input())
  abc = [0]*n
  for i in range(n):
    abc[i] = LI()
  # print(abc)
  dp = [[0,0,0] for _ in range(n+1)]
  for lst in range(3):
    dp[1][lst] = abc[0][lst]

  for i in range(1,n):
    for lst in range(3):
      for nxt in range(3):
        if lst != nxt:
          dp[i+1][nxt] = max(dp[i+1][nxt], dp[i][lst] + abc[i][nxt])
    # print(dp)

  ans = 0
  for lst in range(3):
    ans = max(ans, dp[n][lst])
  print(ans)

if __name__ == '__main__':
  main()
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
mod = 10**9 + 7

def main():
  N = I()
  h = LI()
  dp = [0]*N
  for i in range(1, N):
    if i == 1:
      dp[i] = dp[i-1] + abs(h[i]-h[i-1])
    else:
      dp[i] = min(dp[i-1] + abs(h[i]-h[i-1]),
                  dp[i-2] + abs(h[i]-h[i-2]))
  print(dp[-1])
if __name__ == '__main__':
  main()
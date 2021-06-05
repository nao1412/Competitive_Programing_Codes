import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
mod = 10**9 + 7

def main():
  N = I()
  a = LI()
  dp = [0]*N
  dp[0] = 0
  dp[1] = abs(a[1] - a[0])
  for i in range(2, N):
    dp[i] = min(dp[i-1] + abs(a[i]-a[i-1]),
                dp[i-2] + abs(a[i]-a[i-2]))
  print(dp[-1])
if __name__ == '__main__':
  main()
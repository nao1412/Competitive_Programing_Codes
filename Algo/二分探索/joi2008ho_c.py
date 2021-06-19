from bisect import bisect
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
mod = 10**9 + 7

def main():
  N, M = MI()
  P = [0]*(N+1)
  for _ in range(N):
    P[_+1] = I()
  zeroone = []
  for i in range(N+1):
    for j in range(i, N+1):
      zeroone.append(P[i] + P[j])
  zeroone.sort()
  ans = 0
  for p in zeroone:
    if M - p > 0:
      x = bisect(zeroone, M-p) - 1
      ans = max(ans, p + zeroone[x])
  print(ans)
  
if __name__ == '__main__':
  main()
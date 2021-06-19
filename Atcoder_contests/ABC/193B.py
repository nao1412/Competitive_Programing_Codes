import sys
import math
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
INF = 100100100100

def main():
  n = I()
  ans = INF
  for i in range(n):
    a, p, k = MI()
    if a < k:
      ans = min(ans, p)
  if ans == INF: print(-1)
  else: print(ans)
if __name__ == '__main__':
  main()
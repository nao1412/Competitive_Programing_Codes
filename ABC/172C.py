import sys
import math
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
from bisect import bisect_right
def main():
  n, m, k = MI()
  a = LI()
  b = LI()
  bsum = [b[0]]
  for i in range(m-1):
    bsum.append(bsum[i] + b[i+1])
  # print(bsum)
  tot = 0
  aco = 0
  ans = 0
  while tot <= k:
    find = k - tot
    bco = bisect_right(bsum, find)
    # print(aco, bco, find)
    ans = max(ans, aco + bco)
    if aco == n: break
    tot += a[aco]
    aco += 1
  print(ans)
if __name__ == '__main__':
  main()
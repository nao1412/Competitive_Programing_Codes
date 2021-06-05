import sys
import numpy as np
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
INF = 1001001001
from statistics import median_low
def main():
  n, k = MI()
  a = []
  for _ in range(n):
    a.append(LI())
  A = np.array(a)
  # print(A)
  ans = INF
  for i in range(n-k+1):
    for j in range(n-k+1):
      x = A[i:i+k, j:j+k]
      x = np.ravel(x)
      # print(x)
      ans = min(ans, median_low(x))
      # print(ans)
  print(ans)
if __name__ == '__main__':
  main()
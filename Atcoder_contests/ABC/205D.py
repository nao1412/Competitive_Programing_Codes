import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
import math
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
def H(n): return [input() for i in range(n)]
mod = 10**9 + 7
from bisect import bisect_left
def main():
  n, q = MI()
  a = LI()
  bfr = 0
  b = []
  for i in range(n):
    b.append(a[i] - bfr - 1)
    bfr = a[i]
  # print(b)
  rb = [0]
  for i in range(n):
    rb.append(rb[i] + b[i])
  # print(rb)
  a = [0] + a
  # print(a)
  for _ in range(q):
    k = I()
    x = bisect_left(rb, k)
    # print(x, 'x')
    if x >= n+1: x = n
    # print(a[x], 'a[x]')
    # print(rb[x], 'rb[x]')
    if k - rb[x] > 0: print(a[x] + k - rb[x])
    else: print(a[x-1] + k - rb[x-1])
if __name__ == '__main__':
  main()

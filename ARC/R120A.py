import sys
import math
from typing import Mapping
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n = I()
  a = LI()
  MAX_a = -1
  s = 0
  ans = 0
  for i in range(n):
    s += a[i]
    MAX_a = max(MAX_a, a[i])
    ans += s
    print(ans + MAX_a*(i+1))
if __name__ == '__main__':
  main()
import sys
import math
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
from collections import Counter
def main():
  n, k = MI()
  a = LI()
  a = Counter(a)
  nn = len(a)
  b = []
  for i in a.values():
    b.append(i)
  b = sorted(b)
  # print(b)
  print(sum(b[:nn-k]))
if __name__ == '__main__':
  main()
from _typeshed import StrPath
import sys
import math
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n = I()
  x = []
  y = []
  for _ in range(n):
    xx, yy = MI()
    x.append(xx)
    y.append(yy)
  x = sorted(x, reverse=True)
  y = sorted(y, reverse=True)
  ans = 


if __name__ == '__main__':
  main()
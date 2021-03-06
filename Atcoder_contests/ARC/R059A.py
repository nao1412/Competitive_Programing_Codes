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

def main():
  n = I()
  a = LI()
  INF = 1001001001
  cnt = INF
  
  for i in range(min(a), max(a)+1):
    res = 0
    for j in range(n):
      res += (i - a[j]) ** 2
    if cnt > res:
      cnt = res
  print(cnt)
if __name__ == '__main__':
  main()


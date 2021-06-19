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
  a = LI()
  s = sum(a)
  for i in range(1<<4):
    res = 0
    for j in range(4):
      if (i>>j) & 1:
        res += a[j]
    if s - res == res:
      print('Yes')
      exit()
  print('No')
if __name__ == '__main__':
  main()
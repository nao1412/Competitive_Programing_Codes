import sys
import math
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n = I()
  a = n // 1000
  i = 1
  ans = 0
  while a != 0:
    ans += n - (1000**i) + 1
    i += 1
    a = n // (1000**i)
  print(ans)
if __name__ == '__main__':
  main()
import sys
from typing import AnyStr
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n = I()
  a = LI()
  ans = 0
  ttl = sum(a) % mod
  for i in range(n-1):
    ttl -= a[i]
    if ttl < 0: ttl += mod
    ans += a[i] * ttl
    ans %= mod
  print(ans)
      
if __name__ == '__main__':
  main()
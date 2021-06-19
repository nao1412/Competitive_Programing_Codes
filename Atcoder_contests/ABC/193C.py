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
  s = set()
  for a in range(2, int(n**0.5)+1):
    x = a*a
    while x <= n:
      s.add(x)
      x *= a
  print(n - len(s))
if __name__ == '__main__':
  main()
import sys
import math
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
def g1(n):
  return int(''.join(sorted(str(n))[::-1]))
def g2(n):
  return int(''.join(sorted(str(n))))
def f(n):
  return g1(n) - g2(n)

def main():
  n, k = MI()
  for i in range(k):
    n = f(n)
  print(n)
    
if __name__ == '__main__':
  main()
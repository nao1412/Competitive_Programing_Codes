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
  n, k = MI()
  if k % 2 == 0:
    n1 = n // k
    n2 = n1
    if n % k >= k // 2: 
      n2 = n1 + 1
  else:
    n1 = n // k
    n2 = 0
  print(n1**3+n2**3)
if __name__ == '__main__':
  main()

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
  n, m = MI()
  ans = 1
  a = 1
  while a * a <= m:
    if m % a == 0:
      b = m // a
      if a * n <= m: ans = max(ans, a)
      if b * n <= m: ans = max(ans, b)
    a += 1
  print(ans)

  ''' 別解 '''
  '''
  x = m // n
  while 1:
    if m % x == 0:
      print(x)
      exit()
    else: x -= 1
  '''
if __name__ == '__main__':
  main()

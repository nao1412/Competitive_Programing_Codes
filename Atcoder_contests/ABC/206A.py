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
  a = math.floor(1.08 * n)
  if a < 206: print('Yay!')
  elif a == 206: print('so-so')
  else: print(':(')
if __name__ == '__main__':
  main()

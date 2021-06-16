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

def jg(a, b):
  if a > b: print('>')
  elif a == b: print('=')
  else: print('<')
  return 0

def main():
  a, b, c = MI()
  if a >= 0 and b >= 0:
    jg(a, b)
  else:
    if not c%2: jg(abs(a), abs(b))
    else: jg(a, b)
if __name__ == '__main__':
  main()


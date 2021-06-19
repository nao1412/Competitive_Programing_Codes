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
  a, b, c = MI()
  if a == b:
    print(c)
  elif b == c:
    print(a)
  elif c == a:
    print(b)
  else: print(0)
if __name__ == '__main__':
  main()
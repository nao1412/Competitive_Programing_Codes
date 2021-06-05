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
  a, b, x, y = MI()
  a = a*2-1
  b *= 2
  ans = 0
  t = abs(a-b)
  if 2*x > y:
    ans += y * (t // 2)
    t -= t//2 * 2
  ans += t * x
  print(ans)
if __name__ == '__main__':
  main()
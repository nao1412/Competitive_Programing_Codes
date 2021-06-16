import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
from math import acos, cos, sin
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
def H(n): return [input() for i in range(n)]
mod = 10**9 + 7
import cmath
def main():
  n = I()
  x1, y1 = MI()
  x2, y2 = MI()
  A = x1 + y1*1j
  O = (x1+x2)/2 + (y1+y2)/2*1j
  PI = acos(-1)
  rad = 2*PI/n
  r = cos(rad) + sin(rad) * 1j
  # print(O, PI)
  # print(O + (A-O) * r)
  ans = O + (A-O) * r
  print(ans.real, ans.imag)

  # 書き方変える complexを使うと遅い 5倍くらい
  # n = I()
  # x1, y1 = MI()
  # x2, y2 = MI()
  # a = complex(x1, y1)
  # b = complex(x2, y2)
  # o = (a+b) / 2
  # PI = acos(-1)
  # rad = 2*PI/n
  # r = complex(cos(rad), sin(rad))
  # ans = o + (a-o)*r
  # print(ans.real, ans.imag)
  # # print(a, b)
if __name__ == '__main__':
  main()
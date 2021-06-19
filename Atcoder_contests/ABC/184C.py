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
  a, b = MI()
  c, d = MI()
  x = a - c
  y = b - d
  if x == 0 and y == 0: ans = 0
  elif x+y == 0 or x-y == 0 or abs(x) + abs(y) <= 3: ans = 1
  else:
    if (x+y)%2 == 0 or abs(x) + abs(y) <= 6 or abs(x+y) <= 3 or abs(x-y) <= 3:
      ans = 2
    else:
      ans = 3
  print(ans)
if __name__ == '__main__':
  main()
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
  t = I()
  for _ in range(t):
    c = I()
    if c % 2:
      ans = 'Odd'
    else:
      if c % 4:
        ans = 'Same'
      else:
        ans = 'Even'
    print(ans)
if __name__ == '__main__':
  main()
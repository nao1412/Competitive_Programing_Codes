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
    l, r = MI()
    if l == r:
      if l == 0: 
        print(1)
        continue
      else: 
        print(0)
        continue
    if r < 2*l: 
      print(0)
      continue
    a = r - 2*l + 1
    print(a*(a+1)//2)
if __name__ == '__main__':
  main()
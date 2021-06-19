import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
import math
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n = I()
  a = LI()
  ans = 0
  for i in range(n):
    if a[i] <= 10: continue
    else: ans += a[i] - 10
  print(ans)
if __name__ == '__main__':
  main()

# A = [input() for i in range(H)]
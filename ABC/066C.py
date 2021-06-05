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
  n = I()
  a = LI()
  re = 1
  ans = []
  for i in range(n):
    if re == 1: ans = ans + [a[i]]
    else: ans = [a[i]] + ans
    re *= -1
  # print(ans) 
  if re == -1:
    ans = reversed(ans)
  print(*ans)
if __name__ == '__main__':
  main()
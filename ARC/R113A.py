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
  k = I()
  ans = 0
  for i in range(k):
    b = k // (i+1)
    for j in range(b):
      ans += b // (j+1)
  print(ans)

if __name__ == '__main__':
  main()
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
  n, x = MI()
  x *= 100
  cnt = 0
  for i in range(n):
    v,p = MI()
    cnt += v * p
    if cnt > x:
      print(i+1)
      exit()
  print(-1)
if __name__ == '__main__':
  main()
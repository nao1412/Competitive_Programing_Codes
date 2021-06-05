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
  k = I()
  s = 7
  for i in range(k):
    if s % k == 0:
      print(i+1)
      exit()
    s = (s * 10 + 7) % k
  print(-1)
if __name__ == '__main__':
  main()
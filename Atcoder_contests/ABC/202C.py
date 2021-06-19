import sys
import math
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
import collections
def main():
  n = I()
  a = LI()
  b = LI()
  c = LI()
  al = collections.Counter(a)
  ans = 0
  for i in c:
    ans += al[b[i-1]]
  print(ans)
if __name__ == '__main__':
  main()
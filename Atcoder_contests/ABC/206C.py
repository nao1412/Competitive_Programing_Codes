import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
import math
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
def H(n): return [input() for i in range(n)]
mod = 10**9 + 7
from collections import Counter
def main():
  n = I()
  a = LI()

  cnt = Counter(a)
  ans = 0
  for i in cnt:
    ans += (n - cnt[i]) * cnt[i]
    # print(i)
  print(ans//2)
  # print(cnt)
  
if __name__ == '__main__':
  main()

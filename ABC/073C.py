import sys
import math
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
from collections import Counter
def main():
  n = I()
  memo = []
  for _ in range(n):
    memo.append(I())
  memo = Counter(memo)
  ans = 0
  for i in memo.values():
    if i % 2:
      ans += 1
  print(ans)
if __name__ == '__main__':
  main()
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
  n, k = MI()
  now = 0
  ab = []
  for _ in range(n):
    a = LI()
    ab.append(a)
  ab = sorted(ab, key=lambda x: x[0])
  # print(ab)
  for i in range(n):
    if k < ab[i][0] - now: break
    k -= ab[i][0] - now
    now = ab[i][0]
    k += ab[i][1]
  print(now + k)
if __name__ == '__main__':
  main()
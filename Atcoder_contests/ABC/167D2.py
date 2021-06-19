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
  d = 60
  MAX_n = 200005
  to = [[0]*MAX_n for _ in range(d)]
  n, k = MI()
  a = LI()
  for i in range(n):
    to[0][i] = a[i] - 1
  for i in range(d-1):
    for j in range(n):
      to[i+1][j] = to[i][to[i][j]] # to[i][j] = j kara 2**i ko saki
  v = 0
  for i in reversed(range(d)):
    l = 1<<i
    if l <= k:
      v = to[i][v]
      k -= l
  print(v+1)
if __name__ == '__main__':
  main()
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
  n, k= MI()
  a = []
  for _ in range(n):
    a.append(LI())
  
  ng = -1
  ok = 1001001001
  L = k*k//2+1
  s = [[0]*(n+1) for _ in range(n+1)]
  while abs(ok-ng) > 1:
    wj = (ok+ng)//2
    for i in range(n):
      for j in range(n):
        if a[i][j] > wj: s[i+1][j+1] = 1
        else: s[i+1][j+1] = 0
    
    for i in range(n+1):
      for j in range(n):
        s[i][j+1] += s[i][j]
    for i in range(n):
      for j in range(n+1):
        s[i+1][j] += s[i][j]

    flag = False
    for i in range(n-k+1):
      for j in range(n-k+1):
        now = s[i+k][j+k]
        now -= s[i][j+k]
        now -= s[i+k][j]
        now += s[i][j]
        if L > now: flag = True
    if flag: ok = wj
    else: ng = wj
  
  print(ok)
if __name__ == '__main__':
  main()
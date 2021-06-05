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
  n, q = MI()
  par = [-1]*n
  def find(x):
    if par[x] < 0: return x
    else:
      par[x] = find(par[x])
      return par[x]
  def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y: return False
    if par[x] > par[y]: x, y = y, x
    par[x] += par[y]
    par[y] = x
    return True
  def same(x, y): return find(x) == find(y)
  for _ in range(q):
    p, a, b = MI()
    if p:
      if same(a, b): print('Yes')
      else: print('No')
    else:
      unite(a,b)

if __name__ == '__main__':
  main()
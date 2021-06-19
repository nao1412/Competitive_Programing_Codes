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
  d = [-1]*n
  def find(x):
    if d[x] < 0: return x
    else: return find(d[x])
  def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y: return False
    if d[x] > d[y]: x, y = y, x
    d[x] += d[y]
    d[y] = x
    return True
  def same(x, y): return find(x) == find(y)
  def size(x): return -d[find(x)]
  for _ in range(q):
    com, x, y = MI()
    if com:
      if same(x, y): print(1)
      else: print(0)
    else: unite(x, y)
    # print(d)
if __name__ == '__main__':
  main()
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

def main():
  n = I()
  a = LI()

  a1 = a[:n//2]
  a2 = a[n//2:]
  if n % 2 == 1: a2 = a2[1:]
  a2 = a2[::-1]
  
  par = [-1]*1001001
  # xの根を見つける
  def find(x):
    if par[x] < 0: return x
    else:
      par[x] = find(par[x])
      return par[x] # 経路縮約
  # x, yの集合をunite
  def unite(x, y):
    rx = find(x) # rootにする
    ry = find(y)
    if rx == ry: return False # mstクラスカル法　くっつけるのに成功したのか
    if par[rx] > par[ry]: rx, ry = ry, rx # sizeの大きいほうをxにする。なお、データは負
    par[rx] += par[ry] # yをxにくっつける sizeも管理
    par[ry] = rx # 
    return True
  # xとyが同じ集合かどうか
  def same(x, y): return find(x) == find(y)
  # xの連結成分のサイズ
  def size(x): return -par[find(x)]

  for i in range(len(a1)):
    unite(a1[i], a2[i])
  
  # print(par)
  ans = 0
  for i in par:
    if i < -1:
      ans += -i - 1
  print(ans)
    
if __name__ == '__main__':
  main()

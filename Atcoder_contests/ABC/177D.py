import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n, m = MI()
  
  # union find
  def find(x):
    if par[x] < 0: return x
    else: 
      par[x] = find(par[x])
      return par[x] # 経路縮約
  def unite(x, y):
    rx = find(x) # rootにする
    ry = find(y)
    if rx == ry: return False
    if par[rx] > par[ry]: rx, ry = ry, rx
    par[rx] += par[ry]
    par[ry] = rx
    return True
  def size(x): return -par[find(x)] # 連結成分サイズ
  par = [-1]*n
  for _ in range(m):
    a, b = MI()
    unite(a-1, b-1)

  ans = 0
  for i in range(n):
    ans = max(ans, size(i))
  print(ans)
if __name__ == '__main__':
  main()
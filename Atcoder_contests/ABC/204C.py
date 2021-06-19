import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
import math
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n, m = MI()
  path = [[] for _ in range(n)]
  for _ in range(m):
    a, b = MI()
    path[a-1].append(b-1)

  # def dfs(v):
  #   if temp[v]: return
  #   temp[v] = True
  #   for vv in path[v]: dfs(vv)
  # ans = 0
  # for i in range(n):
  #   temp = [False]*n
  #   dfs(i)
  #   ans += sum(temp)

  def dfs(v):
    if tmp[v]: return # すでに探索済みならもう探索をしない
    tmp[v] = True # ここに行ける
    for vv in path[v]: dfs(vv) # 矢印のほうに行ける
    # いつ終わるの？
    # 探索済みの場合、それ以上道がない場合。行った先が探索済みの時は行き止まりと同じ

  ans = 0
  for i in range(n):
    tmp = [False]*n
    dfs(i)
    ans += sum(tmp)
  
  print(ans)

if __name__ == '__main__':
  main()

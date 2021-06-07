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
  for i in range(m):
    a, b = MI()
    path[a-1].append(b-1)

  def dfs(v):
    if temp[v]: return
    temp[v] = True
    for vv in path[v]: dfs(vv)
  ans = 0
  for i in range(n):
    temp = [False]*n
    dfs(i)
    ans += sum(temp)
  print(ans)

if __name__ == '__main__':
  main()

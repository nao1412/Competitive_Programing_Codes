import sys
sys.setrecursionlimit(500000)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n, q = MI()
  g = [[] for _ in range(n)]
  ans = [0]*n
  visited = [0]*n

  for _  in range(n-1):
    a, b = MI()
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
  
  for _  in range(q):
    p, x = MI()
    p -= 1
    ans[p] += x
  visited[0] = 1
  def dfs(v, p = -1):
    for u in g[v]:
      if visited[u]: continue
      visited[u] = 1
      ans[u] += ans[v]
      dfs(u, v)
  dfs(0)
  print(*ans)

if __name__ == '__main__':
  main()
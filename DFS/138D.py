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
  g = [[] for _  in range(n)]
  cnt = [0]*n
  visited = [0]*n

  for i in range(n-1):
    a, b = MI()
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
  
  for i in range(q):
    p, x = MI()
    p -= 1
    cnt[p] += x # 根にxを足す
  
  visited[0] = 1
  st = [0]

  while st: # stに頂点がある間
    v = st.pop() # 行く場所
    for u in g[v]: # vを根とする頂点に対して
      if visited[u]: # 逆戻りしないようにもう加算されていたら飛ばす
        continue
      visited[u] = 1 # 足跡をつける
      cnt[u] += cnt[v] # 加算
      st.append(u) # stに次に行く場所を追加
  
  print(*cnt)

if __name__ == '__main__':
  main()
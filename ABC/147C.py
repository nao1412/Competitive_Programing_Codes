n = int(input())
# graph = [[-1]*n]*n この初期化の仕方はよくない。すべてが同じ要素だと判断されて一個要素を変えるとすべてに反映される
graph = [[-1]*n for _ in range(n)]
for i in range(n):
  a = int(input())
  for _ in range(a):
    x, y = map(int, input().split())
    graph[i][x-1] = y
    
ans = 0
# n人が正直or不親切の場合を全探索
for i in range(2**n):
  honesty = [0]*n
  for j in range(n):
    if ((i >> j) & 1):
      honesty[j] = 1 # 0~n-1までの2進数表記

  ok = True # 矛盾しないかのフラッグok
  for j in range(n): # 一人ずつ証言と矛盾しないか確かめる
    if honesty[j]: # 正直の時は証言は確実でなければならない
      for k in range(n): # その人の他の人(自分も含める-1だから関係ないけど)への証言
        if graph[j][k] == -1: continue
        if graph[j][k] != honesty[k]: ok = False # 証言の有向グラフと仮定のhonestyが違ったらこれは矛盾している
  if ok: # 矛盾せずにここまでこれたbitの中でフラグが一番多いのが勝ち
    ans = max(ans, honesty.count(1))

print(ans)

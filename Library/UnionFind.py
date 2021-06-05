n = 0
par = [-1]*n # parent
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

class UnionFind(): # uf(n)
  def __init__(self, n):
      self.self.par = [-1]*n
  def find(self, x):
    if self.par[x] == x: return x
    else: return self.find(self.par[x]) # 経路縮約

  def unite(self, x, y):
    rx = self.find(x) # rootにする
    ry = self.find(y)
    if rx == ry: return False
    if self.par[rx] > self.par[ry]: self.par[rx] = self.par[ry]
    self.par[rx] += self.par[ry]
    self.par[rx] = ry
    return True

  def same(self, x, y): return self.find(x) == self.find(y)

  def size(self, x): return -self.par[self.find(x)] # 連結成分サイズ



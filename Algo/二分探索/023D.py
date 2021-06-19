def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n = int(input())
  hs = [tuple(I()) for _ in range(n)]
  high = 10**16
  low = 0
  
  def check(X):
    time = [0]*n
    for i, x in enumerate(hs): # インデックス番号と要素を取得　今回はタプル
      h, s = x # タプルをh, sに代入しなおす
      if X < h: # もしmidよりもhが大きいならmidは適さない
        return False # すべてのhに対して満たさなければならない
      time[i] = (X-h) // s # すべて満たしているときXに到達するまでの時間は?
    time.sort()
    for i in range(n):
      if time[i] < i: # iより小さいとXは適さないものといえる
        return False
    return True # すべてにおいてtime[i]がiより大きくないといけない
  
  while high - low > 1:
    mid = (high + low) // 2
    if check(mid):
      high = mid
    else:
      low = mid

  print(high)
  
if __name__ == '__main__':
  main()
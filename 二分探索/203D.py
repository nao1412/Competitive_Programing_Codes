import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n, k = MI()
  a = []
  for _ in range(n):
    a.append(LI())
  
  L = k*k//2+1
  wa = -1
  ac = 1001001001
  while wa + 1 < ac: # 二分探索で中央値を決め打ち
    wj = (wa+ac)//2
    ok = False

    s = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n): # 累積和のテーブルを作る
      for j in range(n):
        if a[i][j] > wj: s[i+1][j+1] = 1 # wjより大なら1
        else: s[i+1][j+1] = 0
        # s[i+1][j+1] = a[i][j]
    for i in range(n+1):
      for j in range(n):
        s[i][j+1] += s[i][j]
    for i in range(n):
      for j in range(n+1):
        s[i+1][j] += s[i][j]

    for i in range(n-k+1): # 二次元累積和
      for j in range(n-k+1):
        now = s[i+k][j+k]
        now -= s[i][j+k]
        now -= s[i+k][j]
        now += s[i][j]
        if now < L: ok = True # その区画に中央値が存在する！
    if ok: ac = wj
    else: wa = wj
  print(ac)
if __name__ == '__main__':
  main()
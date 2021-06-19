import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
import math
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
def H(n): return [input() for i in range(n)]
mod = 10**9 + 7

# 高速素因数分解

def prime_factorize(n):
  a = []
  while n % 2 == 0: # 2は偶数なので先に処理
    a.append(2)
    n //= 2
  f = 3
  while f**2 <= n: # 素因数は√n以下であるからf**2がn以下の場合を考える
    if n % f == 0: # その素数で割り切れるだけ割る
      a.append(f)
      n //= f
    else:          # 割り切れなくなったら次の奇数。合成数で割られることはない。
      f += 2       # 理由は合成数の素因数でfより小さいものはすでに割られているから
  if n != 1:
    a.append(n)
  return list(set(a))        # 素因数分解のリストを返す

def add(a):
  l = len(a)
  for i in range(1<<l):
    tmp = 1
    for j in range(l):
      if (i >> j) & 1:
        tmp *= a[j]
    a.append(tmp)
  return list(set(a))

def main():
  l, r = MI()
  x = l
  ans = 0
  
  while x < r:
    res = 0
    pf = prime_factorize(x)
    ls = add(pf)
    # print(pf, ls)
    ls = ls[1:]
    # print(ls)
    for i in range(len(ls)):
      res += r // pf[i] - (x-1) // pf[i]
    
    res -= r//x
    ans += res
    x += 1
  print(ans)
if __name__ == '__main__':
  main()

import sys
import math
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
import collections
# def main():
#   n = I()
#   if n == 1:
#     print(0)
#     exit()
#   # 高速素因数分解
#   def prime_factorize(n):
#     a = []
#     while n % 2 == 0: # 2は偶数なので先に処理
#       a.append(2)
#       n //= 2
#     f = 3
#     while f**2 <= n: # 素因数は√n以下であるからf**2がn以下の場合を考える
#       if n % f == 0: # その素数で割り切れるだけ割る
#         a.append(f)
#         n //= f
#       else:          # 割り切れなくなったら次の奇数。合成数で割られることはない。
#         f += 2       # 理由は合成数の素因数でfより小さいものはすでに割られているから
#     if n != 1:
#       a.append(n)
#     return collections.Counter(a)         # 素因数分解のリストを返す
#   pf = prime_factorize(n)
#   # print(pf)
#   # print(len(pf))
#   cnt = 1
#   ans = 0
#   MAX_pf = max(pf.values())
#   while MAX_pf > 0:
#     for i in pf.keys():
#       pf[i] -= cnt
#       if pf[i] >= 0: ans += 1
#     # print(pf, MAX_pf)
#     MAX_pf -= cnt
#     cnt += 1
#   print(ans)
def main():
  n = I()
  
  
if __name__ == '__main__':
  main()
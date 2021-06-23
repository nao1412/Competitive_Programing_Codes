
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
  return a         # 素因数分解のリストを返す



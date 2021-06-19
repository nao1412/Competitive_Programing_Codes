import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
from math import factorial
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
def H(n): return [input() for i in range(n)]
mod = 10**9 + 7

def modinv(a, mod):
  b = mod; u = 1; v = 0
  while b:
    t = a // b
    a -= t * b; a, b = b, a
    u -= t * v; u, v = v, u
  u %= mod
  if u < 0: u += mod
  return u

def main():
  n, m, k = MI()
  x = n+m
  tmp = 1
  for i in range(min(n, m)):
    tmp = (tmp * x) % mod
    x -= 1
  print(tmp, factorial(min(n,m )))
  ttl = tmp * modinv(factorial(min(n, m)), mod)
  print(ttl)
  # def f(w, b):
  #   if w - b > k: return res
  #   res += 
  #   return f(w+1, b), f(w, b+1)

if __name__ == '__main__':
  main()

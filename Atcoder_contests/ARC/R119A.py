import sys
import math
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
INF = 100100100100100
def main():
  n = I()
  b = int(math.log2(n))
  ans = INF
  if n == 1: ans = 1
  for i in range(b):
    a = n // 2**i
    c = n % 2**i
    ans = min(ans, a+i+c)
    # print(a, i ,c, ans
  print(ans)

if __name__ == '__main__':
  main()
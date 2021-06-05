import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
import math
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n, q = MI()
  g = [[] for _ in range(n)]
  for _ in range(n-1):
    a, b = MI()
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)
  
  c = [0]*n
  for i in range(q):
    p, x = MI()
    

if __name__ == '__main__':
  main()

# A = [input() for i in range(H)]
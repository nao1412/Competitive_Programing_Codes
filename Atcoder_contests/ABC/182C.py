import sys
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
INF = 1001001001

def main():
  s = S()
  amari = [0,0,0]
  k = len(s)
  for i in range(k):
    amari[(int(s[i]) - 0) % 3] += 1
  x = int(s) % 3
  ans = INF
  for i1 in range(3):
    for i2 in range(3):
      if amari[1] < i1: continue
      if amari[2] < i2: continue
      if i1 + i2 == k: continue
      nx = x
      nx -= i1*1
      nx -= i2*2
      if nx % 3 == 0: ans = min(ans, i1+i2)
  if ans == INF: ans = -1
  print(ans)

if __name__ == '__main__':
  main()
import sys
import math
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  a,b,k = MI()
  c = [[0]*61 for _ in range(61)]
  c[0][0] = 1
  for i in range(60):
    for j in range(60):
        c[i+1][j] += c[i][j]
        c[i+1][j+1] += c[i][j]
  ans = ''
  while a+b > 0:
    x = 0
    if a >= 1: x = c[a+b-1][a-1]
    if x <= k:
      ans += 'a'
      a -= 1
    else:
      ans += 'b'
      b -= 1
      k -= x
  print(ans)
if __name__ == '__main__':
  main()
import sys
import math
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n = I()
  s = S()
  brg = [0,0,0]
  for i in range(n):
    brg[ord(s[i]) % 3] += 1
  ans = 1
  for i in range(3): ans *= brg[i]
  for j in range(n):
    for i in range(j):
      k = j + (j-i)
      if k < n:
        if s[i] == s[j]: continue
        if s[j] == s[k]: continue
        if s[k] == s[i]: continue
        ans -= 1
  print(ans)

if __name__ == '__main__':
  main()
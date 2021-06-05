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
  h, w = MI()
  s = []
  for _ in range(h):
    s.append(S())
  ans = 0
  for i in range(h-1):
    for j in range(w-1):
      cnt = 0
      for di in range(2):
        for dj in range(2):
          if s[i+di][j+dj] == '#': cnt += 1
      if cnt == 1 or cnt == 3: ans += 1
  print(ans)

if __name__ == '__main__':
  main()
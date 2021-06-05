import sys
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
from collections import defaultdict

l = defaultdict(lambda:0)
def main():
  n = I()
  for i in range(n):
    l[S()] += 1

  ll = sorted(l.items(), key=lambda x:x[0])
  ans = sorted(ll, key=lambda x:x[1], reverse=True)
  m = ans[0][1]
  for i in range(len(ans)):
    if ans[i][1] == m:
      print(ans[i][0])

if __name__ == '__main__':
  main()
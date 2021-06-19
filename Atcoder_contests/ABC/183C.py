import sys
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
import itertools
def main():
  n, k = MI()
  l = []
  for i in range(1, n):
    l.append(i)
  ll = itertools.permutations(l)
  t = []
  for _ in range(n):
    t.append(LI())

  ans = 0
  for L in ll:
    cnt = 0
    L = list(L)
    L.insert(0, 0)
    # print(L)
    now = 0
    for i in range(n):
      nx = L.pop()
      cnt += t[nx][now]
      now = nx
    if cnt == k:
      ans += 1
  print(ans)  
if __name__ == '__main__':
  main()
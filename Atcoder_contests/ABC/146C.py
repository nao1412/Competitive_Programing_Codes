import sys
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
# 今回はN <= 10**9なのでbisectは使えない

def main():
  a, b, x = MI()
  def isok(arg):
    return a * arg + b * len(str(arg)) <= x
  def bs(ng, ok):
    while (abs(ok-ng)) > 1:
      mid = (ok + ng) // 2
      if isok(mid):
        ok = mid
      else:
        ng = mid
    return ok
  print(bs(10**9 + 1, 0)) #両方範囲外を選択
if __name__ == '__main__':
  main()
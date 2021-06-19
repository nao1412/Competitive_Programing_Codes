import sys
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n = I()
  a = LI()

  ans = 0
  for l in range(n):
    x = a[l]
    for r in range(l, n):
      x = min(x, a[r])
      ans = max(ans, x*(r-l+1))
  return print(ans)
if __name__ == '__main__':
  main()
import sys
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7
def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b, a%b)
def ggcd(a, b, c):
  return gcd(gcd(a,b),c)
def main():
  k = I()
  ans = 0
  for i in range(1,k+1):
    for j in range(i, k+1):
      for h in range(j, k+1):
        if i == j == h:
          cnt = 1
        elif i == j or j == h or h == i:
          cnt = 3
        else:
          cnt = 6
        ans += ggcd(i, j, h) * cnt
  print(ans)
if __name__ == '__main__':
  main()
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

def main():
  n, X = MI()
  x = LI()
  x.append(X)
  x.sort()
  for i in range(n):
    if i == 0:
      ans = x[i+1] - x[i]
    else:
      ans = gcd(ans, x[i+1] - x[i])
      
  print(ans)

if __name__ == '__main__':
  main()
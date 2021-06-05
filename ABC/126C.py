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
  n, k = MI()
  ans = 0
  for i in range(1, n+1):
    if i >= k: 
      ans += n - i + 1
      break
    ans += 0.5 ** math.ceil(math.log2(k/i))
  print(ans / n)
if __name__ == '__main__':
  main()
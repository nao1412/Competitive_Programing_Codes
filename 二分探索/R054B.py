import bisect
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
mod = 10**9 + 7

def main():
  P = float(input())
  def cost(x):
    return x + P * pow(2, -(x/1.5))
  left = 0
  right = int(1e+18)
  for i in range(10**5):
    m1 = (left * 2 + right) / 3
    m2 = (left + right * 2) / 3
    if cost(m1) < cost(m2):
      right = m2
    else: left = m1
  print(cost(left))
if __name__ == '__main__':
  main()
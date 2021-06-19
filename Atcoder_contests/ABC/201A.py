import sys
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  a = LI()
  a.sort()
  if a[2] - a[1] == a[1] - a[0]: print('Yes')
  else: print('No')
if __name__ == '__main__':
  main()
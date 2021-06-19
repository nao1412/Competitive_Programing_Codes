import sys
import math
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  s, p = MI()
  for x in range(int(p**0.5)+1):
    if x*(s-x) == p:
      print('Yes')
      exit()
  print('No')
      
if __name__ == '__main__':
  main()
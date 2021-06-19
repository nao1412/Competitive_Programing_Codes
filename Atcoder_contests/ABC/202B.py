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
  s = list(S())
  for i in range(len(s)):
    if s[i] == '9':
      s[i] = '6'
    elif s[i] == '6':
      s[i] = '9'
  s = reversed(s)
  print(''.join(s))
if __name__ == '__main__':
  main()
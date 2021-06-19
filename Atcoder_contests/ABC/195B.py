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
  a, b, w = MI()
  w *= 1000
  ans = []
  flag = 0
  if a <= w/math.ceil(w/b) <= b: ans.append(math.ceil(w/b))
  else: flag = 1
  if a <= w/math.floor(w/a) <= b: ans.append(math.floor(w/a))
  else: flag = 1
  # print(ans)
  if flag: print('UNSATISFIABLE')
  else: print(*ans)

if __name__ == '__main__':
  main()
import sys
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n, x = MI()
  s = S()
  for i in range(n):
    if s[i] == 'o': x += 1
    else: x = max(0, x - 1) # elif x: でもいい
  print(x)
if __name__ == '__main__':
  main()
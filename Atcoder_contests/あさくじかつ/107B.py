import sys
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  h, w = MI()
  a = []
  retu = [0] * h
  gyou = [0] * w
  for i in range(h):
    a.append(S())
  for i in range(h):
    for j in range(w):
      if a[i][j] == '#':
        retu[i] = 1
        gyou[j] = 1
  for i in range(h):
    if retu[i]:
      for j in range(w):
        if gyou[j]:
          print(a[i][j], end = '')
    print()
if __name__ == '__main__':
  main()
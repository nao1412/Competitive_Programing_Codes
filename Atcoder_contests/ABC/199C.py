import sys
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n = I()
  s = list(S())
  q = I()
  flag = 1
  for _ in range(q):
    t, a, b  = MI()
    a -= 1
    b -= 1
    if t == 1:
      if flag == 1: s[a], s[b] = s[b], s[a]
      else: s[(a+n)%(n*2)], s[b-n] = s[b-n], s[(a+n)%(n*2)]
    else: flag *= -1
  s = ''.join(s)
  if flag == -1:
    s1 = s[:n]
    s2 = s[n:]
    s = s2 + s1
  print(s)
if __name__ == '__main__':
  main()
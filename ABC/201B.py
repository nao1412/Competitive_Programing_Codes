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
  st = []
  for i in range(n):
    s, t = map(str, input().split())
    st.append([s, int(t)])
  st = sorted(st, key=lambda x:x[1])
  print(st[-2][0])
if __name__ == '__main__':
  main()
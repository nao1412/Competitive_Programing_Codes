import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
mod = 10**9 + 7

def main():
  n = I()
  s = LI()
  q = I()
  T = LI()
  # 普通のやり方
  # ans = 0
  # def bs(t):
  #   ok, ng = -1, n
  #   def is_ok(i):
  #     return s[i] <= t
  #   while abs(ok - ng) > 1:
  #     mid = (ok + ng) // 2
  #     if is_ok(mid):
  #       ok = mid
  #     else:
  #       ng = mid
  #   return s[max(ok, 0)] == t

  # for t in T:
  #   if bs(t):
  #     ans += 1
  # print(ans)
  
  # bisect を使う
  import bisect
  ans = 0
  for t in T:
    ok = bisect.bisect(s, t) - 1
    if s[max(ok, 0)] == t:
      ans += 1
  print(ans)
if __name__ == '__main__':
  main()
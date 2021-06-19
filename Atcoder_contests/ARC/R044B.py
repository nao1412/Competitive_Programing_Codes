def LI(): return list(map(int, input().split()))
def LS(): return map(int, input().split())

def main():
  n = int(input())
  a = LI()
  if a[0] != 0: return 0
  am =max(a)
  s = [0]*(am+1)
  for c in a:
    s[c] += 1
  if s[0] > 1: return 0
  for i in range(am+1):
    if s[i] == 0: return 0    

  ans = 1
  mod = 10**9 + 7
  pre = 1
  for i in range(1,len(s)):
    now = s[i]
    if now > 1:
      ans *= pow(2, (now * (now-1)) // 2, mod)
      ans %= mod
    ans *= pow((2 ** pre - 1) % mod, now, mod)
    ans %= mod
    pre = now
  return ans

if __name__ == '__main__':
  print(main())
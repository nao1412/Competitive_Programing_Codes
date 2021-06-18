import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
import math
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
def H(n): return [input() for i in range(n)]
mod = 10**9 + 7

def main():
  s = S()
  t = S()

  lt = len(t)
  flag = False
  for i in range(len(s) - lt + 1):
    ss = list(s[i:i+lt])
    j = 0
    for sss in ss:
      if sss == '?':
        j += 1 
        continue
      else:
        if sss == t[j]: 
          j += 1
          continue
        else: break
    if j == lt:
      flag = True
      IN = i
  ans = ''
  if flag:
    i = 0
    while i < len(s):
      if i == IN:
        ans += t
        i += lt
      elif s[i] == '?': 
        ans += 'a'
        i += 1
      else: 
        ans += s[i]
        i += 1
    print(ans)
  else:
    print('UNRESTORABLE')
  
if __name__ == '__main__':
  main()

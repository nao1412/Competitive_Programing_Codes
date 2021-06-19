import sys
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  s = S()
  num = [0]*10
  for i in range(10):
    if s[i] == 'o':
      num[i] = 1
    elif s[i] == 'x':
      num[i] = -1
  ans = 0
  nums = ['0','1','2', '3', '4', '5','6', '7','8','9']
  for i in range(10):
    for j in range(10):
      for k in range(10):
        for l in range(10):
          pas = [nums[i] , nums[j] , nums[k] , nums[l]]
          flag = True
          for n in range(10):
            if num[n] == 1:
              if not str(n) in pas: 
                flag = False
                break
            if num[n] == -1:
              if str(n) in pas:
                flag = False
                break
          if flag: ans += 1
  print(ans)
if __name__ == '__main__':
  main()
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n = int(input())
  a = LI()
  ans = [0]*n
  for i in range(n-1):
    ans[a[i] - 1] += 1
  for aa in ans:
    print(aa)
  
if __name__ == '__main__':
  main()
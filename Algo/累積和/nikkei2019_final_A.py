def l(): return list(map(int, input().split()))
def m(): return map(int, input().split())

def main():
  n = int(input())
  a = l()
  sm = [0]*(n+1)
  for i in range(n):
    sm[i+1] = sm[i] + a[i]
  for i in range(1, n+1):
    ans = 0
    for j in range(n-i+1):
      memo = sm[j+i] - sm[j]
      ans = max(ans, memo)
    print(ans)
    

if __name__ == '__main__':
  main()
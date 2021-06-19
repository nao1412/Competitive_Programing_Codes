def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n = int(input())
  a = LI()
  cnt = 0
  for i in range(1,n):
    if a[i-1] > a[i]:
      cnt += (a[i-1] - a[i])
      a[i] = a[i-1]
  print(cnt)
  
if __name__ == '__main__':
  main()
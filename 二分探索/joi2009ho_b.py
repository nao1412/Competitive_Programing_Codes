def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  d = int(input())
  n = int(input())
  m = int(input())
  shop, addr = [0]*n, [0]*m
  for i in range(n-1):
    shop[i+1] = int(input())
  for i in range(m):
    addr[i] = int(input())

  for i in range(m):
    left = 0
    right = d - 1
    mt = 0
    while left < right:
      if addr[i] == mid:
        mt += 

if __name__ == '__main__':
  main()
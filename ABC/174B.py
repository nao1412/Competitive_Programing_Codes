def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n, d= I()
  cnt = 0
  for i in range(n):
    x, y = I()
    if (x**2 + y**2)**0.5 <= d:
      cnt += 1
  print(cnt)
   
if __name__ == '__main__':
  main()
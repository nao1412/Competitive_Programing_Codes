def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n, x, t = I()
  if n % x == 0:
    print((n//x)*t)
  else:
    print(((n//x) + 1)*t)
if __name__ == '__main__':
  main()
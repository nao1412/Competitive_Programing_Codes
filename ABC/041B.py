def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  a,b,c = LI()
  print(a*b*c % mod)
  # a*b % mod *c % mod
if __name__ == '__main__':
  main()
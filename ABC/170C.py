def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  x, n = I()
  p = LI()
  for i in range(51):
    if x - i not in p:
      ans = x - i
      break
    if x + i not in p:
      ans = x + i
      break
  print(ans)
if __name__ == '__main__':
  main()

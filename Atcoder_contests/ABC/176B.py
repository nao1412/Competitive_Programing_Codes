def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def main():
  n = input()
  x = len(n)
  ans = 0
  for i in range(x):
    ans += int(n[i])
  if ans%9 == 0:
    print('Yes')
  else:
    print('No')
if __name__ == '__main__':
  main()
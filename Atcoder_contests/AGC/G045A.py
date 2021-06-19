def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())

def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    a = LI()
    s = input()
    x = 0
    for i in range(n):
      if s[i] == '1' and a[i] != x:
        ans = 1
        x = x ^ a[i]
      elif s[i] == '0' and a[i] == x:
        ans = 0
    print(ans)

if __name__ == '__main__':
  main()

  # 最終的にってことラウンドの数は与えられている
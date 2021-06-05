def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
  
def main():
  m = int(input())
  a = LI()
  ans = 0
  if a.count(1) == 1:
    print(1)
    exit()
  n = max(a)
  num = [True]*(n+1)
  num[0] = num[1] = False
  a.sort()
  for i in range(m):
    if (i != m-1 and a[i]==a[i+1]) or (i != 0 and a[i]== a[i-1]): num[a[i]] = False
    for j in range(a[i]*2, n+1, a[i]):
      num[j] = False
  for aa in a:
    if num[aa]:
      ans += 1
  print(ans)

if __name__ == '__main__':
  main()
def main():
  n = int(input())
  a, b = [0]*n, [0]*n
  mina = 1001001001001
  maxb = 1
  for _ in range(n):
    a[_], b[_] = map(int, input().split())
  
  mina = min(a)
  maxb = max(b)
  ab = a + b
  ans = 1001001001001
  for en in ab:
    for ex in ab:
      memo = 0
      for i in range(n):
        memo += abs(en - a[i]) + abs(a[i] - b[i]) + abs(b[i] - ex)
      ans = min(ans, memo)
  print(ans)
  

if __name__ == '__main__':
  main()
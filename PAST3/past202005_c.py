a, r, n = map(int, input().split())

if a * r ** (n-1) <= 10**9:
  print(a*r**(n-1))
else:
  print('large') 
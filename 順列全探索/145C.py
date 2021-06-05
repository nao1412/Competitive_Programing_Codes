from itertools import permutations

n = int(input())
x, y = [0]*n, [0]*n
for i in range(n):
  x[i], y[i] = map(int, input().split())

def dist(a, b):
  dx = x[a] - x[b]
  dy = y[a] - y[b]
  return (dx**2 + dy**2)**0.5

ans = 0
np = [x for x in range(n)]
p = list(permutations(np))
for a in p:
  memo = 0
  for i in range(n-1):
    memo += dist(a[i],a[i+1])
  ans += memo
print(ans / len(p))
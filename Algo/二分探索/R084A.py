from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
c.sort()

res = 0
for j in b:
  res += bisect_left(a, j) * (n - bisect_right(c, j))
print(res)
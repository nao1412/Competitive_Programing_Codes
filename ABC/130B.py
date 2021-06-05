#ABC 130B
n, x = map(int, input().split())
l = list(map(int, input().split()))
d = 0
cnt = 1
for i in l:
   d += i
   if d <= x:
      cnt += 1
print(cnt)
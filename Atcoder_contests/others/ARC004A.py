import math

n = int(input())
x = [0]*n
y = [0]*n
ans = 0
for i in range(n):
    x[i], y[i] = map(int, input().split())
for i in range(n-1):
    for j in range(i+1, n):
        lg = (x[i]-x[j])**2 + (y[i]-y[j])**2
        if ans < lg:
            ans = lg
print(math.sqrt(ans))
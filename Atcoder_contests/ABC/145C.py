n = int(input())
x, y = [0]*n, [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())

kyi = 0
for i in range(n-1):
    for j in range(i+1,n):
        kyi += ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5

print(kyi * 2 / n)
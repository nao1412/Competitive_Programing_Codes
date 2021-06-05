n, a, b = map(int,input().split())

y = 0
for i in range(n+1):
    x = 0
    j = i
    while j > 0:
        x += j % 10
        j //= 10
    if x >= a and x <= b:
        y += i
print(y)

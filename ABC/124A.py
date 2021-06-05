a, b = map(int,input().split())
x = 0
for i in range(2):
    if a <= b:
        x += b
        b -= 1
    else:
        x += a
        a -= 1
print(x)
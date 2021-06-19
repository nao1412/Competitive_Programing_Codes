n = int(input())
s = 0
d = list(map(int, input().split()))
for i in range(n):
    for j in range(n-i-1):
        s += d[i] * d[i+j+1]
print(s)
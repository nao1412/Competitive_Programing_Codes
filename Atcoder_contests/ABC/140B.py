n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
m = 0
for i in range(n):
    m += b[i]
    if i != n-1 and a[i+1] == a[i] + 1:
        m += c[a[i]-1]
print(m)
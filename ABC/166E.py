n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] + a[j] == abs(i-j):
            ans += 1
print(ans)
n = int(input())
a = list(map(int, input().split()))

dp = [0]*n

for i in range(1, n):
    if i > 1:
        dp[i] = min(dp[i-2]+abs(a[i]-a[i-2]), dp[i-1]+abs(a[i]-a[i-1]))
    else:
        dp[i] = abs(a[i]-a[i-1])
        
print(dp[n-1])
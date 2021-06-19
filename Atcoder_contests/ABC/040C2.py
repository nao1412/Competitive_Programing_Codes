n = int(input())
a = list(map(int, input().split()))

dp = [10**5]*n
dp[0] = 0

for i in range(n-1):
    if i < n-2:
        dp[i+1] = min(dp[i+1], dp[i]+abs(a[i]-a[i+1]))
        dp[i+2] = min(dp[i+2], dp[i]+abs(a[i]-a[i+2]))
    else:
        dp[i+1] = min(dp[i+1], dp[i]+abs(a[i]-a[i+1]))

print(dp[n-1])
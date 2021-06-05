y = int(input())
dp = [0]*99
dp.insert(0,1)
if y >= 2000:
    print(1)
else:
    for x in range(100,y+1):
        if dp[x-100] == 1 or dp[x-101] == 1 or dp[x-102] == 1 or dp[x-103] == 1 or dp[x-104] == 1 or dp[x-105] == 1:
            dp.append(1)
        else:
            dp.append(0)

    print(dp[y])
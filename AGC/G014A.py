cookie = list(map(int, input().split()))
sc = sum(cookie)
cnt = 0
if cookie[0] == cookie[1] and cookie[1] == cookie[2] and cookie[0]%2 == 0:
    print(-1)
    exit()
memo = [0]*3
while cookie[0]%2 == 0 and cookie[1]%2 == 0 and cookie[2]%2 == 0:
    memo[0] = (cookie[1] + cookie[2]) // 2
    memo[1] = (cookie[0] + cookie[2]) // 2
    memo[2] = (cookie[1] + cookie[0]) // 2
    for i in range(3):
        cookie[i] = memo[i]
    cnt += 1

print(cnt)
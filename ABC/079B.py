n = int(input())
memo = [2, 1]
if n == 1:
    print(memo[n])
    exit()
else:
    for i in range(1,n):
        tmp = memo[1]
        memo[1] = memo[0] + tmp
        memo[0] = tmp

print(memo[1])
n = int(input())
a = [int(input()) for i in range(n)]

ans = 0
res = a[0]
for i in range(n):
    ans += 1
    if res == 2:
        print(ans)
        exit()
    res = a[res-1]
    

print(-1)
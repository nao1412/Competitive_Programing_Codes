n = int(input())
a = [0]*n
for i in range(n):
    a[i] = int(input())

# a = [int(input()) for _ in range(n)]

now = a[0]
cnt = 0

while cnt <= n:
    cnt += 1
    if now == 2:
        print(cnt)
        exit()
    now = a[now-1]

print(-1)
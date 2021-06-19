a, b = map(int, input().split())
m = 1
cnt = 0
while m < b:
    m += a-1
    cnt += 1
print(cnt)
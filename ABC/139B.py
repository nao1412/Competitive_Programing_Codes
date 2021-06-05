a, b = map(int, input().split())
cnt = 0
c = 1
while c < b:
    c += a - 1
    cnt += 1
print(cnt)
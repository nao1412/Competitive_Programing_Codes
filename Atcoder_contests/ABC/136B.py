n = int(input())
cnt = 0
for k in range(1,n+1):
    if k >= 1 and k <= 9:
        cnt += 1
    elif k >= 100 and k <= 999:
        cnt += 1
    elif k >= 10000 and k <= 99999:
        cnt += 1
print(cnt)
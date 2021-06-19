n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    minj = i
    for j in range(i,n):
        if a[j] < a[minj]:
            minj = j
    if i != minj:
        cnt += 1
    tmp = a[i]
    a[i] = a[minj]
    a[minj] = tmp

print(*a)
print(cnt)

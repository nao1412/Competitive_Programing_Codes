# Bubble Sort

n = int(input())
a = list(map(int, input().split()))

cnt = 0
flag = 1
while flag:
    flag = 0
    for j in range(n-1,0,-1):
        if a[j] < a[j-1]:
            tmp = a[j]
            a[j] = a[j-1]
            a[j-1] = tmp
            flag = 1
            cnt += 1

print(*a)
print(cnt)
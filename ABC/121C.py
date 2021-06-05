n, m = map(int, input().split())
a = [0]*n
for i in range(n):
    a[i] = list(map(int, input().split()))

# flag = 1
# while flag:
#     flag = 0
#     for j in range(n-1):
#         if a[j] > a[j+1]:
#             tmp = a[j]
#             a[j] = a[j+1]
#             a[j+1] = tmp
#             res = b[j]
#             b[j] = b[j+1]
#             b[j+1] = res
#             flag = 1

a.sort()  # key=lambda x: x[0]

ans = 0
for i in range(n):
    if m > a[i][1]:
        ans += a[i][0]*a[i][1]
        m -= a[i][1]
    else:
        ans += m*a[i][0]
        break

print(ans)
a = []
for i in range(3):
    aa = list(map(int, input().split()))
    a.append(aa)
n = int(input())
b = [0]*n
for i in range(n):
    b[i] = int(input())

for x in b:
    for i in range(3):
        for j in range(3):
            if x == a[i][j]:
                a[i][j] = -1
ans = 'No'
for i in range(3):
    if a[i][0] == a[i][1] and a[i][1] == a[i][2]:
        ans = 'Yes'

for i in range(3):
    if a[0][i] == a[1][i] and a[1][i] == a[2][i]:
        ans = 'Yes'

if a[0][2] == a[1][1] and a[1][1] == a[2][0]:
    ans = 'Yes'

if a[0][0] == a[1][1] and a[1][1] == a[2][2]:
    ans = 'Yes'

print(ans)
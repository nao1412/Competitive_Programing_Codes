N = int(input())
d = [int(input()) for i in range(N)] #中身がstrで処理されてしまわないように、intを前につける
d.sort()
j = 0
k = 0
for i in range(N):
    if(j < d[i]):
        k += 1
        j = d[i]
print(k)

N = int(input())
d = [int(input()) for i in range(N)]
d.sort()
j = 0
k = 0
for i in range(N):
    if(j < d[i]):
        k += 1
        j = d[i]
print(k)

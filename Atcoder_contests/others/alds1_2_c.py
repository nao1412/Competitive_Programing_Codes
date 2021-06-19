n = int(input())
a = list(map(str, input().split()))

def bubble(n, a):
    flag = 1
    while flag:
        flag = 0
        for i in range(n-1):
            if a[i][1] > a[i+1][1]:
                tmp = a[i][1]
                a[i][1] = a[i+1][1]
                a[i+1][1] = tmp
                flag = 1
    return a

def selection(n, a):
    for i in range(n):
        minj = i
        for j in range(i+1, n):
            if a[minj][1] > a[j][1]:
                minj = j
        tmp = a[minj][1]
        a[minj][1] = a[i][1]
        a[i][1] = tmp
    
    return a
    
b = [0]*n
for i in range(n):
    b[i] = a[i]

print(*bubble(n,a))
print('Stable')

print(*selection(n,a))
if bubble(n,a) == selection(n,a):
    print('Stable')
else:
    print('Not stable')
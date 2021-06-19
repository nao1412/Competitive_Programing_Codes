a = list(map(int, input().split()))

a.sort()
if (a[1]-a[0]) % 2 == 0:
    print((a[2]*3 - sum(a)) // 2)
else:
    print(((a[2]+1)*3 - sum(a)) // 2)
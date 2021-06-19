n, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
if x == sum(a):
    print(n)
elif x > sum(a):
    print(n-1)
else:
    for i in range(n):
        if x < a[i]:
            print(i)
            break
        x -= a[i]
        
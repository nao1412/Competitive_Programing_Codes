#161C
n, k = map(int, input().split())
z = n%k
if z == 0:
    print(0)
else:
    print(min(k-z, k-(k-z)))
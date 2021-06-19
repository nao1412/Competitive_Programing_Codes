import sys

n = int(input())
h = [int(i) for i in input().split()]
for k in range(n):
    if k == n-1:
        break
    if h[k+1] > h[k]:
        h[k+1] -= 1
    elif h[k+1] < h[k]:
        print('No')
        sys.exit()
    if k+1 == n-1:
        break
print('Yes')
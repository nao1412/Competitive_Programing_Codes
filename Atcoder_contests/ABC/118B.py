n, m = map(int, input().split())
k = []
for i in range(n):
    a = list(map(int, input().split()))
    k.append(a)

ans = [0]*m
for i in range(n):
    for j in range(1,k[i][0]+1):
        ans[k[i][j]-1] += 1

print(ans.count(n))
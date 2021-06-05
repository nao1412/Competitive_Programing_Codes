a, b, k = map(int ,input().split())
if b-a+1 <= k:
    k = b-a+1
ans = []
for i in range(k):
    print(a+i)
    ans.append(a+i)
for i in range(-k+1,1):
    if b+i not in ans:
        print(b+i)
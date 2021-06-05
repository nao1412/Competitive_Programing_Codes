#ABC 142C
n = int(input())
a = list(map(int, input().split()))
ans = [0] * n
for idx,i in enumerate(a, 1):
   ans[i-1] = idx
print(*ans)
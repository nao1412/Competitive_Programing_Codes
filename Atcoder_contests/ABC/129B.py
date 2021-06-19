n = int(input())
w = list(map(int, input().split()))
ans = 10010
for i in range(n):
  ans = min(ans, abs(sum(w[:i]) - sum(w[i:])))

print(ans)
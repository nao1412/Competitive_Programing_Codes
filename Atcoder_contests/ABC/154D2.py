n, k = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = [(p+1)/2 for p in P]
c = [0]
for q in Q:
   c.append(c[-1]+q)
ans = 0
for i in range(k, n+1):
   ans = max(ans, c[i] - c[i-k])
print(ans)
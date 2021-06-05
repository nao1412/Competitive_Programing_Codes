n = int(input())
r = [0]*n
for i in range(n):
    r[i] = int(input())

r_min = r[0]
ans = -2000000000
for i in range(1, n):
    ans = max(ans, r[i] - r_min)
    r_min = min(r[i], r_min) 
    
print(ans)

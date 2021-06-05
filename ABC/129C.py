n, m = map(int, input().split())
a = {int(input()) for _ in range(m)}

s = [1]*(n+1)

if 1 in a:
    s[1] = 0

for i in range(n-1):
    if i+2 in a:
        s[i+2] = 0
        continue
    s[i+2] = (s[i+1] + s[i]) % (10**9+7)
    
print(s[-1])
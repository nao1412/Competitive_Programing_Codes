s = str(input())
cnt = 0
sle = len(s)
n = int(sle/2-1)
for a in range(n+1):
    if s[a] != s[sle-a-1]:
            s.replace(s[a],s[sle-a-1])
            cnt += 1
print(cnt)

s = input()
t = input()
ans = 'Yes'
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    else:
        ans = 'No'
print(ans)
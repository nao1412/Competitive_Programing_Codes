s = input()
cnt = 0
ans = 0
for i in range(len(s)):
  if s[i] == 'A' or s[i] == 'T' or s[i] == 'G' or s[i] == 'C':
    cnt += 1
  else:
    ans = max(ans, cnt)
    cnt = 0
  
print(max(ans, cnt))
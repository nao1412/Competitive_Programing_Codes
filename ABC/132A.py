s = str(input())
judge = 'No'
for i in range(len(s)):
    if s.count(s[i]) == 2:
        judge = 'Yes'
    else:
        judge = 'No'
        break
print(judge)

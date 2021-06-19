s = str(input())
ans = 'Good'
for i in range(3):
    if i == 3:
        break
    elif s[i] == s[i+1]:
        ans = 'Bad'
print(ans)
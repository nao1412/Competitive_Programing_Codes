s = input()
memo = []
ans = 'yes'
for i in s:
    if i not in memo:
        memo.append(i)
    else:
        ans = 'no'
        break

print(ans) 
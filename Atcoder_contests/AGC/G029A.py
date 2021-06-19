s = input()
b = 0
ans = 0
for i in range(len(s)):
    if s[i] == 'W':
        ans += i - b
        b += 1

print(ans)

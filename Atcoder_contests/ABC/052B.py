n = int(input())
s = input()
cnt = 0
ans = 0
for i in range(n):
    if s[i] == 'I':
        cnt += 1
    elif s[i] == 'D':
        cnt -= 1
    ans = max(ans, cnt)

print(ans)
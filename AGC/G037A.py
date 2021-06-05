s = input()

now = ''
pre = ''
ans = 0
for i in s:
    now += i
    if pre != now:
        ans += 1
        pre = now
        now = ''
print(ans)
s = input()
n = len(s)

ans = 0
i = n
while True:
    if ans != 0 and s[0:i//2] == s[i//2:i]:
        print(n - ans)
        exit()
    i -= 2
    ans += 2
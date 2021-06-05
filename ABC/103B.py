s = input()
t = input()

for i in range(len(s)):
    f = s[0]
    ss = s[1:]
    s = ss
    s += f
    if s == t:
        print('Yes')
        exit()

print('No')
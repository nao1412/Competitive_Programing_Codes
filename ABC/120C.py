s = input()
a,b = 0,0
for i in range(len(s)):
    if s[i] == '0':
        a += 1
    else:
        b += 1

print(min(a,b)*2)
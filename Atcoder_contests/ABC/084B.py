a,b = map(int, input().split())
s = input()

for i in range(a):
    if not '0' <= s[i] and s[i] <= '9':
        print('No')
        exit()

if s[a] != '-':
    print('No')
    exit()

for i in range(a+1, a+b+1):
    if not '0' <= s[i] and s[i] <= '9':
        print('No')
        exit()

print('Yes')

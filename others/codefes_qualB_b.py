n, a, b = map(int, input().split())
s = input()
tuka = 0
br = 0
for i in range(n):
    if s[i] == 'a':
        if tuka < a+b:
            print('Yes')
            tuka += 1
        else:
            print('No')
    elif s[i] == 'b':
        if tuka < a+b and br < b:
            print('Yes')
            tuka += 1
            br += 1
        else:
            print('No')
            br += 1
    else:
        print('No')
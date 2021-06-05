s = input()
ans = 'AC'
if s[0] != 'A':
    print('WA')
    exit()
else:
    s = s[1:]
if 'C' not in s[1:-1]:
    print('WA')
    exit()
else:
    if s.count('C') != 1:
        print('WA')
        exit()
    else:
        ss = s.replace('C','')
        if ss.islower():
            print('AC')
        else:
            print('WA')


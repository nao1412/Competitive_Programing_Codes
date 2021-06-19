s = input()

if ('N' in s and 'S' in s) or ('N' not in s and 'S' not in s):
    if ('W' in s and 'E' in s) or ('W' not in s and 'E' not in s):
        print('Yes')
        exit()

print('No')

s = input()
odd = s[0::2]
odd = ','.join(odd)
odd.split(',')
even = s[1::2]
even = ','.join(even)
even.split(',')
if 'L'  not in odd and 'R' not in even:
    print('Yes')
else:
    print('No')
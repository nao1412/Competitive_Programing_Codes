s = input()
if 'eraser' in s:
    s.replace('eraser','')
if 'erase' in s:
    s.replace('erase','')
if 'dreamer' in s:
    s.replace('dreamer','') #元の文字列は変わっていない
if 'dream' in s:
    s.replace('dream','') #stripメソッドは両端からはぎとるものだから使えない

print(s)
emp = len(s)
print(emp)
if emp == 0:
    print('YES')
else:
    print('NO')
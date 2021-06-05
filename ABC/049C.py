s = input()
if 'eraser' in s:
    s = s.replace('eraser','')
if 'erase' in s:
    s = s.replace('erase','')
if 'dreamer' in s:
    s = s.replace('dreamer','') 
if 'dream' in s:
    s = s.replace('dream','') #ifなんちゃらはひつようない
#s = input().replace....
emp = len(s)
if emp == 0: #if s:
    print('YES')
else:
    print('NO')
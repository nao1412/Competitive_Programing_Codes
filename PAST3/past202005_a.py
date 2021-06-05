s = input()
t = input()
if s == t:
  print('same')
  exit()
else:
  ans = 'different'
  for i in range(3):
    if s[i] == t[i]: continue
    else:
      if s[i].swapcase() == t[i]:
        ans = 'case-insensitive'
      else:
        ans = 'different'
        break
  print(ans)

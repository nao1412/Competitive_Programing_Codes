t = list(input())
n = len(t)
for i in range(n):
  if t[i] == '?':
    t[i] = 'D'
print(''.join(t))

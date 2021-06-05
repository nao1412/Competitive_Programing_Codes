# b = input()
# if b == 'A':
#     print('T')
# elif b == 'T':
#     print('A')
# elif b == 'G':
#     print('C')
# else:
#     print('G')
b = input()
c = []
for i in range(len(b)):
  if b[i] == 'A':
    c.append('T')
  elif b[i] == 'T':
    c.append('A')
  elif b[i] == 'G':
    c.append('C')
  else:
    c.append('G')
print(''.join(c))
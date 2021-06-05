n = int(input())
s = input()
cnr = 0
for i in range(n-2):
  if s[i:i+3] == 'ABC':
    cnr += 1
print(cnr)
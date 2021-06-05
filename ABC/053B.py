s = input()

for i in range(len(s)):
    if s[i] == 'A':
        a = i
        break
for i in range(-1,-len(s),-1):
    if s[i] == 'Z':
        b = len(s) + i
        break

print(b-a+1)
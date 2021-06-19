s = input()
l = len(s)
n = [0] * (l+1)

for i in range(l):
    if s[i] == '<':
        n[i+1] = n[i] + 1

for i in reversed(range(l)):
    if s[i] == '>':
        n[i] = max(n[i+1] + 1, n[i])

print(sum(n))
import collections
n = int(input())
sg = []
for _ in range(n):
    s = input()
    sg.append(s)
sgc = collections.Counter(sg)
print(len(sgc))
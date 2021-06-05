h, w =map(int, input().split())
a = ['#'*(w+2)]
for i in range(h):
    aa = '#' + input() + '#'
    a.append(aa)
a.append('#'*(w+2))
print('\n'.join(a))
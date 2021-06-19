def sm(i, l):
    if i == n-1:
        return sum(list(map(int, l.split('+'))))
    return sm(i+1, l+s[i+1]) + sm(i+1, l+'+'+s[i+1])

s = input()
n = len(s)

print(sm(0, s[0]))

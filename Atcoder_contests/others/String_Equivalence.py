n = int(input())
alphabet = 'abcdefghij'

def ans(n):
    if n == 1:
        return ['a']
    ret = []
    for s in ans(n-1):
        l = len(set(s))
        for i in range(l+1):
            ret.append(s + alphabet[i])
    return ret

for s in ans(n):
    print(s)

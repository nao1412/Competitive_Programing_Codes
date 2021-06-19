k = int(input())
l = [1,2,3,4,5,6,7,8,9]

def dfs(d, a, b):
    if d == 10:
        return 
    for i in [-1,0,1]:
        a *= 10 + (a%10+i)
        b.append(a)
        dfs(d+1, a)
        a //= 10
    return l

for x in [1,2,3,4,5,6,7,8,9]:
    dfs(1, x, l)
l_s = sorted(l)
print(l)
print(l_s[k])
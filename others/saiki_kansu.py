n = 5
m = 3

def dfs(a):
    global n
    global m
    if len(a) == n:
        return 
    for v in range(m):
        a.append(v)
        dfs(a)
        a.pop()


dfs([])
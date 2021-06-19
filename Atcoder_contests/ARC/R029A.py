n = int(input())
t = [int(input()) for i in range(n)]
ans = 200

def dfs(i, a, b):
    global ans 
    if i == n-1:
        ans = min(ans, max(a, b))
    else:
        dfs(i+1, a+t[i+1], b)
        dfs(i+1, a, b+t[i+1])
    return ans
        
print(dfs(0, t[0], 0))
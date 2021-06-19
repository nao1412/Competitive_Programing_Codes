n, m, q = map(int, input().split())
a = [0]*q
b = [0]*q
c = [0]*q
d = [0]*q
for i in range(q):
    a[i],b[i],c[i],d[i] = map(int,input().split())
    a[i] -= 1
    b[i] -= 1

def score(A):
    tmp = 0
    for ai, bi, ci, di in zip(a, b, c, d):   
        if A[bi] - A[ai] == ci:               
            tmp += di                        
    return tmp                               
    # for i in range(q):
    #     if A[b[i]]-A[a[i]] == c[i]:
    #         tmp += d[i]
    # return tmp

def dfs(A):
    if len(A) == n:
        return score(A)   
    res = 0
    if len(A) > 0:                # prev_last = A[-1] if len(A) > 0 else 0
        prev_last = A[-1] 
    else:
        prev_last = 0
    for i in range(prev_last, m):
        A.append(i)
        res = max(res, dfs(A))    # 再起を呼び出しながら、最大値の更新
        A.pop()
    return res

print(dfs([]))
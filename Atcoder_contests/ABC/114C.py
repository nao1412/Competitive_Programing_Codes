n = int(input())

def dfs(a):
    if int(a) > n:
        return 0
    ret = 1 if all(a.count(c) > 0 for c in '753') else 0
    for v in '753':
        a += v
        ret += dfs(a)  # この3行を ret += dfs(a+v) とも書ける
        a = a[:-1]  # numはそのまま繰り返される
    return ret


print(dfs('0'))
n = int(input())
k = int(input())
x = list(map(int, input().split()))

def f(n, k, x):
    rtn = 0
    for i in range(n):
        rtn += min(x[i], k-x[i]) * 2
    return rtn

print(f(n, k, x))
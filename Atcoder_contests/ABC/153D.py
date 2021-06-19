h = int(input())

# dp = [1]*h
# for i in range(1,h):
#     dp[i] = dp[(i+1)//2 - 1] * 2 + 1

# print(dp[-1])

# for i in range(h):
#     if 2**i <= h and h < 2**(i+1):
#         a = i
#         break

# ans = 1
# for i in range(a):
#     ans = ans * 2 + 1

# print(ans)

def f(x):
    if x == 1: return 1
    a = f(x//2)
    return a*2 + 1

print(f(h))
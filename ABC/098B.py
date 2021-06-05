n = int(input())
s = input()

cs = [0]*(n-1)

for i in range(n-1):
    cnt = 0
    memo = []
    for j in s[0:i+1]:
        if j in s[i+1:n] and j not in memo:
            cnt += 1
        memo.append(j)
        
    cs[i] = cnt

print(max(cs))
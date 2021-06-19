n = int(input())
s = [0]*n
for i in range(n):
    s[i] = int(input())

s_sum = sum(s)
s_sort = sorted(s)

if s_sum % 10 == 0:
    for i in range(n):
        if s_sort[i] % 10 != 0:
            s_sum -= s_sort[i]
            ans = s_sum
            break
        else:
            ans = 0
    print(ans)
else:
    print(s_sum)

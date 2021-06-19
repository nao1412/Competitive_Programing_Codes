s = input()
t = input()

ss = sorted(s)
tt = sorted(t, reverse=True)

if ss < tt:
    print('Yes')
else:
    print('No')


# ss = [s[i] for i in range(n)]
# tt = [t[i] for i in range(m)]
# ss.sort()
# tt.sort(reverse=True)

# for i in range(n):
#     if ss[i] < tt[i]:
#         print('Yes')
#         exit()
#     elif ss[i] > tt[i]:
#         print('No')
#         exit()

# if n < m:
#     print('Yes')
# else:
#     print('No')

ae = [int(input()) for _ in range(5)]

sum_ae = 0
g = 9
cnt = 0  
for i in ae:
    if i % 10 != 0:
        g = min(g, i % 10)
        sum_ae += (i//10 + 1) * 10
        cnt += 1
    else:
        sum_ae += i
if cnt != 0:
    print(sum_ae - (10-g))
else:
    print(sum_ae)

# import itertools
# p = list(itertools.permutations(ae))
# print(p)
# for _ in range(120):
#     ans = 0
#     for i in range(5):
#         while ans % 10 != 0:
#             ans += 1
#         ans += ae[p[i]]
#     final_anser = min(final_anser, ans)

# print(final_anser)
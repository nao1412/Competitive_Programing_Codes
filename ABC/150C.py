# import itertools

# n = int(input())
# p = tuple(map(int, input().split())) # 横入力
# q = tuple(map(int, input().split())) # 横入力
# seq = list(range(1,n+1))
# nnn = list(itertools.permutations(seq, n))
# print(abs(nnn.index(q) - nnn.index(p)))


n = int(input())
p = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]

# 階乗
def kai(x):
    a = 1
    for i in range(1, x + 1):
        a *= i
    return a

al= list(range(1,n+1))
j = n-1
a = 0
for i in p:
    a += al.index(i) * kai(j)
    j -= 1
    al.remove(i)

al = list(range(1, n+1))
j = n-1
b = 0
for i in q:
    b += al.index(i) * kai(j)
    j -= 1
    al.remove(i)

print(abs(a-b))

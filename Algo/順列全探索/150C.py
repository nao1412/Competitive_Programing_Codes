from itertools import permutations
n = int(input())
a = tuple(map(int ,input().split()))
b = tuple(map(int ,input().split()))

np = [i for i in range(1, n+1)]
p = list(permutations(np))
ai = p.index(a)
bi = p.index(b)
print(abs(ai-bi))
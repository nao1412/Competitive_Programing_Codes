a, b, k = map(int, input().split())
memo = []
for i in range(min(a, b)):
  if a % (i+1) == 0 and b % (i+1) == 0:
    memo.append(i+1)

print(memo[-k])
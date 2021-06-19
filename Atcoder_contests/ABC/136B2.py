n = int(input())
cnt = 0
for i in range(1,n+1):
  if i // 10 == 0 or 10 <= i//10 < 100 or 1000 <= i//10 < 10000:
    cnt += 1
print(cnt)

# 解説
N = int(input())
2 print(len(list(filter(lambda x: len(str(x)) % 2 == 1, range(1, N + 1)))))


l = ['Alice', 'Bob', 'Charle']
l = sorted(l, key=lambda x: x[1])
print(l)
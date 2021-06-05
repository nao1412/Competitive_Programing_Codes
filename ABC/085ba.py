N = int(input())
d = [int(input()) for i in range(N)]
d_sorted = sorted(d)
size = 0
count = 0
for i in range(N):
    if(size < d_sorted[i]):
        count += 1
        size = d_sorted[i]
print(count)

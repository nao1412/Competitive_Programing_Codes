#ABC 133C
l, r = map(int, input().split())
ans = 2019
for i in range(l, r):
    for j in range(i+1, r+1):
        tmp = i*j % 2019
        if ans > tmp:
            ans = tmp
        if ans == 0:
            print(ans)
            exit(0)
print(ans)


# num_map = list(map(lambda j: j % 2019, num)) 
# num_map.sort()
# print(num_map[0]*num_map[1])
abc = list(map(int, input().split()))
for i in range(3):
    if abc[i] % 2 == 0:
        print(0)
        exit()
abc.sort()
print(abc[0]*abc[1])
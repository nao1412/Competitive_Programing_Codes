x = int(input())
if x >= 2000:
    print(1)
else:
    c = x//100 + 1
    am = x%100
    for i in range(c):
        for j in range(c-i):
            for k in range(c-i-j):
                for l in range(c-i-j-k):
                    for m in range(c-i-j-l):
                        if am == i*5 + j*4 + k*3 + l*2 + m*1:
                            print(1)
                            exit()
    print(0)

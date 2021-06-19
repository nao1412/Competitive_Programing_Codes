n = int(input())
num = [1,2,3,4,5,6]
i = 0
mod = 5
nn = n % 30
while i < nn:
    tmp = num[i % mod]
    num[i % mod] = num[i % mod + 1]
    num[i % mod + 1] = tmp
    i += 1
        
numnum = [str(a) for a in num]
print(''.join(numnum))
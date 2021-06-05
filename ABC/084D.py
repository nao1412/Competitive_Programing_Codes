q = int(input())
l, r = [0]*q, [0]*q
for i in range(q):
    l[i], r[i] = map(int, input().split())

MAX = 101010
is_prime = [1]*MAX
is_prime[0] = 0
is_prime[1] = 0
for i in range(2,MAX):
    if not is_prime[i]: 
        continue
    for j in range(i*2, MAX, i):
        is_prime[j] = 0

a = [0]*MAX
for i in range(1,MAX,2):  # ,,2
    # if i%2 == 0: 
    #     continue
    if is_prime[i] and is_prime[(i+1)//2]: 
        a[i] = 1

s = [0]*(MAX+1)
for i in range(MAX): 
    s[i+1] = s[i] + a[i]

for i in range(q):
    print(s[r[i]+1]-s[l[i]])
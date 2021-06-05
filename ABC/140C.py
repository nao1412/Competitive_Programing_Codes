n = int(input())
b = list(map(int, input().split()))
amt = b[0] + b[n-2]
for i in range(n-1):
    if i != n-2 and b[i] <= b[i+1]:
        amt += b[i]
    elif i != n-2 and b[i] > b[i+1]:
        amt += b[i+1]
print(amt)
s = input()
ans = 0
memo = 0
for i in s:
    if i == 'A' or i == 'T' or i == 'C' or i == 'G':
        memo += 1
    else:
        ans = max(ans, memo)
        memo = 0
        
print(max(ans, memo))
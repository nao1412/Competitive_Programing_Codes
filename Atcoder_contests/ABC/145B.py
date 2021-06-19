n = int(input())
s = input()
judge = 'Yes'
if n % 2 == 0:
    for i in range(int(n/2)):
        if s[i] != s[i + int(n/2)]:  #s[:n//2] == s[n//2:] \n print('Yes')
            judge = 'No'
else:
    judge = 'No'
print(judge)
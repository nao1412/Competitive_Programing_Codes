s = input()
k = int(input())

if len(s) >= k and s[:k] == '1'*k:
    print(1)
else:
    for i in s:
        if i != '1':
            print(i)
            exit()
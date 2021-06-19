#Hitachi String A
s = input()
s1 = 'hi'
for i in range(5):
    if s == s1:
        print('Yes')
        exit()
    else:
        s1 += 'hi'
print('No')
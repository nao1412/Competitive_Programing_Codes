s = input()

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','None']

for i in s:
    if i in alpha:
        alpha.remove(i)

print(alpha[0])
n = int(input())
w = []
for i in range(n):
    s = input()
    w.append(s)

jdg = 'Yes'
if len(set(w)) != len(w):
    jdg = 'No'
    print(jdg)
    exit()

for i in range(1,n):
    if w[i-1][-1] != w[i][0]:
        jdg = 'No'
        break 
    
print(jdg)
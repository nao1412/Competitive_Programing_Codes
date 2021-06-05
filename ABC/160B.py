#160B
x = int(input())
pls = 0
y = x // 500
if y > 0:
    pls += y*1000
if (x-y*500) // 5 > 0:
    pls += ((x-y*500)//5)*5  
print(pls)
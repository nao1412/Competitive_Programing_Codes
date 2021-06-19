s = input()
ans = 999
for i in range(len(s)-2):
    lun = int(s[i] + s[i+1] + s[i+2])
    ans = min(abs(753-lun), ans)
print(ans)
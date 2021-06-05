n = int(input())
s = input()
t = input()
cnt = 0
for i in range(n):
  if s[-1-i:] == t[:i+1]:
    cnt = i + 1
print(n*2-cnt)
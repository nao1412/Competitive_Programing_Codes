h, w = map(int, input().split())
s = ['#'*w]*(h+2)
for i in range(1,h+1):
    s[i]= '#' + input() + '#'
s[h+1] = '#'*w
from collections import deque

print(s)
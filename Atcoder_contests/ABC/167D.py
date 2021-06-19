import sys
import math
sys.setrecursionlimit(10**7)
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
    n, k = MI()
    a = LI()
    
    s = []
    ord = [-1]*(n+1)
    v = 1
    while ord[v] == -1:
        ord[v] = len(s)
        s.append(v)
        v = a[v-1]
    c = len(s) - ord[v]
    l = ord[v]
    if k < l: print(s[k])
    else:
        k -= l
        k %= c
        print(s[l+k])

if __name__ == '__main__':
  main()
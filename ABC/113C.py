import sys
sys.setrecursionlimit(10**7) # 再帰回数を増やす
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def S(): return input()
def LS(): return list(map(str, input().split()))
mod = 10**9 + 7

def main():
  n, m = MI()
  c = []
  for i in range(m):
    a, b = MI()
    c.append([i,a,b])
  
  c = sorted(c, key=lambda x:(x[1], x[2]))

  ID = [0]*m
  cnt = 0
  now = c[0][1]
  for city in c:
    if now == city[1]: cnt += 1
    else: cnt = 1
    ID[city[0]] = '0'*(6 - len(str(city[1]))) + str(city[1]) + '0'*(6-len(str(cnt))) + str(cnt)
    now = city[1]
  [print(i) for i in ID]
  
if __name__ == '__main__':
  main()

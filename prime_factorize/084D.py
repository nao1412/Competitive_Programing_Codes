def l(): return list(map(int, input().split()))
def m(): return map(int, input().split())

def sieve(n): # エラトステネスの篩ですよ
  num = [True]*n
  num[0] = num[1] = False
  for i in range(2,int(n**0.5)+1):
    if num[i]:
      for j in range(i**2, n, i):
        num[j] = False
  return [i for i in range(2,n) if num[i]]

def main():
  q = int(input())
  l , r = [0]*q, [0]*q
  for i in range(q):
    l[i], r[i] = m()
  rr = max(r) 
  prime = sieve(rr+1)
  # print(prime)
  likp = [0]*rr
  for i in prime:
    if (i+1) // 2 in prime:
      likp[i-1] = 1
  # print(likp)
  sm = [0]*(rr+1)
  for i in range(rr):
    sm[i+1] = sm[i] + likp[i]
  # print(sm)
  for i in range(q):
    print(sm[r[i]] - sm[l[i]-1])

if __name__ == '__main__':
  main()

def lt(): return list(map(int, input().split()))
def mp(): return map(int, input().split())

def main():
  n, m = mp()
  k = [0]*(n-1)
  for i in range(n-1):
    k[i] = int(input())
  s = [0]*m
  for i in range(m):
    s[i] = int(input())

  ksm = [0]*n
  for i in range(n-1):
    ksm[i+1] = ksm[i] + k[i]
  now = 0
  ans = 0
  for i in range(m):
    ans += abs(ksm[now + s[i]] - ksm[now])
    now += s[i]

  print(ans % 10**5)
if __name__ == '__main__':
  main()
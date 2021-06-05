def lp(): return list(map(int, input().split()))
def mp(): return map(int, input().split())

def main():
  n = int(input())
  a = []
  if n == 1: 
    print('Not Prime')
    exit()
  while n % 2 == 0:
    n //= 2
    a.append(2)
  f = 3
  while f**2 <= n:
    if n % f == 0:
      a.append(f)
      n //= f
    else:
      f += 2
  if n != 1:
    a.append(n)
  if len(a) == 1:
    ans = 'Prime'
  elif 2 not in a and 3 not in a and 5 not in a:
    ans = 'Prime'
  else: ans = 'Not Prime'
  print(ans)
if __name__ == '__main__':
  main()
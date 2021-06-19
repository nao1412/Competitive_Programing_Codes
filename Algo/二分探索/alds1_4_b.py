def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())
mod = 10**9 + 7

def binarysearch(n, a, cnt):
  left = 0
  right = n - 1
  while left < right:
    mid = (left + right) // 2
    if mid == a:
      return 1
    elif mid < a:
      left = mid + 1
    else:
      right = mid
  return 0

def main():
  n = int(input())
  s = LI()
  q = int(input())
  t = LI()
  cnt = 0
  for i in range(q):
    if t[i] > s[-1]:
      continue
    cnt += binarysearch(n, t[i], cnt)
  print(cnt)


  
if __name__ == '__main__':
  main()
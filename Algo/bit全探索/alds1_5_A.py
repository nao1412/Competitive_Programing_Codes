def main():
  n = int(input())
  a = list(map(int, input().split()))
  q = int(input())
  ques = list(map(int, input().split()))

  for k in range(q):
    ans = 'no'
    for i in range(2**n):
      abit = [0]*n
      for j in range(n):
        if ((i >> j) & 1): 
          abit[j] = 1
      
      cnt = 0
      if sum(a) < ques[k]: 
        ans = 'no'
      else:
        for j in range(n):
          if abit[j] == 1: cnt += a[j]
        if cnt == ques[k]: 
          ans = 'yes'
    print(ans)


if __name__ == '__main__':
  main()

# エラトステネスの篩

def sieve(n):
  num = [True]*(n+1)
  num[0] = num[1] = False
  for i in range(2,int(n**0.5)+1):
    if num[i]:
      for j in range(i**2, n+1, i):
        num[j] = False
  return num # 自然数が素数か素数じゃないかだけ




  # 素数のリストが欲しいなら↓
  # return [i for i in range(2,n+1) if num[i]]


# def eratosthenes(limit):
#   prime = [2]
#   for i in range(3,limit+1):
#     for j in prime:
#       if i % j == 0: break
#     else: prime.append(i)
#   return prime

n = int(input())
print(sieve(n), len(sieve(n)))

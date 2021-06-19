n = int(input())
for i in range(1, int(n**0.5) + 1):
  if n % i == 0:
    maxi = i

print(len(str(n//maxi)))

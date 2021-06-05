#ABC 131B
n, l = map(int, input().split())
apple = [l+i for i in range(n)]
apple.sort(key = lambda x:abs(x))
print(sum(apple[1:]))
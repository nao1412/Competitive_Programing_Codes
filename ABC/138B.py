n = int(input())
a = map(int, input().split())
print(1/sum(1/i for i in a))

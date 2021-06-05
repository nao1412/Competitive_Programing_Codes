q, h, s, d = map(int, input().split())
n = int(input())

l1 = min(h*2, q*4, s)
l2 = min(8*q, h*4, s*2, d)

ans = n//2 * l2 + n%2 * l1
print(ans)
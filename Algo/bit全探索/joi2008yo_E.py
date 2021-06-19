import numpy as np
r, c = map(int, input().split())
a = np.array([list(map(int, input().split())) for _ in range(r)])

ans = 0
for i in range(2**r):
  bit = np.array([[i >> j & 1 for j in range(r)]]).T
  black = (a^bit).sum(axis=0)
  ans = max(ans, np.fmax(r-black, black).sum())

print(ans)
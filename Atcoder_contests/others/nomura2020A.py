h1, m1, h2, m2, k = map(int ,input().split())

ss = m1 + h1 * 60
gg = m2 + h2 * 60

print(gg-ss-k)
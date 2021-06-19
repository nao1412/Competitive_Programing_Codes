d, g = map(int, input().split())
p = [0]*d
c = [0]*d
for i in range(d):
    p[i], c[i] = map(int, input().split())
    
def f(a, b):
    if a == 0:
        return 10*9
    n = min(b//(a*100), p[a-1])  # 最大点で必要な数と最大点の問題数
    score = a*100*n              # 最大点×問題数
    if n == p[a-1]:              # ボーナスがもらえた
        score += c[a-1]
    if score < b:                # 目標点に達してないとき   
        n += f(a-1, b-score)     # 何回も再起するかも
    return  min(n, f(a-1, b))    # その結果の n と a-1の時のn の小さいほう


print(f(d, g))
    
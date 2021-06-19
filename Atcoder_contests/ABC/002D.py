def main(): 
    n, m = map(int, input().split())
    g = [[0]*n for _ in range(n)]
    for i in range(n):
        g[i][i] = 1
    for i in range(m):
        x, y = map(int, input().split())
        g[x-1][y-1] = 1
        g[y-1][x-1] = 1
    # print(g)
    ans = 0
    for i in range(2**n):
        bit = [0]*n
        for j in range(n):
            if ((i >> j) & 1):
                bit[j] = 1
        
        cnt = 0
        for j in range(n):
            flag = True # すべての議員の関係について調べる
            for k in range(n):
                if bit[k] > g[j][k]: # もし派閥候補(bit)と関係が一致しないならFalse
                    flag = False # bitに入っていないとだめだけど、gに入っていなくともいい
            if flag: cnt += 1 # 関わりが多いのはいいが少ないのはNG
        # bitより関わりを多く持っていたらcnt +1
        if cnt == bit.count(1): # 正式な派閥のみカウント(重要)
            ans = max(ans, cnt)
                
    print(ans)

if __name__ == '__main__':
    main()

# bit全探索

# for i in range(2**n):    
#   bit = [i >> j & 1 for j in range(n)]

def main(): 
    n, m = map(int, input().split())
    g = [[0]*n for _ in range(n)]
    for i in range(m):
        x, y = map(int, input().split())
        g[x-1][y-1] = 1
        g[y-1][x-1] = 1
    
    ans = 0
    for i in range(2**n):
        bit = [0]*n
        for j in range(n):
            if (i >> j) & 1: #全探索するための二進数表記の数を作る
                bit[j] = 1
        
        for j in range(n):
            for k in range(n):

    print(ans)

if __name__ == '__main__':
    main()
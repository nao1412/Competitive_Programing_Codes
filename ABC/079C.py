def ans(i, j, k):
    if i == 3:
        if j == 7:
            print(k + '=7')
            exit()
    else:      #return ではなぜかけない？
        ans(i+1, j-int(n[i+1]), k+'-'+n[i+1]),
        ans(i+1, j+int(n[i+1]), k+'+'+n[i+1])

n = input()

ans(0, int(n[0]), n[0])


#これならおｋ

# def ans(i, j, k):
#     if i == 3:
#         if j == 7:
#             print(k + '=7')
#             exit()
#         return
#     ans(i+1, j-int(n[i+1]), k+'-'+n[i+1]), 
#     ans(i+1, j+int(n[i+1]), k+'+'+n[i+1])

n = int(input())
s = [input() for _ in range(n)]
import collections
c = collections.Counter(s)
d = c.most_common()
e = [d[0][0]]
for i in range(len(d)-1): #nじゃない　dの長さ
   if d[0][1] == d[i+1][1]:
      e.append(d[i+1][0])       #辞書順にする
e.sort()
print('\n'.join(e))   #print(repr(e))では改行コードがふくまれたものが出てくるはず
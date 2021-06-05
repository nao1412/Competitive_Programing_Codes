#ABC 131C
a, b, c, d = map(int, input().split())
def gcd(a,b):
   while b != 0:
      a, b = b, a%b
   return a
def lcm(a,b):
   return int(a*b / gcd(a,b))
cnt = 0
quo_c = b//c - (a-1)//c
quo_d = b//d - (a-1)//d
quo_cd = b//lcm(c,d) - (a-1)//lcm(c,d)
print(b - (a-1) - quo_c - quo_d + quo_cd)
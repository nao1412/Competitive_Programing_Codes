def LI(): return list(map(int, input().split()))
def I(): return map(int, input().split())


mod = 10**9 + 7


def main():
    n, a, b = I()
    s = input()
    yn = []
    for i in range(n):
        if s[i] == 'a':
            if a + b > 0:
                print('Yes')
                if a > 0:
                    a -= 1
                else:
                    b -= 1
            else:
                print('No')
        elif s[i] == 'b':
            if a + b > 0 and b > 0:
                print('Yes')
            else:
                print('No')
            if b > 0:
                b -= 1
        else:
            print('No')


if __name__ == '__main__':
    main()

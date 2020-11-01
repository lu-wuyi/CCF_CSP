n = int(input())
inlist = [int(i) for i in input().split()]

zuo = [[0 for j in range(5)] for i in range(20)]

def deal(n):
    ans = []
    need = [0]*n
    ok = 0
    for i in range(20):
        for j in range(5):
            if zuo[i][j] == 0 and j + n <= 5:
                for z in range(j,j+n):
                    zuo[i][z] = 1
                    ans.append(i*5+z+1)
                return ans
                    
    for i in range(20):
        for j in range(5):
            if zuo[i][j] == 0:
                zuo[i][j] = 1
                ans.append(i*5 + j + 1)
                n -= 1
            if n== 0:
                break
        if n== 0:
            break
    return ans

for i in inlist:
    a = deal(i)
    for j in a:
        print(j, end = '')
        if j != a[-1]:
            print(' ', end = '')
    print()

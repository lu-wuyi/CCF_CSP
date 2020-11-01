#得到输入
chushi = []
for i in range(15):
    chushi.append([int(j) for j in input().split()])
for i in range(4):
    chushi.append([1]*10)
bankuai = []
for i in range(4):
    bankuai.append([int(j) for j in input().split()])
n = int(input())

#处理函数，判断板块能下降到第几行
def check(c,b,m):
    for i in range(4):
        for j in range(4):
            if chushi[i+m][j+n-1] and bankuai[i][j]:
                    return m
    return check(c,b,m+1)

m = check(chushi, bankuai,0)
for i in range(4):
    for j in range(4):
        if chushi[i+m-1][j+n-1] == 0:
            chushi[i+m-1][j+n-1] = bankuai[i][j]
for i in range(15):
    for j in range(10):
        print(chushi[i][j], end = ' ')
    print()

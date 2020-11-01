#得到输入
n, m = map(int, input().split())
qipan = []
for i in range(n):
    qipan.append([int(i) for i in input().split()])

#建立一个数组，用来标记是否要为0。非0位置后面该为0
check = []
for i in range(n):
    check.append([1]*m)

#检查行
for i in range(n):
    for j in range(1, m-1):
        if qipan[i][j-1] == qipan[i][j] == qipan[i][j+1]:
            check[i][j-1], check[i][j], check[i][j+1] = 0, 0, 0

#检查列
for i in range(1, n-1):
    for j in range(m):
        if qipan[i-1][j] == qipan[i][j] == qipan[i+1][j]:
            check[i-1][j], check[i][j], check[i+1][j] = 0, 0, 0

#改变数组
for i in range(n):
    for j in range(m):
        if check[i][j]:
            continue
        qipan[i][j] = 0

#展示棋盘
for line in qipan:
    for i in line:
        print(i, end = ' ')
    print()

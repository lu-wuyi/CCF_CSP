#得到输入
m, n, q = map(int, input().split())
operatings = []
for i in range(q):
    operatings.append(input().split())

#初始化画布
ans = []
for i in range(n):
    ans.append(['.' for j in range(m)])

#连线函数
def connection(x1, y1, x2, y2):
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            if ans[y][x1] not in ('-', '+'):
                ans[y][x1] = '|'
            elif ans[y][x1] == '-':
                ans[y][x1] = '+'
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            if ans[y1][x] not in ('|', '+'):
                ans[y1][x] = '-'
            elif ans[y1][x] == '|':
                ans[y1][x] = '+'

a = ['-', '|', '+']
#一个记录矩阵
check = []
for i in range(n):
    check.append([0]*m)
#填充函数
def fill(x, y, c):
    if (x>=0 and x<m) and (y>=0 and y<n) and check[y][x] == 0 and (ans[y][x] not in a):
        ans[y][x] = c
        check[y][x] = 1
    else:
        return
    fill(x-1,y,c)
    fill(x+1,y,c)
    fill(x,y-1,c)
    fill(x,y+1,c)

#主程序
for command in operatings:
    if command[0] == '1':
        fill(int(command[1]), int(command[2]), command[3])
        check = []
        for i in range(n):
            check.append([0]*m)
    elif command[0] == '0':
        connection(int(command[1]), int(command[2]), int(command[3]), int(command[4]))

#输出
for line in range(n-1, -1, -1):
    for x in ans[line]:
        print(x, end = '')
    print()


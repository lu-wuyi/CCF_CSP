#得到输入
n, m, k, d = map(int, input().split())

dian = []
for i in range(m):
    dian.append([int(i)-1 for i in input().split()] + [0])
    
need = []
for i in range(k):
    need.append([int(i) for i in input().split()])
    
cant = []
for i in range(d):
    cant.append([int(i) for i in input().split()])

M = [[0]*n for i in range(n)]#地图
M_min = [[0]*n for i in range(n)]

for i in range(d):
    M[cant[i][0]-1][cant[i][1]-1] = 1#将不能去的点设置为1

for i in range(m):
    M[dian[i][0]][dian[i][1]] = 1

def minlu():
#输入两点  探查他们的最短距离, 从第一个点进行广度搜索  搜到第二个点为止
    queue = dian#点的坐标与到该点的距离
    ans = 0
    while queue:
        now = queue.pop(0)
        M_min[now[0]][now[1]] = now[2]
        if now[0] + 1 < n:
            if M[now[0]+1][now[1]] != 1:
                queue.append([now[0]+1, now[1], now[2]+1])
                M[now[0]+1][now[1]] = 1
        if now[0] > 0:
            if M[now[0]-1][now[1]] != 1:
                queue.append([now[0]-1, now[1], now[2]+1])
                M[now[0]-1][now[1]] = 1
        if now[1] + 1 < n:
            if M[now[0]][now[1]+1] != 1:
                queue.append([now[0], now[1]+1, now[2]+1])
                M[now[0]][now[1]+1] = 1
        if now[1] > 0:
            if M[now[0]][now[1]-1] != 1:
                queue.append([now[0], now[1]-1, now[2]+1])
                M[now[0]][now[1]-1] = 1
    return 

#主程序
minlu()
s = 0
for i in range(k):
    s += M_min[need[i][0]-1][need[i][1]-1]*need[i][2]
print(s)

#得到输入
p = int(input())
cate = {}   #cate = {'crm':2, 'git':3, 'game':-1}
for i in range(p):
    a = input().split(sep = ':')
    if len(a) == 2:
        cate[a[0]] = int(a[1])
    else:
        cate[a[0]] = -1

r = int(input())
role = {}   #role = {...'it':'crm:1 git:1 game'...}
for i in range(r):
    a = input().split(maxsplit = 2)
    role[a[0]] = a[2]

u = int(input())
user = {}
for i in range(u):
    a = input().split(maxsplit = 2)
    user[a[0]] = a[2]

#函数  输入查询命令返回ture false 或num
def chaxun(x):
    a,b = x.split()
    if a not in user: #如果a不在user中，无意义输出false
        print('false')
        return
    arole = user[a].split() #得到a的角色列表
    acate = {} #a的权限字典 形式同上方
    for i in arole:
        c = role[i].split() #得到i角色的所有权限列表
        for j in c:
            z = j.split(sep = ':')
            if len(z) == 2:
                if z[0] in acate and int(z[1]) <= acate[z[0]]: #权限已在字典中，且新输入小于旧输入
                    pass
                else:
                    acate[z[0]] = int(z[1])
            else:
                acate[z[0]] = -1

    b = b.split(sep = ':')
    if len(b) == 2: #带等级查询
        if b[0] in acate and int(b[1]) <= acate[b[0]]:
            print('true')
        else:
            print('false')
    elif len(b) == 1: #不带等级查询
        if b[0] not in acate:
            print('false') #不在a的权限中
        else:
            if acate[b[0]] == -1:
                print('true') #不带等级权限
            else:
                print(acate[b[0]])

#主程序
q = int(input())
for i in range(q):
    chaxun(input())
        
    

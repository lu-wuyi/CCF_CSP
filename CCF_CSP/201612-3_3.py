#得到输入
#用字典cate存放权限
p = int(input())
cate = {}
for i in range(p):
    line = input().split(sep = ':')
    if len(line) == 1:       #无等级权限，用''做值
        cate[line[0]] = ''
    else:                    #带等级权限，用int做值
        cate[line[0]] = int(line[1])
#结果形如 cate = {'crm':2, 'git':3, 'game':''}

#用字典roles存放角色，值为该角色的权限列表，权限可能重复
r = int(input())
roles = {}
for i in range(r):
    line = input().split()
    num = int(line[1])
    quanxian = []   #用来记录该角色的所有权限
    for j in range(num):
        role_cate = line[j+2].split(':')
        if len(role_cate) == 1:
            quanxian.append([role_cate[0], ''])
        else:
            quanxian.append([role_cate[0], int(role_cate[1])])
    roles[line[0]] = quanxian
'''
roles ={
'hr':[['crm', 2]],
'it':[['crm', 1], ['git', 1], ['game', '']],
'dev':[['git', 3], ['game', '']],
'qa':[['git', 2]]
}
'''

#用字典users存放用户，值为用户的所有权限，需要对重复的权限进行处理
u = int(input())
users = {}
for i in range(u):
    line = input().split()
    num = int(line[1])
    user_quanxian = {}   #用来存放该用户的所有权限
    for j in range(num):
        quanxian_s = roles[line[2+j]]   #得到该角色的权限列表
        for quanxian in quanxian_s:
            if quanxian[1] == '':       #该权限是不带等级权限
                user_quanxian[quanxian[0]] = ''
            else:                       #该权限是  带等级权限
                if quanxian[0] in user_quanxian:        #该权限已出现在权限字典中
                    if quanxian[1] > user_quanxian[quanxian[0]]:    #新权限等级大于原有等级，更新
                        user_quanxian[quanxian[0]] = quanxian[1]
                else:                   #该权限未出现在字典中，直接加入
                    user_quanxian[quanxian[0]] = quanxian[1]
    users[line[0]] = user_quanxian
'''
users = {
...
'bob':{'crm':2, 'git':1, 'game':''}
...
}
'''

#对查询进行处理
q = int(input())
for i in range(q):
    name, need = input().split()
    need = need.split(':')
    if name not in users:   #如果用户名不存在
        print('false')
        continue
    name_cate = users[name]
    if need[0] not in name_cate:    #如果未拥有该权限
        print('false')
        continue
    if len(need) == 1:  #不带等级查询
        if name_cate[need[0]] == '':    #不带等级权限
            print('true')
        else:
            print(name_cate[need[0]])
    else:               #带等级查询
        if name_cate[need[0]] == '':    #不带等级权限
            print('false')
        else:
            if int(need[1]) > name_cate[need[0]]:   #查询等级大与拥有等级
                print('false')
            else:
                print('true')
    

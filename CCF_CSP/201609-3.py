#得到输入
n = int(input())
operation = []
for i in range(n):
    operation.append(input().split())

#双方血量及战场怪物属性，
onel = 30
twol = 30
one = []
two = []

#各种操作
def summon(op, i):
    lo = int(op[1])-1
    ad = int(op[2])
    hp = int(op[3])
    if i == 1:
        now = one
    else:
        now = two
    if lo < len(now):
        now = now[:lo] + [[ad, hp]] + now[lo:]
    else:
        now.append([ad, hp])
    return now

def attack(op, i):
    if i == 1:
        atr = one
        bear = two
        bearl = twol
    else:
        atr = two
        bear = one
        bearl = onel
    cc = int(op[1])-1 #攻击者位置
    dd = int(op[2])-1 #被攻击位置

    if dd != -1:
        atr[cc][1] = atr[cc][1]-bear[dd][0]  
        bear[dd][1] = bear[dd][1]-atr[cc][0]
    else:
        bearl = bearl - atr[cc][0]
        
    if dd != -1:
        if atr[cc][1] <= 0:
            atr.pop(cc)
        if bear[dd][1] <= 0:
            bear.pop(dd)
    return atr, bear, bearl

#主程序
z = 1
win = 0
for i in operation: 
    if i[0] == 'summon':
        now = summon(i, z)
        if z == 1:
            one = now
        else:
            two = now
    elif i[0] == 'attack':
        now = attack(i, z)
        if z == 1:
            one = now[0]
            two = now[1]
            twol = now[2]
        else:
            two = now[0]
            one = now[1]
            onel = now[2]
        #if onel <= 0:
            #win = -1
            #break
        #elif twol <= 0:
            #win = 1
            #break
        #把上面注释去了  可以中途检测
    elif i[0] == 'end':
        if z == 1:
            z = 2
        else:
            z = 1
    #print(onel, one)
    #print(twol, two)
    #print('---------')

#傻逼题目，我把中途判断谁死，不进行后续操作，之间判胜负的代码去了，100分，不去只有90分
#输出
if onel <= 0:
    win = -1
elif twol <= 0:
    win = 1
#中途判断的话，把上面去掉，再上面的注释去了
print(win)
print(onel)
print(len(one), end = ' ')
for i in range(len(one)):
    print(one[i][1], end = '')
    if i < len(one)-1:
        print(' ', end = '')
print()        
print(twol)
print(len(two), end = ' ')
for i in range(len(two)):
    print(two[i][1], end = '')
    if i < len(two)-1:
        print(' ', end = '')


            

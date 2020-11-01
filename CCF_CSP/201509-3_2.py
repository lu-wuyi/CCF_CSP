#模板生成系统
#re正则表达式匹配
import re
m,n = map(int,input().split())
temple = []#模板
for i in range(m):
    temple.append(input())
vardict = dict()#变量
for i in range(n):
    var,value = input().split(" ",1)
    vardict[var] = eval(value)#清除引号
print(vardict)
 
def trans(matched):#变量替换值函数
    var = matched.group('var')
    if var in vardict:
        return vardict[var]
    else:
        return ""
for i in range(len(temple)):
    print(re.sub(r'{{ (?P<var>\w*) }}',trans,temple[i]))
    #re替换方法，匹配{{  }}格式(?P<var>)命名组，\w匹配小写字母数字和下划线，*表示匹配一个或多个\w
    #trans匹配方法，调用函数将命名组的var替换成值

#得到输入
P = int(input())
now_path = input()
paths = []
check = []
for i in range(P):
    paths.append(input())
    if paths[-1] != '' and paths[-1][0] == '/':
        check.append(0)
    else:
        check.append(1)
        
#对路径分割
def fenge(path):
    length = len(path)
    i = 0
    while(i<length):
        if path[i] == '':
            path.pop(i)
            length -= 1
        else:
            i += 1
    return path

now_path = fenge(now_path.split(sep = '/'))
for i in range(len(paths)):
    paths[i] = fenge(paths[i].split(sep = '/'))

def getpath(path, c):
    ans = []
    if c == 1:
        ans = now_path[:]
    for i in path:
        if i == '..':
            if ans != []:
                ans.pop()
            else:
                if i == path[0]:
                    ans = ['d2']
        elif i == '.':
            pass
        else:
            ans.append(i)
    str_path = ''
    for i in ans:
        str_path += '/' + i
    return str_path

for i in range(len(paths)):
    a = getpath(paths[i], check[i])
    if a != '':
        print(a)
    else:
        print('/')














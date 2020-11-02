import sys
import re

#得到输入
In = sys.stdin.readlines()
in_str = ''
for line in In:
    in_str += line
if in_str[-1] == '\n':
    in_str = in_str[:-1]

A = re.split(r'\n{2,}', in_str)
if A[-1] == '':
    A.pop()

#段落
def qiangdiao(m):
    return '<em>' + m.group('Text') + '</em>'

#链接
def lianjie(m):
    return '<a href="' + m.group('Link') + '">' + m.group('ABC') + '</a>'

#无序列表
def liebiao(m):
    return '<li>' + m.group('abc') + '</li>\n'

#标题
def biaoti(m):
    num = len(m.group('num'))
    return '<h'+str(num)+'>'+m.group('biaoti')+'</h'+str(num)+'>\n'

def chuli(d):
    if d[0] == '#':
        return re.sub(r'(?P<num>#+)\s+(?P<biaoti>.+)', biaoti, d)
    elif d[0] == '*':
        a = re.sub('\*\s+(?P<abc>.+)\n?', liebiao, d)
        return '<ul>\n' + a + '</ul>\n'
    else:
        return '<p>' + d + '</p>\n'

for i in range(len(A)):
    A[i] = re.sub(r'_(?P<Text>[^_]+?)_', qiangdiao, A[i])
    A[i] = re.sub(r'\[(?P<ABC>.+?)\]\((?P<Link>.+?)\)', lianjie, A[i])
    A[i] = chuli(A[i])

out_str = ''
for i in range(len(A)):
    out_str += A[i]
    if i != len(A)-1:
        out_str += ''

if out_str[-1] == '\n':
    out_str = out_str[:-1]
print(out_str)



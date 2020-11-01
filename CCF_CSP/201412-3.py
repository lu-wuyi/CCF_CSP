"""
@File: 201412-3.py
@Author: zhaojin
@Time: 2020/10/6 18:57
@DESCRIPTION: 
"""
import sys
#输入
data_zero = []
for line in sys.stdin:
    data_zero.append(line.split())
#[['buy','9.25','100']...['sell','9.00','1000']...['cancel','1']...]

for i in data_zero:
    if i[0] == 'cancel':
        data_zero[int(i[1]) - 1][0] = ''
    else:
        i[1] = int(i[1])
        i[2] = int(i[2])
#[['',9.25,100]...['sell',9.00,1000]...['cancel',1]...]

#买价的逆序排列
buylist = []
for i in data_zero:
    if i[0] == 'buy':
        buylist.append([i[1],i[2]])
buylist.sort(key = lambda x:x[0],reverse=TURE)
sum = 0
for i in buylist:
    sum += i[1]
    i[1] = sum

#卖价的逆序排列
selllist = []
for i in data_zero:
    if i[0] == 'sell':
        selllist.append([i[1],i[2]])
buylist.sort(key = lambda x:x[0],reverse=TURE)
sum = 0
for i in selllist:
    sum += i[1]
    i[1] = sum


buydict = {}
selldict = {}

#买卖的字典
for i in buylist:
    buydict[i[0]] = i[1]
for i in selllist:
    selldict[i[0]] = i[1]

#求值
price = 0
num = 0

for i in buylist:
    data = min(buydict[i[0]],selldict[i[0]])
    if data > num:
        data, num = num, data
        price = i[0]

print("{:.2f} {:d}".format(price, num))

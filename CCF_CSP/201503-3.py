#得到输入
[a, b, c, y1, y2] = [int(i) for i in input().split()]

#判断x年是不是闰年
def run(x):
    if x%400 == 0 or (x%4 == 0 and x % 100 != 0):
        return 1
    return 0

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#计算y从y1到y2年 的a月第一天是星期几
#到y年有多少天
for y in range(y1, y2+1):
    #y = y1
    sum = 0
    for year in range(1850, y):
        if run(year):
            sum += 366
        else:
            sum += 365
    #到a月有多少天
    for month in range(1,a):
        sum += days[month - 1]
    if a > 2 and run(y):
        sum += 1
    oneday = sum % 7 + 2
    #计算 第b个星期c 是这个月的第几天
    if c >= oneday:
        day = (b-1)*7 + c-oneday + 1
    else:
        day = b*7 + c - oneday + 1
    if (day <= days[a - 1]) or (a == 2 and run(y) and day <=29):
        print('{:d}/{:0>2d}/{:0>2d}'.format(y, a, day))
    else:
        print("none")      
'''        
count = oneday - 1
for y in range(y1,y2):
    if (a<2 or (a==2 and day <=28)) and run(y):
        day -= 2
        count += 2
        if count >= 7:
            day += 7
            count = 0
        if day <= 0:
            day += 7
        if day >days[a - 1]:
            print("none")
        else:
            print('{:d}/{:0>2d}/{:0>2d}'.format(y+1, a, day))
    elif (a>2 or (a==2 and day == 29)) and run(y+1):
        day -= 2
        count += 2
        if count >= 7:
            day += 7
            count = 0
        if day <= 0:
            day += 7
        if day >days[a - 1]:
            print("none")
        else:
            print('{:d}/{:0>2d}/{:0>2d}'.format(y+1, a, day))
    else:
        day -= 1
        count += 1
        if count >= 7:
            day += 7
            count = 0
        if day <= 0:
            day += 7
        if day >days[a - 1]:
            print("none")
        else:
            print('{:d}/{:0>2d}/{:0>2d}'.format(y+1, a, day))

'''            

    

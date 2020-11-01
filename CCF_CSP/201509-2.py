#得到输入
y = int(input())
d = int(input())

#判断是不是闰年
def run(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return 1
    return 0

#计算
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0
if run(y):
    month[1] = 29
for i in range(12):
    days += month[i]
    if d <= days:
        print(i+1)
        days -= month[i]
        day = d - days
        print(day)
        break
    

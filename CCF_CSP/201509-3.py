import sys

#得到输入
[m, n] = [int(i) for i in input().split()]
s = ''
for line in sys.stdin:
    s += line
    m -= 1
    if m == 0:
        break
s = s[:-1]
kdict = {}
for line in sys.stdin:
    [key, data] = line.split(' ', 1)
    key = '{{ ' + key + " }}"
    data = data[1:-2]
    kdict[key] = data
    n -= 1
    if n == 0:
        break
keys = list(kdict)

#KMP函数
def KMP(a):
    kmp = [-1 for i in range(len(a))]
    i = 0
    j = -1
    while(i < len(a)-1):
        if (j == -1 or a[i] == a[j]):
            i += 1
            j += 1
            if (a[i] == a[j]):
                kmp[i] = kmp[j]
            else:
                kmp[i] = j
        else:
            j = kmp[j]
    return kmp
#检查函数，用a检查b
def check(a, b):
    kmp_a = KMP(a)
    i = 0
    j = 0
    while(j < len(a) and i < len(b)):
        if (j == -1 or b[i] == a[j]):
            i += 1
            j += 1
        else:
            j = kmp_a[j]
    if i == len(b) and j != len(a):
        return -1
    else:
        return i - j
#替换函数，用data代替b中的key
def exchange(key, data, b):
    while(1):
        a = check(key, b)
        length = len(key)
        if a != -1:
            b = b[:a] + data + b[a+length:]
        else:
            break
    return b

#主程序
answer = s
for i in keys:
    answer = exchange(i, kdict[i], answer)
print(answer)

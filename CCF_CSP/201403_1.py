N_s = input()
N = int(N_s)
'''
可以用一句话
N = int(input()) 
'''
num = []
num_s = input()
s = ''
for i in num_s:
    if i == ' ':
        num.append(int(s))
        s = ''
    else:
        s += i
num.append(int(s))
'''
输入第二行可以优化
input()输入的是'num num num num'形式
可以用split方法分割成数组
num = input().split()
再用for循环或者列表表达式转成数组列表
for i in range(N):
    num[i] = int(num[i])
或者
num = [int(i) for i in num]
'''

answer = 0
for i in range(N):
    for j in range(i+1, N):
        if num[i]+num[j] == 0:
            answer += 1

print(answer)

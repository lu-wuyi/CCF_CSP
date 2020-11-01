ISBN = input()
s = ''.join(ISBN.split(sep = '-'))
num = [int(i) for i in s[:-1]]

sum = 0
k = 1
for i in range(len(num)):
    sum += num[i]*k
    k += 1

sum = sum%11
if sum == 10:
    sum = 'X'
sum = str(sum)

if sum == ISBN[-1]:
    print("Right")
else:
    print(ISBN[:-1] + sum)

n = int(input())
l = []
answer = [0 for i in range(10000)]
for i in range(n):
    m = [int(j) for j in input().split()]
    a,b,c,d = m[0],m[1],m[2],m[3]
    for j in range(b,d):
        for z in range(j*100+a,j*100+c):
            answer[z] += 1

sum = 0
for i in answer:
    if i != 0:
        sum += 1
    
print(sum)

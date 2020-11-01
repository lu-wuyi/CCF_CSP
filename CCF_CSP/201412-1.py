n = int(input())
count = {}
answer = []
a = input().split()
for i in a:
    i = int(i)
    if i in count:
        count[i] += 1
        answer.append(count[i])
    else:
        count[i] = 1
        answer.append(count[i])
for i in range(n):
    print(answer[i],end = ' ')
print()

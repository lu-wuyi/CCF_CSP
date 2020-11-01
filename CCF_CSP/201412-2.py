n = int(input())
a = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    list_str = input().split()
    a[i] = [int(j) for j in list_str]

answer = []
i, j = 0, 0
answer.append(a[i][j])
while(i < n-1 or j < n-1):
    if (i == 0 and j < n-1):
        j += 1
        answer.append(a[i][j])
        while(j != 0):
            i += 1
            j -= 1
            answer.append(a[i][j])
        continue
    if (j == 0 and i < n-1):
        i += 1
        answer.append(a[i][j])
        while(i != 0):
            i -= 1
            j += 1
            answer.append(a[i][j])
        continue
    if (j == n-1):
        i += 1
        answer.append(a[i][j])
        while(i != n-1):
            i += 1
            j -= 1
            answer.append(a[i][j])
        continue
    if (i == n-1):
        j += 1
        answer.append(a[i][j])
        while(j != n-1):
            i -= 1
            j += 1
            answer.append(a[i][j])
        continue

for i in range(n*n):
    print(answer[i],end = ' ')
print()

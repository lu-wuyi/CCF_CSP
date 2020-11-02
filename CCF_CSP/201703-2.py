n = int(input())
m = int(input())
student = []
for i in range(1, n+1):
    student.append(i)

for i in range(m):
    a, b = [int(i) for i in input().split()]
    c = student.index(a)
    student.remove(a)
    student.insert(c+b, a)

for i in range(n):
    print(student[i], end = ' ')
print()
    

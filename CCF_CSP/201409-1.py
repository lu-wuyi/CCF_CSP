n = int(input())
s = input()
mylist = [int(i) for i in s.split()]

sum = 0
for i in range(n-1):
    for j in range(i+1,n):
        if mylist[i] - mylist[j] == 1 or mylist[i] - mylist[j] == -1:
            sum += 1
    
print(sum)

n = int(input())
inlist  = [int(i) for i in input().split()]

sum =0
for i in range(n):
    if i == 0 or i == n-1:
        continue
    if (inlist[i-1]-inlist[i])*(inlist[i]-inlist[i+1])<0:
        sum += 1

print(sum)

n = int(input())
inlist = [int(i) for i in input().split()]

M = 0
for i in range(1, n):
    if abs(inlist[i]- inlist[i-1]) > M:
        M = abs(inlist[i] - inlist[i-1])
        
print(M)

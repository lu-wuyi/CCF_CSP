n = int(input())
alist = [int(i) for i in input().split()]

alist.sort()

mid = alist[n//2]

low = 0
high = 0
for i in alist:
    if i < mid:
        low += 1
    elif i > mid:
        high += 1

if low == high:
    print(mid)
else:
    print(-1)
    

n, k = [int(i) for i in input().split()]
alist = [int(i) for i in input().split()]

num = 0
num_k = 0
while(alist):
    num_k += alist.pop(0)
    if num_k >= k:
        num += 1
        num_k = 0
if num_k > 0:
    num += 1
print(num)

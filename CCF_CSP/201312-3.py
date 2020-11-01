n = int(input())
s = input().split()
h_list = [int(i) for i in s]

m = 0
for i in range(n):
    h = h_list[i]
    wide = 1
    j = i
    while(j >= 0 and h_list[j] >= h):
        j -= 1
        wide += 1
    wide -= 1
    j = i
    while(j < len(h_list) and h_list[j] >= h):
        j += 1
        wide += 1
    wide -= 1
    i_max = h*wide
    if i_max > m:
        m = i_max

print(m)

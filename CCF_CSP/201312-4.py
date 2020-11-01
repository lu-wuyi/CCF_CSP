n = int(input())

def c(a,b):
    f = 1
    d = 1
    for i in range(b):
        f = f*(a-i)
        d = d*(1+i)
    return f//d

sum = 0
for i in range(2, n-1):
    j = n - i
    z = c(n-1, i)
    sum += z*(j-1)*(i-1)

sum = int(sum % 1000000007)

print(sum)
    

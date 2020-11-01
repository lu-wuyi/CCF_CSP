N = int(input())
s = input()
a = ''
nums = []
for j in range(len(s)):
    if s[j] == ' ':
        nums.append(int(a))
        a = ''
    else:
        a += s[j]
nums.append(int(a))

answer = {}
for i in range(N):
    if answer.get(nums[i]) == None:
        answer[nums[i]] = 1
    else:
        answer[nums[i]] += 1

m = 0
n = 0
for i in range(N):
    b = answer[nums[i]]
    if b > m:
        n = nums[i]
        m = b
    elif b == m and nums[i] < n:
        n = nums[i]

print(n)
            
    

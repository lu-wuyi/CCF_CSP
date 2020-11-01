class Window():
    def __init__(self, x1, y1, x2, y2, name):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.name = name
        
    def check(self, x, y):
        if x >= self.x1 and x <= self.x2 and y >= self.y1 and y <= self.y2:
            return 1
        else:
            return 0

[N, M] = [int(i) for i in input().split()]

l = []
for i in range(N):
    [x1, x2, y1, y2] = [int(i) for i in input().split()]
    l = [Window(x1,x2,y1,y2,i+1)] + l

for i in range(M):
    [x, y] = [int(i) for i in input().split()]
    for j in range(N):
        if l[j].check(x,y):
            print(l[j].name)
            l = [l[j]] + l[:j] + l[j+1:]
            break
        if j == N-1:
            print("IGNORED")

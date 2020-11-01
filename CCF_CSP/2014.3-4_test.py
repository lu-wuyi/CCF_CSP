def getDist(x1, y1, x2, y2):
    return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
def bfs():
    queue = [[0, 0, 0]]  # [当前点，步数(层数)，新增类型的结点个数]
    visited = [False] * len(graph)
    visited[0] = True
    while queue:    #pop(0)用来返回第一个数
        node, step, k_count = queue.pop(0)# 搜到第2个点就返回层数减1 pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        if node == 1:
            return step - 1     # 找邻点，如果新增类型的结点 超过k就不入队
        for nd in graph[node]:      # 遇到新增类型的结点，计数加一，标号是n以及之后的就是新增结点
            k_count_tem = (k_count + 1)  if nd >= luyouqi else k_count
            if not visited[nd] and k_count_tem <= zuiduo:
                queue.append([nd, step + 1, k_count_tem])
                visited[nd] = True
luyouqi, weizhi, zuiduo, mi = map(int, input().split())  #bfs，队列里的每个元素是一个列表 [ node 结点，step步数（层数） ,k_count 遍历到新增结点的个数 ]
graph = [[] for _ in range(luyouqi + weizhi)]
nodes = []
for i in range(luyouqi + weizhi):
    nodes.append([int(e) for e in input().split()])

# 整理点，两点距离<=r的连线，构图
for i in range(len(nodes) - 1):
    for j in range(i + 1, len(nodes)):
        x1, y1 = nodes[i]
        x2, y2 = nodes[j]
        if getDist(x1, y1, x2, y2) <= mi:
            graph[i].append(j)
            graph[j].append(i)
print(bfs())

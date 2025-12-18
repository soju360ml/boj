import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value, node=None):
        self.value = value
        self.node = node

class HeapQueue:
    def __init__(self):
        self.nodes = []
        self.count = 0
    def __swap(self, l_idx, r_idx):
        self.nodes[l_idx], self.nodes[r_idx] = self.nodes[r_idx], self.nodes[l_idx]
    def insert(self, value, node):
        new_node = Node(value, node)
        self.nodes.append(new_node)
        self.count += 1
        self.upheap()
    def upheap(self):
        cur_idx = self.count - 1
        while cur_idx > 0:
            par_idx = (cur_idx - 1) // 2
            if self.nodes[cur_idx].value < self.nodes[par_idx].value:
                self.__swap(cur_idx, par_idx)
                cur_idx = par_idx
            else:
                break
    def extract(self):
        r = self.nodes[0]
        self.nodes[0] = self.nodes[self.count - 1]
        del self.nodes[self.count - 1]
        self.count -= 1
        if self.count > 0:
            self.downheap()
        return r
    def downheap(self):
        cur_idx = 0
        child_idx = 1
        while cur_idx < self.count // 2:
            child_idx = cur_idx * 2 + 1
            if child_idx + 1 < self.count and self.nodes[child_idx].value > self.nodes[child_idx + 1].value:
                child_idx += 1
            if self.nodes[cur_idx].value > self.nodes[child_idx].value:
                self.__swap(cur_idx, child_idx)
                cur_idx = child_idx
                continue
            else:
                break

V, E = map(int, input().split())
edges = []
adjacency = {i: {} for i in range(1, V + 1)}
count = 0
cost = 0
visited = set()
heapq = HeapQueue()
for _ in range(E):
    node1, node2, weight = map(int, input().split())
    if node2 not in adjacency[node1]:
        adjacency[node1][node2] = weight
        adjacency[node2][node1] = weight
    else:
        if adjacency[node1][node2] > weight:
            adjacency[node1][node2] = weight
            adjacency[node2][node1] = weight
            
heapq.insert(0, 1)
while count < V:
    cur = heapq.extract()
    if cur.node in visited:
        continue
    visited.add(cur.node)
    count += 1
    cost += cur.value
    for k, v in adjacency[cur.node].items():
        heapq.insert(v, k)
print(cost)
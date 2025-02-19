class Graph:
    def __init__(self, size, setting=False):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        if setting:
            self.setting_All_connecting()
        self.tag = {0 : ['GS25', 30], 
                    1 : ['CU', 60], 
                    2 : ['Seven11', 10], 
                    3 : ['MiniStop', 90], 
                    4 : ['Emart24', 40]}

    def setting_All_connecting(self):
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    self.graph[i][j] = 1

    def __str__(self):
        return "\n".join(str(row) for row in self.graph)

    def set(self, edge_dict):
        row = list(edge_dict.keys())[0]
        values = list(edge_dict.values())[0]

        if not (0 <= row < self.size):
            raise ValueError(f"유효하지 않은 row 번호입니다: {row}")
        if len(values) != self.size:
            raise ValueError(f"values 길이는 {self.size}이어야 합니다.")

        self.graph[row] = values

    def dfs(self, start):
        max = 0
        visited = []
        stack = [start]

        while stack:
            node = stack.pop()
            if self.tag[node][1] > max:
                max = self.tag[node][1]
                store = self.tag[node][0]
            if node not in visited:
                visited.append(node)
                # 현재 노드(node)의 인접 노드 탐색
                for neighbor in range(self.size - 1, -1, -1):
                    if self.graph[node][neighbor] == 1 and neighbor not in visited:
                        stack.append(neighbor)
        print(f'허니버터칩 많은 곳 {store} : {max}개')
        return visited

graph = Graph(5)
graph.set({0 : [0,1,1,0,0]})
graph.set({1 : [1,0,1,1,0]})
graph.set({2 : [1,1,0,1,0]})
graph.set({3 : [0,1,1,0,1]})
graph.set({4 : [0,0,0,1,0]})

print(graph.dfs(0))
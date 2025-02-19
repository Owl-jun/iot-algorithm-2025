class Graph:
    def __init__(self, size, setting=False):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        if setting:
            self.setting_All_connecting()

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

if __name__ == "__main__":

    G1 = Graph(6)
    G1.set({0 : [0,1,1,0,0,0]})
    G1.set({1 : [1,0,0,1,0,0]})
    G1.set({2 : [1,0,0,1,0,0]})
    G1.set({3 : [0,1,1,0,1,1]})
    G1.set({4 : [0,0,0,1,0,1]})
    G1.set({5 : [0,0,0,1,1,0]})

    print("DFS 방문 순서:", G1.dfs(0))
    print("DFS 방문 순서:", G1.dfs(5))
    print("DFS 방문 순서:", G1.dfs(2))


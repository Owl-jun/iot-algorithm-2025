def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))  # 스택에서 순서를 맞추기 위해 reversed 사용

    return visited


# 무방향 그래프
my_graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

print(dfs(my_graph, 1))  
# 예상 결과: [1, 2, 4, 5, 3, 6] (스택이므로 탐색 순서는 다를 수 있음)

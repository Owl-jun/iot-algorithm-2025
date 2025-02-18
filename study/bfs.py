from collections import deque

def escape_maze(maze, n, m):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([(0,0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx,ny))

    # 도착점이 방문되지 않았다면 -1을 반환 (혹은 예외 처리)
    return maze[n-1][m-1] if maze[n-1][m-1] > 1 else -1  # 도착할 수 없으면 -1 반환

maze = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,0]  # 도착지점 (4,5) 는 벽이므로 도착 불가!
]

print(escape_maze(maze, 5, 6))  # -1 (이동 불가능)

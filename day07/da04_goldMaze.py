
goldMaze = [[1,4,4,2,2],
            [1,3,3,0,5],
            [1,2,4,3,0],
            [3,3,0,4,2],
            [1,3,4,5,3]]

def solution(goldMaze):
    col_len = len(goldMaze[0])
    row_len = len(goldMaze)
    memo = [[0 for _ in range(col_len)] for _ in range(row_len)]
    memo[0][0] = goldMaze[0][0]

    rowSum = colSum = goldMaze[0][0]
    for rIdx in range(1,row_len):
        rowSum += goldMaze[0][rIdx]
        memo[0][rIdx] = rowSum
    for cIdx in range(1,col_len):
        colSum += goldMaze[cIdx][0]
        memo[cIdx][0] = colSum

    for row in range(1,row_len):
        for col in range(1,col_len):
            data = memo[row-1][col] if memo[row-1][col] > memo[row][col-1] else memo[row][col-1]
            memo[row][col] = data + goldMaze[row][col]
    return memo[row_len-1][col_len-1]

print(solution(goldMaze))
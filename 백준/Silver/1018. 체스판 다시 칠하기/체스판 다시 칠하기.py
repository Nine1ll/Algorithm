def min_recoloring(chessboard, N, M):
    patterns = [
        ['W', 'B'] * 4,
        ['B', 'W'] * 4
    ] * 4
    
    def count_recoloring(x, y, pattern):
        count = 0
        for i in range(8):
            for j in range(8):
                if chessboard[x + i][y + j] != pattern[i][j]:
                    count += 1
        return count
    
    min_changes = float('inf')
    for i in range(N - 7):
        for j in range(M - 7):
            changes1 = count_recoloring(i, j, patterns)
            changes2 = count_recoloring(i, j, patterns[::-1])
            min_changes = min(min_changes, changes1, changes2)
    
    return min_changes

# 입력 예시
N, M = map(int, input().split())
chessboard = [input().strip() for _ in range(N)]

# 최소 색칠 횟수 출력
print(min_recoloring(chessboard, N, M))

def solve_n_queens():
    n = 8
    board = [[0 for x in range(n)] for y in range(n)]
    solutions = []
    
    def is_valid(board, row, col):
        # Проверяем, что нет ферзей на горизонтали и вертикали
        for i in range(n):
            if board[row][i] == 1 or board[i][col] == 1:
                return False
        # Проверяем, что нет ферзей на диагоналях
        for i in range(n):
            for j in range(n):
                if (i + j == row + col) or (i - j == row - col):
                    if board[i][j] == 1:
                        return False
        return True
    
    def solve(board, row):
        if row == n:
            # Добавляем найденное решение в список решений
            solutions.append(board)
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 1
                solve(board, row+1)
                board[row][col] = 0
    
    solve(board, 0)
    return len(solutions)

print(solve_n_queens())

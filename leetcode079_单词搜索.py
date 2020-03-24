class Solution:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def exist(self, board, word):
        row = len(board)
        if row == 0:
            return False
        col = len(board[0])
        visited = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:# 将该路径标为已经走过
                    visited[i][j] = 1
                    if self.backtrack(i, j, visited, board, word[1:]) == True:
                        return True
                    else: # 回溯
                        visited[i][j] = 0
        return False
    def backtrack(self, i, j, visited, board, word):
        if len(word) == 0:
            return True
        for direct in self.directions:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                # 忽略已经走过的路径
                if visited[cur_i][cur_j] == 1:
                    continue
                visited[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, visited, board, word[1:]) == True:
                    return True
                else:# 回溯
                    visited[cur_i][cur_j] = 0
        return False